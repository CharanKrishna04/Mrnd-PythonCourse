'''
Palindrome is a word which spells the same from both ends.

Create the smallest palindrome from a given word by appending characters to its end.

Examples:
- Malayalam -> Malayalam
- Malayal -> Malayalam (we want smallest palindrome)


Notes:
1. Don't change the letters of the initial word, only add new small letters
2. The palindrome is case-insensitive (ie) Tat is a valid palindrome
3. Only letters are allowed, any other characters should raise a ValueError
4. Non strings should raise a TypeError
5. Empty string is considered as a palindrome.
'''

import re
def smallest_palindrome(word):
    if not isinstance(word,str):
        raise TypeError
    if not bool(re.match(r"^[a-zA-Z]*$",word)):
        raise ValueError
    flag=0
    if word[0]>'A' and word[0]<'Z':
        flag=1

    word = word.lower()
    l = 0
    ext = ''
    palin = word
    while palin != palin[::-1]:
        ext = word[l] + ext
        l += 1
        palin = word + ext
    if flag==1:
        palin=palin.capitalize()
    return palin

# write your own tests
def test_smallest_palindrome():
    assert 'Malayalam' == smallest_palindrome('Malayal')
    print(smallest_palindrome('abcd'))
