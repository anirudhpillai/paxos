import sys


class Learner:
    """
    Learner finds out when a propal has been accepted by a majority
    of acceptors
    """
    def __init__(self, majority):
        self.acceptance_count = {}
        self.majority = majority

    def inform(self, proposal):
        if proposal in self.acceptance_count:
            self.acceptance_count[proposal] += 1
        else:
            self.acceptance_count[proposal] = 1

        # check whether any proposal has been accepted by a majority
        for k, v in self.acceptance_count.items():
            if v >= self.majority:
                print("Proposal Accepted")
                print(k)
                sys.exit()
