from .process import Process
from .message import AcceptRequestMessage, PrepareRequestMessage, \
    PromiseResponseMessage, NackResponseMessage


class Acceptor(Process):
    """
    Implementation of the Acceptor in the adapted Simple Paxos protocol.

    Attributes:
        :state  current state of the Acceptor
        :id     id of the Acceptor
        :env    environment this Acceptor is running in
    """

    def __init__(self, env, id):
        Process.__init__(self, env, id)
        self.state = ("AInit",)
        self.env = env
        self.env.add_proc(self)
        self.id = id

    def send_promise_resp(self, to):
        p_no, p_val = self.state[1]
        self.send_msg(to, PromiseResponseMessage(self.id, (p_no, p_val)))

    def send_nack_resp(self, to):
        self.send_msg(to, NackResponseMessage(self.id))

    def body(self):
        while True:
            msg = self.get_next_msg()
            p_no, p_val = msg.proposal

            if isinstance(msg, PrepareRequestMessage):
                if self.state[0] == "AInit":
                    self.state = ("APromised", msg.proposal)
                    self.send_promise_resp(p_no)
                elif self.state[0] == "APromised":
                    promised_no, _ = self.state[1]
                    if p_val < promised_no:
                        self.send_nack_resp(p_no)
                    else:
                        self.state = ("APromised", msg.proposal)
                        self.send_promise_resp(p_no)
                else:
                    self.send_nack_resp(p_no)
            elif isinstance(msg, AcceptRequestMessage):
                if self.state[0] == "AInit":
                    self.state = ("AAccepted", msg.proposal)
                else:
                    promised_no, _ = self.state[1]
                    if p_val >= promised_no:
                        self.state = ("AAccepted", msg.proposal)
                        print("Node %d has state %s" % (self.id, self.state))
