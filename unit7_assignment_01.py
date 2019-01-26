__author__ = 'Kalyan'

problem = """
 We are going to revisit unit6 assignment3 for this problem.

 Given an input file of words (mixed case). Group those words into anagram groups and write them
 into the destination file so that words in larger anagram groups come before words in smaller anagram sets.

 With in an anagram group, order them in case insensitive ascending sorting order.

 If 2 anagram groups have same count, then set with smaller starting word comes first.

 For e.g. if source contains (ant, Tan, cat, TAC, Act, bat, Tab), the anagram groups are (ant, Tan), (bat, Tab)
 and (Act, cat, TAC) and destination should contain Act, cat, TAC, ant, Tan, bat, Tab (one word in each line).
 the (ant, Tan) set comes before (bat, Tab) as ant < bat.

 At first sight, this looks like a big problem, but you can decompose into smaller problems and crack each one.

 This program should be written as a command line script. It takes one argument the input file of words and outputs
 <input>-results.txt where <input>.txt is the input file of words.
"""
import sys


def lower_sort(inp):
    return str(inp).lower()
def are_anagrams(first, second):
    if(first==None or second==None):
        return False
    x=list(first.lower().replace(" ",""))
    x.sort()
    y=list(second.lower().replace(" ",""))
    y.sort()
    return x==y

def make_list(source):
    fin = open(source, 'rt')
    l = []
    for x in fin:
        y = x.lstrip()
        if y == '' or y[0] == '#':
            continue
        z = x.rstrip('\n')
        l.append(z)
    fin.close()
    return l

def group_anagrams(l):
    res=[]
    while len(l)>0:
        main_str=l.pop(0)
        sub=[]
        sub.append(main_str)
        i=0
        while i<len(l):
            if are_anagrams(main_str,l[i]):
                sub.append(l[i])
                l.pop(i)
            else:
                i+=1
        sub.sort(key=str.lower)
        res.append(sub)

    res.sort(key=lower_sort)
    res.sort(key=len,reverse=True)
    return res



def main(argv=sys.argv):

    l=make_list(argv[1])
    l=group_anagrams(l)
    fout = open(argv[1][:-4]+"-results.txt", 'wt')
    for i in l:
        fout.write('\n'.join(i)+'\n')
    fout.close()


if __name__ == "__main__":
    sys.exit(main())
'''
from collections import defaultdict


def AnagramsTogether(words):
    d = defaultdict()
    for item in words:
        s = "".join(sorted(item.lower()))
        if s not in d:
            d[s] = []
        d[s].append(item)
    return list(d.values())


def anagrams_sort(anagrams):
    for i in anagrams:
        i.sort(key=str.lower)
    anagrams.sort(key=lambda x: x[0].lower())
    anagrams.sort(key=len, reverse=True)
    return anagrams


def write_to_file(lines, dest):
    with open(dest, "wt") as op:
        for words in lines:
            for word in words:
                op.write(word + "\n")


def read_words(source):
    with open(source) as ip:
        words = []
        lines = ip.readlines()
        for i in lines:
            i = i.strip()
            if not (i == "" or i[0] == "#" ):
                words.append(i)
        return words


def main():
    words = read_words("random460k.txt")
    data = AnagramsTogether(words)
    sorted_data = anagrams_sort(data)
    write_to_file(sorted_data, "pp34_output.txt")


if __name__ == '__main__':
    exit(main())
'''