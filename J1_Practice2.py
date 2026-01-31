# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#5  (Packages delivered)
#2  (Collisions)
'''
Problem: Cupcake Party (2022 J1)
The Scenario: A class is having a party. There are 28 students in the class.

A regular box holds 8 cupcakes.

A small box holds 3 cupcakes.

The Goal: Given the number of regular and small boxes, how many cupcakes will be left over after every student gets exactly one?

Sample Input:

Plaintext
2 (Regular boxes)
5 (Small boxes)
'''

children=32
regular_box=8
small_box=5
total=2*regular_box+3*small_box
remaining=total-children
print("remaining=",remaining)