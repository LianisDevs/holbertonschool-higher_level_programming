"""
This is the module containing the CountedIterator class
"""


class CountedIterator():
    """
    This is the CountedIterator class
    """
    def __init__(self, data):
        self.iterator = iter(data)
        self.counter = 0

    def get_count(self):
        return self.counter

    def __next__(self):
        self.counter += 1
        return self.iterator.__next__()
