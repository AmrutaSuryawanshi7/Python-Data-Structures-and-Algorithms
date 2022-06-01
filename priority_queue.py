"""
Python Data Structures - A Game-Based Approach
Priority Queue Class based on heapq.
"""

import heapq


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

    def __str__(self):
        return str(self.elements)


if __name__ == "__main__":
    pq = PriorityQueue()
    print(pq)
    pq.put("Amar", 2)
    pq.put("Rutvik", 3)
    pq.put("Amruta", 1)
    print(pq)
    print(pq.get())
    print(pq.get())
    print(pq.get())
    print(pq)
