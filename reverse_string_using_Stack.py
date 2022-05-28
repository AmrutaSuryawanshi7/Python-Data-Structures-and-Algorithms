"""
Stack challenge - Reverse the string
"""

import stack

string = "gninraeL nIdekniL htiw tol a nraeL"
reversed_string = ""
s = stack.Stack()

# Your solution here.
for letter in string:
    s.push(letter)

while not s.is_empty():
    reversed_string += s.pop()

print(reversed_string)
