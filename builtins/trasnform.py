'''
Given a sentence in which words are separated by spaces.

Re-arrange it so that words are reordered according to the following criteria.
 - longer words come before shorter words
 - if two words have same length, the one with smaller vowel occurance count comes first (feeel counts as 3 vowel occurances)
 - if even that is same, preserve the original order.

Constraints:
- Only allowed characters are a-zA-Z in the words
- raise a ValueError if the sentence contains any characters beyond the above
- raise a TypeError if input is not a string
- The result should preserve the words as is without changing case etc. but the sentence should be sorted so that
longer words precede shorter words. In case of tie, the word with fewer vowels comes first, if there is a tie even there,
preserve the original order.
- If there are multiple spaces, merge them into a single space in the result.
- If there is any leading or trailing space, remove it from the result.

Note: use the features of python to solve this problem, DON'T WRITE YOUR OWN SORT ROUTINE!
'''

def count_vowels(s):
    v='aeiouAEIOU'
    count=0
    for i in s:
        if i in v:
            count+=1
    return count
def transform(sentence):
    sentence=sentence.split()
    sentence=sorted(sentence,key=count_vowels)
    sentence=sorted(sentence,key=lambda a:len(a),reverse=True)

    return ' '.join(sentence)



def test_transform():
    assert "elephant walking runway down seen was the An" == transform("An elephant was seen walking down the runway")