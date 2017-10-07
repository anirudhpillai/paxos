from paxos.acceptor import Acceptor
from paxos.proposer import Proposer
from paxos.learner import Learner


majority = 3

learner = Learner(majority)
acceptors = [Acceptor(learner) for _ in range(majority * 2 - 1)]
proposer = Proposer(acceptors)

proposer.prepare()
