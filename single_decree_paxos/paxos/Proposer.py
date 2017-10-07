import random


class Proposer:
    """
    Proposer proposes a value to a majority of Acceptors
    """
    def __init__():
        self.proposal_number = 0
        self.proposal_value = "init"

    def prepare(acceptors):
        """
        The proposer randomly selects a majority of Acceptors and sends them
        a prepare request with the proposal_number and proposal_value
        """
        majority = len(acceptors) // 2 + 1
        # randomly select majority of acceptors
        majority_set = random.sample(acceptors, majority)

        responses = []

        for acceptor in majority_set:
            resp = acceptor.prepare(self.proposal_number, self.proposal_value)
            if resp:
                responses.append(resp)

        if not responses:
            return
