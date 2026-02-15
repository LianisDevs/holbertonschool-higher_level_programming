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
        try:
            next = self.iterator.__next__()
            self.counter += 1
            return next
        except StopIteration:
            raise StopIteration("No more items.")
