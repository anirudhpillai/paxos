class Proposal:
    """
    Proposal has a proposal number and proposal value
    """
    def __init__(self, number, value):
        self.number = number
        self.value = value

    def __lt__(self, other):
        return self.number < other.number

    def __str__(self):
        return "Proposal: value -> {}, number -> {} ".format(
            self.value,
            self.number
        )

    def __hash__(self):
        return hash((self.number, self.value))

    def __eq__(self, other):
        return self.number == other.number and self.value == other.value

    def increment(self):
        self.number += 1
