'''
    print all anagrams formed by all dictionary words.
    Import all the words from lowercase.txt and return anagram that occured maximum times

'''

from collections import defaultdict

def read_words():
    with open('lowercase.txt') as ip:
        lines=ip.readlines()
        return map(str.strip,lines)


def get_anagrams(words):
    d=defaultdict(list)
    for w in words:
        key=''.join(sorted(w.lower()))
        d[key].append(w)
    return d

def anagrams():
    words=read_words()
    anagram_list=list(get_anagrams(words).values())
    return max(anagram_list,key=len)



def test_anagrams():
    print(anagrams())



