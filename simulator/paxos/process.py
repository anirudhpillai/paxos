import multiprocessing
import threading


class Process(threading.Thread):
    """
    Attributes:
        :state  current state of the Acceptor
        :id     id of the Acceptor
        :env    environment this Acceptor is running in
    """

    def __init__(self, env, id):
        super(Process, self).__init__()
        self.inbox = multiprocessing.Manager().Queue()
        self.env = env
        self.id = id

    def run(self):
        try:
            self.body()
            self.env.remove_proc(self.id)
        except EOFError:
            print("Exiting...")

    def get_next_msg(self):
        return self.inbox.get()

    def send_msg(self, dst, msg):
        self.env.send_msg(dst, msg)

    def deliver(self, msg):
        self.inbox.put(msg)
