class LinkedList(object):
    def __init__(self, key, value=None,):
        self.key = key
        self.value = value
        self.next = None
        self.length = 1

    def set_next(self, next):
        if isinstance(next, LinkedList):
            self.next = next
        else:
            raise TypeError("Type needs to be LinkedList")

    def get_next(self):
        return self.next

    def len(self):
        length=self.length
        nod = self.get_next()
        while nod is not None:
            length += 1
            nod = nod.get_next()
        return length+1



    def __str__(self):
        return f"[Key is {self.key} Value is {self.value}] ---> {self.next}"


