__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
A chain of words is defined as a sequence of words w1, w2, .. wn where each of the words is formed by removing exactly
one letter from the previous word. Each of the words w2, ... wn need to valid words as given in the dictionary file 
(final_words.txt)

For e.g. once -> one -> on is valid chain start with once.    

Your job for this problem is to write a routine that given a word returns the longest chain of words starting with 
a given word. [valid words are words in the given file - final_words.txt ].  

If multiple chains are possible, pick the one that has words which are earlier in the alphabet ordering.

For e.g meat -> met -> me and meat -> eat -> at are valid longest chains of length 3 starting with meat. 
If these are the only 2 longest chains return [meat, eat, at] as eat comes before met in the alphabet ordering.

Notes:
1. Raise TypeError if word is not a string
2. Return a list of words including the original word (all in smaller case even if original is mixed case)
3. If the word has no chains just return the word in the list (chain of length 1).
4. Use the open_input_file helper routine given to open the file. The current directory will not be your folder 
   and you will not find the file if you do not do this.
5. Do not read the file multiple times in your implementation (once per invocation is fine, though in general if 
you write this as a cli tool, you will load once and run the queries multiple times)!
6. DO NOT SUBMIT the words file, we will add it at our end.
'''

import os
import inspect

# helper routines...
def get_module_dir():
    mod_file = inspect.getfile(inspect.currentframe())
    mod_dir = os.path.dirname(mod_file)
    return mod_dir


def open_input_file(file, mode="rt"):
    mod_dir = get_module_dir()
    test_file = os.path.join(mod_dir, file)
    return open(test_file, mode)

def get_chain(file,main_list,current):
    last=current[-1]
    flag=0
    for i in range(len(last)):
        temp=last[:i]+last[i+1:]
        if temp in file:

            flag+=1
            get_chain(file,main_list,current+[temp])
    if flag==0:
        main_list.append(current)


# Important USE the open_input_file routine given above to open the "final_words.txt".
def get_longest_chain(word):

    if not isinstance(word,str):
        raise TypeError

    f=open_input_file('final_words.txt')
    words=f.readlines()
    word=word.lower()
    words=list(map(str.strip,words))
    main_list=[]
    current=[]
    current.append(word)
    get_chain(words,main_list,current)

    main_list=sorted(main_list,key=lambda a: ''.join(a))
    main_list=sorted(main_list,key=len)

    return main_list[0]



def test_get_longest_chain():

    assert ["small", "mall", "all"]== get_longest_chain("small")
    assert ['meat', 'eat', 'at'] == get_longest_chain("meat")
    assert ['once', 'one', 'ne'] == get_longest_chain("once")
    assert ['doctors', 'doctor'] == get_longest_chain("doctors")
    assert ['domestics', 'domestic'] == get_longest_chain("domestics")
    assert ['climber', 'limber'] == get_longest_chain("climber")
    assert ['ashamed', 'shamed', 'shame', 'same', 'sam', 'am'] == get_longest_chain("ashamed")
    assert ['ambulances', 'ambulance'] == get_longest_chain("ambulances")
    assert ['asians', 'asian', 'asia'] == get_longest_chain("asians")
    assert ['once', 'one', 'ne'] == get_longest_chain("once")
    assert ["small", "mall", "all"] == get_longest_chain("small")
    try:
        get_longest_chain(1)
    except TypeError:
        pass
