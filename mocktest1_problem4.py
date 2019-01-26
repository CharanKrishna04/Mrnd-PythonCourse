__author__ = 'Kalyan'

max_marks = 20

notes = '''
This is the counterpart to the encrypt routine that you wrote in problem 3. 

You are given the encrypted string, the original key used to encrypt the original string.

Your job is to reconstruct the original string.

Notes:
1. raise TypeError if text is not a str or key is not EncryptKey
2. raise ValueError if the grid is invalid (ie) cannot accomodate the text  or if rows/cols are <= 0 
3. returns the original string (remove the padding chars).
4. You can assume that the original string does not contain the padding chars
5. see the definitions for Corner and EncryptKey in mock1common.py

'''

from mock1common import EncryptKey, Corner

def fill_matrix(text,key):
    if key.corner==Corner.BOTTOM_RIGHT or key.corner==Corner.TOP_LEFT:
        matrix=[[None]*key.cols for i in range(key.rows)]
        r=key.rows
        c=key.cols
    else:
        matrix=[[None]*key.rows for i in range(key.cols)]
        r=key.cols
        c=key.rows

    dx,dy=0,1
    x,y=0,0

    for i in text:
        matrix[x][y]=i
        nx,ny= x+dx, y+dy
        if 0<=nx<r and 0<=ny<c and matrix[nx][ny]==None:
            x,y=nx,ny
        else:
            dx,dy=dy,-dx
            x,y=x+dx, y+dy

    return matrix


def decrypt(encrypted_text, key):


    matrix=fill_matrix(encrypted_text,key)

    if key.corner==Corner.BOTTOM_LEFT:
        matrix=list(zip(*matrix))[::-1]

    if key.corner==Corner.BOTTOM_RIGHT:
        for i in range(key.rows):
            matrix[i]=matrix[i][::-1]
        matrix=matrix[::-1]

    if key.corner==Corner.TOP_RIGHT:
        matrix=list(zip(*matrix[::-1]))

    path=''
    for i in range(key.rows):
        path+=''.join(matrix[i])

    path=path.replace('*','')
    return  path



# a basic test is given, write your own tests based on constraints.
def test_decrypt():
    assert "how are you?" == decrypt("ao***?urhow y e", EncryptKey(3, 5, Corner.TOP_RIGHT))
    assert "how are you?" == decrypt("how ao***?ure y", EncryptKey(3, 5, Corner.TOP_LEFT))
    assert "how are you?" == decrypt("urhow ao***?e y", EncryptKey(3, 5, Corner.BOTTOM_LEFT))
    assert "how are you?" == decrypt("***?urhow aoy e", EncryptKey(3, 5, Corner.BOTTOM_RIGHT))
