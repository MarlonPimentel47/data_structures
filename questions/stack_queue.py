from data_structures.structures import Stack


#  implement queue using two stacks
#  needs enqueue and dequeue methods
class QueueVariant:

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, val):
        self.s1.push(val)

    def dequeue(self):
        if self.s2.is_empty():
            while not self.s1.is_empty():
                self.s2.push(self.s1.pop())

        val = self.s2.pop()
        return val


def test():

    q = QueueVariant()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    print("1", q.dequeue())
    print("2", q.dequeue())
    print("3", q.dequeue())

    q.enqueue(10)
    print("4", q.dequeue())
    print("5", q.dequeue())
    print("10", q.dequeue())


test()
