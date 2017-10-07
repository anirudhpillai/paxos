from .proposal import Proposal
from binascii import hexlify

import os
import random
import time
import threading


class Proposer:
    """
    Proposer proposes a value to a majority of Acceptors
    """

    def __init__(self, acceptors):
        self.acceptors = acceptors
        self.majority = len(self.acceptors) // 2 + 1
        self.proposal_number = 0
        self.proposal_value = hexlify(os.urandom(3)).decode()
        self.proposal = Proposal(self.proposal_number, self.proposal_value)

        print("Proposer: ", self.proposal_value)

    def propose(self):
        """
        The proposer tries to propose the value in an asynchronous way.
        It call the prepare method in a new thread
        """
        proposal_thread = threading.Thread(target=self.prepare)
        proposal_thread.start()

    def prepare(self):
        """
        The proposer randomly selects a majority of Acceptors and sends them
        a prepare request with the proposal_number and proposal_value.
        If it receives a majority response then it sends out the accept_request
        """
        # Increase proposal number
        self.proposal.increment()

        majority_set = self._select_majority()
        # majority_set = self.acceptors

        responses = []

        for acceptor in majority_set:
            resp = acceptor.prepare(self.proposal)
            # simulate delay in receiving request
            time.sleep(random.choice(range(20)) / 10)
            if resp:  # if acceptor didn't ignore prepare request
                responses.append(resp)

        if len(responses) < self.majority:
            return  # Majority of responses not received

        # chooses proposal with highest proposal number
        prepared_proposal = max(responses)
        selected_proposal = Proposal(
            self.proposal.number, prepared_proposal.value
        )
        self.proposal = selected_proposal
        self.send_accept_request()

    def send_accept_request(self):
        """
        Once proposer receives promises from a majority of acceptors,
        it sends out an accept request to another majority of receivers
        """
        majority_set = self._select_majority()

        for acceptor in majority_set:
            acceptor.accept(self.proposal)

    def _select_majority(self):
        """
        Randomly selects a majority of acceptors
        """
        # randomly select majority of acceptors
        majority_set = random.sample(
            self.acceptors,
            random.choice(range(self.majority, len(self.acceptors)))
        )

        return majority_set
