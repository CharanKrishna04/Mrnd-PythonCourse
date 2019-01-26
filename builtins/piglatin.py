'''
Pig latin is an amusing game to conceal the meaning of a sentence.

Rules for converting a word to pig latin are as follows:

1. If word starts with a consonant, move all continuous consonants before the first vowel to the end and add  "ay" at the end.
e.g  happy becomes appyhay, trash becomes ashtray, dog becomes ogday etc.

2. If word starts with a vowel, you just add an ay. e.g. egg become eggay, eight becomes eightay etc.

Your job is to write a routine that will convert a given text to pig latin. e.g "There is, however, no need for fear."
should get converted to  "Erethay isay, oweverhay, onay eednay orfay earfay."  Note that punctuation and
capitalization has to be preserved

You can write helper sub routines to make your code easy to read and write.

Constraints: only punctuation allowed is , and . and they will come immediately after a word and
will be followed by a space if there is a next word. Acronyms are not allowed in sentences.
Some words may be capitalized (first letter is capital like "There" in the above example)
and you have to preserve its capitalization in the final word too (Erethay)

You can assume that only valid inputs as specified above will be given.
'''

def translate_to_pig_latin(word):
    punch=''
    trans=word
    if word[-1]==',' or word[-1]=='.':
        punch=word[-1]
        trans=word[:-1]

    vowels='aeiouAEIOU'
    while trans[0] not in vowels:
        trans=trans[1:]+trans[:1]
    trans+='ay'
    if word[0]>'A' and word[0]<'Z':
        trans=trans.capitalize()
    return trans+punch


def get_pig_latin(sentence):
    sentence=sentence.split()
    for i in range(len(sentence)):
        sentence[i]=translate_to_pig_latin(sentence[i])

    return ' '.join(sentence)

# write your own tests according to the constraints and notes given above.
def test_get_pig_latin():
        assert "onay earfay" == get_pig_latin("no fear")
        print(get_pig_latin("There is, however, no need for fear."))
        assert "Erethay isay, oweverhay, onay eednay orfay earfay." == get_pig_latin("There is, however, no need for fear.")



