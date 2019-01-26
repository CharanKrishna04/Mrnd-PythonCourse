__author__ = 'Kalyan'

notes = '''
1. Read instructions for the function carefully and constraints carefully.
2. Try to generate all possible combinations of tests which exhaustively test the given constraints.
3. If behavior in certain cases is unclear, you can ask on the forums
'''
from placeholders import *

# Convert a sentence which has either or to only the first choice.
# e.g we could either go to a movie or a hotel -> we could go to a movie.
# note: do not use intermediate lists (string.split), only use string functions
# assume words are separated by a single space. you can use control flow statements
# So sentence is of form <blah> either <something> or <somethingelse> and gets converted to <blah> <something>
# if it is not of the correct form, you just return the original sentence.
def prune_either_or(sentence):
    if(sentence==None):
        return sentence
    if sentence.split()[0]=='either' or sentence.split()[-1]=='or' or 'either' not in sentence.split(" ") or 'or' not in sentence.split(" ") or ' either or ' in sentence:
        return sentence

    return " ".join(sentence.split(' either ')).split(' or ')[0]



def test_prune_either_or_student():
    assert "We can go to a movie" == prune_either_or("We can go either to a movie or to a hotel")
    assert "We can go either way" == prune_either_or("We can go either way")
    assert "either this or that" == prune_either_or("either this or that")
    assert "either way is fine" == prune_either_or("either way is fine")
    assert "It is neither here nor there" == prune_either_or("It is neither here nor there")
    assert "Two mythical cities either and oregon" == prune_either_or("Two mythical cities either and oregon")
    assert "Some random either or test" == prune_either_or("Some random either or test")
    assert '<blah> either <something> or '==prune_either_or('<blah> either <something> or ')
    assert None == prune_either_or(None)


# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_prune_either_or_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_prune_either_or(prune_either_or)
