"""
Question4
Write a function, that replaces all vowels in a string with a specified vowel.
Examples
vow_replace("apples and bananas", "u") ➞ "upplus und bununus"
vow_replace("cheese casserole", "o") ➞ "chooso cossorolo"
vow_replace("stuffed jalapeno poppers", "e") ➞ "steffed jelepene peppers"
Notes
All words will be lowercase. Y is not considered a vowel.
"""

def vow_replace(s,r):
    s1 = ''
    for i in s:
        if i in 'aeiou':
            s1 = s1 + r
        else:
            s1 = s1 + i
    return s1

s = input("Enter String ")
r = input("Enter char used to replace ")
s1 = vow_replace(s,r)
print("vow_replace(",s,',',r,") ➞",s1)