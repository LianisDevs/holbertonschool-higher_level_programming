#!/usr/bin/python3

class VerboseList(list):

    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item):
        super().extend(item)
        print("Extended the list with [{}] items".format(len(item)))

    def remove(self, item):
        try:
            super().remove(item)
            print("Removed [{}] from the list".format(item))
        except Exception:
            print("{} not found in the list".format(item))

    def pop(self, item=-1):
        print("Popped [{}] from the list".format(self[item]))
        super().pop(item)
