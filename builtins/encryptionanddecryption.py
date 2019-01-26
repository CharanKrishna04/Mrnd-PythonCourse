'''
Write encryption and decryption routines according to the given scheme. 

A secret key is used to encrypt a text message in the following manner: 
- key is a string of letters in which each letter represents the right displacement of the source character (a -> 0, z-> 25)
- text -> input text to be sent 

Letters of the input text are mapped to the letters in the key in a round robin manner. For e.g:

For: key = "abcde", text="hi there", the mapping is 
h->a, i -> b, (space is ignored) t ->c, h -> d, e-> e, (go back to starting a here) r -> a, e->b 

now to get the encrypted text, you move h by 0, i by 1, t by 2, h by 3 etc. So you finally get the text "hj vkirf"

The decryption works in the reverse way and returns the original text.

Notes:
- Preserve the casing(lower case remains lower case, Upper case remains Upper case).
- Ignore non-letters and punctuations, i.e., leave them as is in the final result
- For displacement, both small and large letters represent the same displacement. For e.g. b and B both represent 1
- raise TypeError if text and key are not strings.
- raise ValueError if key is empty or has non alphabet characters

Write helper sub routines as required. Make good use of the available datatypes!
'''
import re
from string import ascii_lowercase,ascii_uppercase
# do type checking, non-str should raise TypeException
def encrypt(text, key):

    if not isinstance(text,str) or not isinstance(key,str):
        raise TypeError
    if key=='' or bool(re.match(r".*[^a-zA-Z].*",key)):
        raise ValueError
    res=''
    key=key.lower()
    t_index=0
    key_len=len(key)
    for i in text:
        if i==' ':
            res+=i
            continue
        if i  in ascii_uppercase:
            res+=ascii_uppercase[(ascii_uppercase.index(i)+ascii_uppercase.index(key[t_index]))%26]
            t_index=(t_index+1)%key_len
            continue
        if i in ascii_lowercase:
            res += ascii_lowercase[(ascii_lowercase.index(i) + ascii_lowercase.index(key[t_index])) % 26]
            t_index = (t_index + 1) % key_len
            continue
    return res



def decrypt(text, key):
    if not isinstance(text,str) or not isinstance(key,str):
        raise TypeError
    if key=='' or bool(re.match(r".*[^a-zA-Z].*",key)):
        raise ValueError
    res=''
    key=key.lower()
    t_index=0
    key_len=len(key)
    for i in text:
        if i==' ':
            res+=i
            continue
        if i  in ascii_uppercase:
            res+=ascii_uppercase[(ascii_uppercase.index(i)-ascii_uppercase.index(key[t_index]))%26]
            t_index=(t_index+1)%key_len
            continue
        if i in ascii_lowercase:
            res += ascii_lowercase[(ascii_lowercase.index(i) - ascii_lowercase.index(key[t_index])) % 26]
            t_index = (t_index + 1) % key_len
            continue
    return res



def test_encrypt():
    print(encrypt("hi there", "abcde"))
    assert "hj vkirf" == encrypt("hi there", "abcde")

def test_decrypt():
    assert "hi there" == decrypt("hj vkirf", "abcde")

