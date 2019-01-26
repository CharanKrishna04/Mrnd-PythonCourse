__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
A palindrome is a word which spells the same from both ends (case-insensitive).  

If a word is not a palindrome, you can make a palindrome out of it by adding letters to either ends of the word.

Your goal is to make a palindrome of the minimum length.

For e.g.  cat is not a palindrome, you can add letters at the ends to make palidromes like catac (ending), cattac (ending), 
taccat (beginning), tacat (beginning), acattaca (both ends). However, of all this the minimum length ones are catac and tacat.
  
Notes:

1. If word is not a str, raise TypeError
2. empty string is considered to be a palindrome.
3. if multiple palindromes of same length are possible, return the one earlier in alphabetical ordering (catac in 
   the example above, keep it case insensitive)
4. Only small letters should be added. The casing of original letters should be unchanged.
5. Write your own tests and test thoroughly.
'''

# returns the min length palidrome defined by the criteria given above.
def make_palindrome(word):
    if not isinstance(word,str):
        raise TypeError
    if word=='':
        return word

    main=word
    result=[]
    word = word.lower()
    l = 0
    ext = ''
    palin = word
    while palin != palin[::-1]:
        ext = word[l] + ext
        l += 1
        palin = word + ext
    result.append(main+ext)

    l=-1
    palin=word
    ext=''
    while palin != palin[::-1]:
        ext=ext+word[l]
        l-=1
        palin = ext+word
    result.append(ext+main)

    result.sort()
    result=sorted(result,key=len)
    return result[0]





def test_make_palindrome():
    #print(make_palindrome("cAT"))
    assert "cATac" == make_palindrome("cAT")
