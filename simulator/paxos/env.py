import os
import signal
import sys
import time

from proposer import Proposer
from acceptor import Acceptor

NACCEPTORS = 3
NPROPOSERS = 2


class Env:
    def __init__(self):
        self.procs = {}

    def send_msg(self, dst, msg):
        if dst in self.procs:
            self.procs[dst].deliver(msg)

    def add_proc(self, proc):
        self.procs[proc.id] = proc
        proc.start()

    def remove_proc(self, pid):
        del self.procs[pid]

    def run(self):
        proposers = range(0, NPROPOSERS)
        acceptors = range(NPROPOSERS, NPROPOSERS + NACCEPTORS)

        for i in acceptors:
            pid = "Acceptor %d" % i
            Acceptor(self, i)

        for i in proposers:
            pid = "Proposer %d" % i
            Proposer(self, acceptors, i, i)

        for i in acceptors:
            print(self.procs[i].state)

    def terminate_handler(self, signal, frame):
        self._graceful_exit()

    def _graceful_exit(self, exit_code=0):
        sys.stdout.flush()
        sys.stderr.flush()
        os._exit(exit_code)


def main():
    e = Env()
    e.run()
    signal.signal(signal.SIGINT, e.terminate_handler)
    signal.signal(signal.SIGTERM, e.terminate_handler)
    signal.pause()


main()
