# https://www.codewars.com/kata/525caa5c1bf619d28c000335/train/python
def is_solved(board):
    if win(board): return win(board)
    for i in board:
        if 0 in i:
            return -1
    return 0
def win(board):
    for i in range(len(board)):
        for j in range(len(board)-1):
            if not (board[i][j]==board[i][j+1] and board[i][j]!=0): break
            if j+1==(len(board)-1): return board[i][j]
    for i in range(len(board)):
        for j in range(len(board)-1):
            if not (board[j][i]==board[j+1][i] and board[j][i]!=0): break
            if j+1==(len(board)-1): return board[j][i]
    for i in range(len(board)-1):
        if not (board[i][i]==board[i+1][i+1] and board[i][i]!=0): break
        if i+1==(len(board)-1): return board[i][i]
    if board[0][2]==board[1][1]==board[2][0] and board[0][2]!=0: return board[0][2]
    return 0