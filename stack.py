"""
Python Data Structure - A Game-Based Approach
Stack Class - LIFO (Last-In, First-Out)
"""


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        # return len(self.items) == 0
        return not self.items

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        # -1 : Last item in the list
        return self.items[-1]

    def size(self):
        return len(self.items)

    # It enables us to use the print statement only by calling class & run
    def __str__(self):
        return str(self.items)


"""
Reason of writing __main__, because if we ever wanted to import above class into a different file, 
we could do so without executing with below code, that keeps it modular. 
"""
if __name__ == "__main__":
    s = Stack()
    print(f"List {s}")
    print(f"is_empty {s.is_empty()}")
    s.push(1)
    s.push(4)
    s.push(9)
    print(f"List {s}")
    print(f"Pop {s.pop()}")
    print(f"List {s}")
    print(f"Peek {s.peek()}")
    print(f"is_empty {s.is_empty()}")
