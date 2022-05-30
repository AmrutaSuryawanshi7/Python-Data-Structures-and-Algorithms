"""
Python Data Structures - A Game-Based Approach
Queue class - FIFO (First-In, First-Out)
---------------------------------------------------------------------
queue_ll.py : different file name because there's an existing module in Python called queue,
and you might come across quite a common and hard to debug error if you name your own module same as something that
already exists. Then you would actually override that module and all the methods you expect to find won't work.
So one way to avoid that is to, just rename it to something a little different from the existing module.
---------------------------------------------------------------------
"""

from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return not self.items

    def peek(self):
        return self.items[0]

    def __str__(self):
        return str(self.items)


"""
Reason of writing __main__, because if we ever wanted to import above class into a different file, 
we could do so without executing with below code, that keeps it modular. 
"""
if __name__ == "__main__":
    q = Queue()
    print(q)
    q.enqueue('A')
    q.enqueue('B')
    q.enqueue('C')
    q.enqueue('D')
    print(q)
    q.dequeue()
    print(q)
    print(q.size())
    print(q.peek())
