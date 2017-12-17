from process import Process
from message import AcceptRequestMessage, PrepareRequestMessage, \
    PromiseResponseMessage, NackResponseMessage


class Proposer(Process):
    def __init__(self, env, acceptors, p_no, p_val):
        Process.__init__(self, env, p_no)
        self.state = ("PInit", p_no, p_val)
        self.acceptors = acceptors
        self.env = env
        self.env.add_proc(self)

    def send_prepare_req(self):
        _, p_no, p_val = self.state
        for acceptor in self.acceptors:
            self.send_msg(
                acceptor,
                PrepareRequestMessage(p_no, (p_no, p_val))
            )

    def send_accept_req(self):
        _, p_no, p_val = self.state
        for acceptor in self.acceptors:
            print("Sending msg")
            self.send_msg(
                acceptor,
                AcceptRequestMessage(p_no, (p_no, p_val))
            )

    def body(self):
        _, p_no, p_val = self.state

        self.send_prepare_req()
        self.state = ("PWaitPrepResp", [], p_no, p_val)

        while True:
            msg = self.get_next_msg()
            print("msg", msg)
            if isinstance(msg, PromiseResponseMessage):
                print("Recv Promise")
                if self.state[0] == "PWaitPrepResp":
                    src = msg.src
                    recv_p_no, recv_p_val = msg.proposal
                    recv_promises = self.state[1]

                    if src not in map(lambda x: x[0], recv_promises):
                        recv_promises.append((src, recv_p_no, recv_p_val))
                        if sorted(map(lambda x: x[0], recv_promises)) == sorted(self.acceptors):
                            recv_promises.sort(key=lambda x: x[1])
                            highest_numbered_value = recv_promises[0][2]
                            self.state = (
                                "PSentAccReq", p_no, highest_numbered_value
                            )
                            self.send_accept_req()
                            print("Exiting proposer", p_no)
                            break
                        else:
                            self.state = (
                                "PWaitPrepResp", recv_promises, p_no, p_val
                            )
            elif isinstance(msg, NackResponseMessage):
                print("Exiting proposer", p_no)
                break
