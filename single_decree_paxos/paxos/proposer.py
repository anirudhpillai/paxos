from .proposal import Proposal
from binascii import hexlify

import os
import random


class Proposer:
    """
    Proposer proposes a value to a majority of Acceptors
    """
    def __init__(self, acceptors):
        self.acceptors = acceptors
        self.proposal_number = 0
        self.proposal_value = hexlify(os.urandom(3)).decode()
        self.proposal = Proposal(self.proposal_number, self.proposal_value)

    def prepare(self):
        """
        The proposer randomly selects a majority of Acceptors and sends them
        a prepare request with the proposal_number and proposal_value
        """
        # Increase proposal number
        self.proposal.increment()

        majority = len(self.acceptors) // 2 + 1

        # randomly select majority of acceptors
        majority_set = random.sample(
            self.acceptors,
            random.choice(range(majority, len(self.acceptors)))
        )

        # majority_set = self.acceptors

        responses = []

        for acceptor in majority_set:
            resp = acceptor.prepare(self.proposal)
            if resp:
                responses.append(resp)

        if len(responses) < majority:
            return  # Not enough responses

        # chooses proposal with highest proposal number
        prepared_proposal = max(responses)
        selected_proposal = Proposal(
            self.proposal.number, prepared_proposal.value
        )
        self.proposal = selected_proposal
        self.accept_request()

    def accept_request(self):
        majority = len(self.acceptors) // 2 + 1

        # randomly select majority of acceptors
        majority_set = random.sample(
            self.acceptors,
            random.choice(range(majority, len(self.acceptors)))
        )

        for acceptor in self.acceptors:
            acceptor.accept(self.proposal)
