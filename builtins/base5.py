'''
 This problem deals with number conversion into a custom base 5 notation and back.
 In this notation, the letters a to e are used for digits 0 to 4.

 E.g. decimal 10 in this custom base 5 notation is "ca", decimal 5 is "ba" etc.

 Your job is to write encoding and decoding (both) routines to deal with this notation.
'''

# Notes:
# - If number is not a valid int or long raise TypeError
# - Negative numbers should result in a - prefix to the result similar to how bin works
#  use lower case letters in your result [a to e].
def to_custom_base5(number):
    if isinstance(number,str):
        raise TypeError
    
    res=''
    conv='abcde'
    while number:
        res=conv[number%5]+res
        number=number//5
    return res

# Notes:
# - if s is not a string, raise TypeError
# - if the encoding is not right or empty string, raise ValueError
# - allow both - and + as prefixes which represent sign.
# - allow trailing and starting spaces (but not once the sign or number starts)
# - allow both capital and small letters.
# - return a int or long that corresponds to the number.
def from_custom_base5(s):
    l=len(s)
    res=0
    for i in s:
        l=l-1
        n=ord(i)-ord('a')
        res+= n*(5**l)


    return res

# a basic test is given, write your own tests based on constraints.
def test_to_custom_base5():
    assert "ca" == to_custom_base5(10)

# a basic test is given, write your own tests based on constraints.
def test_from_custom_base5():
    assert 10 == from_custom_base5("ca")