class Message:
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
