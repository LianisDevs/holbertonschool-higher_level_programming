"""
This is the module containing the VerboseList class
"""


class VerboseList(list):
    """
    This is the VerboseList class

    Parameters: inherits list
    """

    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item):
        super().extend(item)
        length = len(item)
        print("Extended the list with [{}] items".format(length))

    def remove(self, item):
        try:
            super().remove(item)
            print("Removed [{}] from the list".format(item))
        except ValueError:
            raise ValueError("{} not found in the list".format(item))

    def pop(self, item=-1):
        print("Popped [{}] from the list".format(self[item]))
        return super().pop(item)
