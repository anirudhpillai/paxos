import threading


class Acceptor:
    """
    Acceptor stores the highest proposal number that it has promised.
    """

    def __init__(self, learner):
        self.accepted_proposal = None
        self.promised_number = 0
        self.learner = learner
        self.lock = threading.RLock()

    def prepare(self, proposal):
        """
        Asks the Acceptor to prepare a proposal.
        The Acceptor ignores the proposal if it has already made a promised
        to ignore proposals with proposal.number <= self.promised_number.
        """
        with self.lock:
            if proposal.number > self.promised_number:
                # promise not to accept proposals < proposal.number
                self.promised_number = proposal.number

                if self.accepted_proposal:
                    return self.accepted_proposal
                else:
                    return proposal

    def accept(self, proposal):
        """
        The Acceptor receives an accept request and only accepts the
        proposal if it hasn't already promised to ignore proposals with
        proposal.number less than self.promised_number where
        self.promised_number > proposal.number
        """
        with self.lock:
            if proposal.number >= self.promised_number:
                self.accepted_proposal = proposal
                # inform learner that it has accepted a proposal
                self.learner.inform(self.accepted_proposal)
                return proposal
