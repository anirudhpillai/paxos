from paxos.acceptor import Acceptor
from paxos.proposer import Proposer
from paxos.learner import Learner


majority = 3
no_of_proposers = 2

learner = Learner(majority)
acceptors = [Acceptor(learner) for _ in range(majority * 2 - 1)]
proposers = [Proposer(acceptors) for _ in range(no_of_proposers)]


while not learner.concensus_achieved():
    for proposer in proposers:
        proposer.propose()
