__author__ = 'Kalyan'

max_marks = 30

problem_notes ='''
This is same as the problem in mock1 with additional constraints on implementation.

This problem deals with a custom encryption/decryption scheme that works as follows. 

Given a string like "how are you?" and m * n grid. The characters of the string are filled 
into the grid row wise top to bottom. So for 3 * 5 you get

h o w _ a
r e _ y o
u ? * * *

In the above example _ is shown visually where there is a space character. Unfilled cells are filled with *'s

The encrypted string is found by starting at a specified corner and going clockwise in 
a decreasing spiral till all the cells are covered. So if corner is top right you get "ao***?urhow y e"

I want you to code this as a decomposition given below. Each of the routines will be independently tested 
and scored. 

You are free to define any additional helper routines that you want.

Notes:
1. raise TypeError if text is not a str or key is not EncryptKey
2. raise ValueError if the grid cannot accomodate the text  or if rows/cols are <= 0 
3. returns the encrypted string as specified above.
4. see the definitions for Corner and EncryptKey in mock2common.py
'''

from mock2common import EncryptKey, Corner

#returns the m x n grid of chars as a list of lists (each row is a list) with the characters as specified in the example.
def get_grid(text, key):
    if not isinstance(text, str) or not isinstance(key, EncryptKey):
        raise TypeError

    if key.rows <= 0 or key.cols <= 0 or len(text) > key.rows*key.cols:
        raise ValueError
    if len(text) < key.rows*key.cols:
        text += '*' * (key.rows*key.cols-len(text))
    return [list(text[key.cols*i:key.cols*(i+1)]) for i in range(key.rows)]

# define this as a generator function that successively returns the cells as (x,y) coordinates in the traversal
# specified by the key
def get_path(key):
    if  not isinstance(key, EncryptKey):
        raise TypeError

    if key.rows <= 0 or key.cols <= 0:
        raise ValueError

    matrix= [[(j,i) for i in range(key.cols)] for j in range(key.rows)]

    if key.corner == Corner.BOTTOM_LEFT:
        matrix = list(zip(*matrix[::-1]))

    if key.corner == Corner.BOTTOM_RIGHT:
        matrix = matrix[::-1]
        for i in range(key.rows):
            matrix[i] = matrix[i][::-1]

    if key.corner == Corner.TOP_RIGHT:
        matrix = list(zip(*matrix))[::-1]

    path=[]

    while matrix:
        path += matrix[0]
        matrix = list(zip(*matrix[1:]))[::-1]
    for i in path:
        yield i


# calls the helper routines get_grid and get_path and gets the encryption done.
def encrypt(text, key):
    if not isinstance(text, str) or not isinstance(key, EncryptKey):
        raise TypeError

    if key.rows <= 0 or key.cols <= 0 or len(text) > key.rows*key.cols:
        raise ValueError

    matrix=get_grid(text,key)
    path=get_path(key)
    result=''
    for coord in path:
        result+= matrix[coord[0]][coord[1]]

    return result

# basic tests are given, write your own tests based on constraints.
def test_get_grid():
    assert [['h', 'o', 'w', '*', '*']] == get_grid("how", EncryptKey(1, 5, Corner.TOP_RIGHT))

def test_get_path():
    assert 'generator' == type(get_path(EncryptKey(1, 5, Corner.TOP_RIGHT))).__name__
    assert [(0,4), (0,3), (0,2), (0,1), (0,0)] == list(get_path(EncryptKey(1, 5, Corner.TOP_RIGHT)))

def test_encrypt():
    assert "how ao***?ure y" == encrypt("how are you?", EncryptKey(3, 5, Corner.TOP_LEFT))
    assert "ao***?urhow y e" == encrypt("how are you?", EncryptKey(3, 5, Corner.TOP_RIGHT))
    assert "urhow ao***?e y" == encrypt("how are you?", EncryptKey(3, 5, Corner.BOTTOM_LEFT))
    assert "***?urhow aoy e" == encrypt("how are you?", EncryptKey(3, 5, Corner.BOTTOM_RIGHT))

    assert "**woh" == encrypt("how", EncryptKey(1, 5, Corner.TOP_RIGHT))
