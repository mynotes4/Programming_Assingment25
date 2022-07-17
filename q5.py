"""
Question5
Create a function that takes a string as input and capitalizes a letter if its ASCII code is
even and returns its lower case version if its ASCII code is odd.
Examples
ascii_capitalize("to be or not to be!") ➞ "To Be oR NoT To Be!"
ascii_capitalize("THE LITTLE MERMAID") ➞ "THe LiTTLe meRmaiD"
ascii_capitalize("Oh what a beautiful morning.") ➞ "oH wHaT a BeauTiFuL moRNiNg."
"""

def ascii_capitalize(s):
    s1 = ""
    for i in s:
        if ord(i) % 2 == 0:
            s1 = s1 + i.upper()
        else:
            s1 = s1 + i.lower()
    return s1

s = input("Enter String ")
s1 = ascii_capitalize(s)
print("ascii_capitalize(",s,") ➞",s1)