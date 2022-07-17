"""
Question3
Write a function that creates a dictionary with each (key, value) pair being the (lower case,
upper case) versions of a letter, respectively.
Examples
mapping(["p", "s"]) ➞ { "p": "P", "s": "S" }
mapping(["a", "b", "c"]) ➞ { "a": "A", "b": "B", "c": "C" }
mapping(["a", "v", "y", "z"]) ➞ { "a": "A", "v": "V", "y": "Y", "z": "Z" }
Notes
All of the letters in the input list will always be lowercase.
"""

def mapping(l):
    l = str_list(l)
    d = {}
    for i in l:
        d[i] =chr(ord(i)-32)
    return d

def str_list(s):
    return s.split(',')

s = input("Enter list in comma seperated sequence \nEg. 1,2,3 :")
d = mapping(s)
print("mapping(",str_list(s),") ➞",d)