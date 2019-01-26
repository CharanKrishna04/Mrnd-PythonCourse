__author__ = 'Kalyan'

max_marks = 20

problem_notes = '''
 This problem deals with number conversion from a custom base 36 notation.

 In this notation, the digits 0 to 9 and letters a to z and  are to represent 0 to 35. 
 E.g. decimal 10 in this notation will be "a", 15 will be "f", 35 will be "z". "10" will represent 36.
  
 The notation in case insensitive so even "Z" is a valid representation for 35.

 Your job is to write a decoding routine for this notation.

 Note: 
 
 1. make good use of python features and avoid huge if else statement flow!
 2. read additional constraints on the function comments below.
 3. add any standard imports that you need.
'''

# Notes:
# - if s is not a string, raise TypeError
# - if the encoding is not right or empty string, raise ValueError
# - allow both - and + as prefixes which represent sign.
# - allow trailing and starting spaces (but not once the sign or number starts)
# - allow both capital and small letters.
# - return a int or long that corresponds to the number.

import re
from string import digits,ascii_lowercase


def from_custom_base36(s):



    if isinstance(s,str)==False:
        raise TypeError
    regex = r"^ *[+-]?[a-zA-Z0-9]+ *$"
    if not bool(re.match(regex,s)):
        raise ValueError

    conv = dict(zip(digits+ascii_lowercase,range(36)))
    s=s.lower()
    res=0
    l=len(s)-1
    for i in s:
        res=res + (36**l)*conv[i]
        l-=1
    return res




# a basic test is given, write your own tests based on constraints.
def test_from_custom_base36():

    assert 72 == from_custom_base36("20")
    assert 35 == from_custom_base36('Z')