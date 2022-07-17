"""
Question1
Create a function that takes three integer arguments (a, b, c) and returns the amount of
integers which are of equal value.
Examples
equal(3, 4, 3) ➞ 2
equal(1, 1, 1) ➞ 3
equal(3, 4, 1) ➞ 0
Notes
Your function must return 0, 2 or 3.
"""

def equal(a,b,c):
    l = []
    for i in [a,b,c]:
        l.append([a,b,c].count(i))
    if max(l) == 1:
        return 0
    return max(l)

a = int(input("Enter Number 1 "))
b = int(input("Enter Number 2 "))
c = int(input("Enter Number 3 "))
print("equal(",a,',',b,',',c,") ➞",equal(a,b,c))