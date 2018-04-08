"""
This file defines the Message super class and all the other
types of messages used in the adapted Simple Paxos protocol.
"""


class Message:
    """
    Message super class which all the differnt message types inherit.

    Attributes:
        :src       sender of the message
        :proposal  proposal contained in the message
    """

    def __init__(self, src, proposal):
        self.src = src
        self.proposal = proposal

    def __str__(self):
        return str(self.__dict__)


class PrepareRequestMessage(Message):
    def __init__(self, src, proposal):
        Message.__init__(self, src, proposal)


class AcceptRequestMessage(Message):
    def __init__(self, src, proposal):
        Message.__init__(self, src, proposal)


class PromiseResponseMessage(Message):
    def __init__(self, src, proposal):
        Message.__init__(self, src, proposal)


class NackResponseMessage(Message):
    def __init__(self, src):
        Message.__init__(self, src, (-1, -1))
