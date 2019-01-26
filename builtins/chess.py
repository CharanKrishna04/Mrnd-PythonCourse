'''
Standard chess rules apply - queens can move along a row or a column or a diagonal.
Given a placement of queens on a nxn board, the placement is considered safe no two queens can kill each other.

Input (board) is a list of queen column positions (ie) if board[i] = j. It means queen in ith column is placed
in jth row. For nxn chessboard, you have rows 0..n-1 and cols 0..n-1.

E.x. if board = [0, 1, 2] it is equivalent to following chessboard:

_ _ Q
_ Q _
Q _ _

Additional notes:

1. ValueError on none or empty list or if list input contains non integers
2. TypeError if board is not a list
3. Return False if board is not a valid placement (for e.g contains column as 5 for a 4x4 chessboard) or if
   2 queens can kill each other
4. Returns True if no 2 queens can kill each other.
'''
def safe_chessboard(board):
    sub=[]
    sum=[]
    for i in range(len(board)):
        if board[i]>=len(board) or board.count(board[i])>1:
            return False
        sub.append(board[i]-i)
        sum.append(board[i]+i)
    for i in range(len(board)):
        if sum.count(sum[i])>1 or sub.count(sub[i])>1:
            return False
    return True


#write your own tests
def test_safe_chessboard():
    assert False == safe_chessboard([0,1,2])
    assert False == safe_chessboard([2, 1, 0])
    assert False == safe_chessboard([0,3,1,2])
    assert True == safe_chessboard([1, 3, 0, 2])

