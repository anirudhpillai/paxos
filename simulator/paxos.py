from paxos.acceptor import Acceptor
from paxos.proposer import Proposer
from paxos.learner import Learner


# TODO: Need to improve simulation to accomodate more proposers and acceptors.
majority = 3
no_of_proposers = 3

learner = Learner(majority)
acceptors = [Acceptor(learner) for _ in range(majority * 2 - 1)]
proposers = [Proposer(acceptors) for _ in range(no_of_proposers)]


while not learner.concensus_achieved():
    for proposer in proposers:
        proposer.propose()
