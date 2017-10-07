class Acceptor:
    """
    Acceptor stores the highest proposal number that it has promised.
    """
    def __init__(self, learner):
        self.accepted_proposal = None
        self.promised_number = 0
        self.learner = learner

    def prepare(self, proposal):
        if not self.accepted_proposal:
            # promise not to accept proposals < proposal.number
            self.promised_number = proposal.number
            return proposal

        if proposal.number > self.promised_number:
            self.promised_number = proposal.number

            if self.accepted_proposal:
                return self.accepted_proposal
            else:
                return proposal

    def accept(self, proposal):
        if proposal.number >= self.promised_number:
            self.accepted_proposal = proposal
            self.inform_learner()
            return proposal

    def inform_learner(self):
        self.learner.inform(self.accepted_proposal)
