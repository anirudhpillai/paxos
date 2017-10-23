import threading


class Learner:
    """
    Learner finds out when a propal has been accepted by a majority
    of acceptors
    """

    def __init__(self, majority):
        self.acceptance_count = {}
        self.majority = majority
        self.value_accepted = False
        self.lock = threading.RLock()

    def inform(self, proposal):
        """
        An Acceptor informs the learner that it has accepted a value.
        The Learner then checks if a majority of Acceptors
        have agreed on a value.
        """
        if self.concensus_achieved():
            return

        if proposal in self.acceptance_count:
            self.acceptance_count[proposal] += 1
            if self.acceptance_count[proposal] >= self.majority:
                with self.lock:
                    self.value_accepted = True
                print("Proposal Accepted")
                print(proposal)
        else:
            self.acceptance_count[proposal] = 1

    def concensus_achieved(self):
        with self.lock:
            return self.value_accepted
