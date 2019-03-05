import random

def EmptyBoard():
    emptyboard = [0]*64
    return emptyboard

def GenBoard():
    x = EmptyBoard()
    white = 10
    black = 20
    pawn = 0
    knight = 1
    bishop = 2
    rook = 3
    queen = 4
    king = 5
    for i in range(8, 16, 1):
        x[i] = white+pawn
    for i in range(48, 56, 1):
        x[i] = black+pawn
    x[0:8] = [white+rook, white+knight, white+bishop, white+king, white+queen, white+bishop, white+knight, white+rook]
    x[56:] = [black+rook, black+knight, black+bishop, black+king, black+queen, black+bishop, black+knight, black+rook]
    return x

def PrintBoard(x):
    print("----------------WHITE----------------")
    space = ' '
    a = 0
    b = 0
    while b < 8:
        while True:
            if x[a] > 9:
                print(str(x[a])+3*space, end = '')
            else:
                print(str(x[a])+4*space, end = '')
            a=a+1
            if a%8 == 0:
                break
        print("")
        b = b+1
    print("----------------BLACK----------------")
    return True

def GetPlayerPositions(board, player):
    accum = []
    for i in range(0, len(board), 1):
        if (-1+player) < board[i] < (6+player):
            accum = accum + [i]
    return accum

def GetPieceLegalMoves(board, position):
    if 9 < board[position] < 16:
        player = 10
    elif 19 < board[position] < 26:
        player = 20

    if board[position] == 10 or board[position] == 20:
        return GetPawnLegalMoves(board, position, player)
    elif board[position] == 11 or board[position] == 21:
        return GetKnightLegalMoves(board, position, player)
    elif board[position] == 12 or board[position] == 22:
        return GetBishopLegalMoves(board, position, player)
    elif board[position] == 13 or board[position] == 23:
        return GetRookLegalMoves(board, position, player)
    elif board[position] == 14 or board[position] == 24:
        return GetQueenLegalMoves(board, position, player)
    elif board[position] == 15 or board[position] == 25:
        return GetKingLegalMoves(board, position, player)
    else:
        return [-1, 'There is no piece here']

def GetPawnLegalMoves(board, position, player):
    accum = []
    if player == 10:
        if (position+9) < 64:
            if board[position+8] == 0:
                accum = accum + [position+8]
            if board[position] % 8 == 0 and (29-player) < board[position+9] < (36-player):
                accum = accum + [position+9]
            if board[position] % 8 == 7 and (29-player) < board[position+7] < (36-player):
                accum = accum + [position+7]
            else:
                if (29-player) < board[position+7] < (36-player):
                    accum = accum + [position+7]
                if (29-player) < board[position+9] < (36-player):
                    accum = accum + [position+9]
        return accum
    if player == 20:
        if (position-9) < 0:
            if board[position-8] == 0:
                accum = accum + [position-8]
            if board[position] % 8 == 0 and (29-player) < board[position-7] < (36-player):
                accum = accum + [position-7]
            if board[position] % 8 == 7 and (29-player) < board[position-9] < (36-player):
                accum = accum + [position-9]
            else:
                if (29-player) < board[position-7] < (36-player):
                    accum = accum + [position-7]
                if (29-player) < board[position-9] < (36-player):
                    accum = accum + [position-9]
        return accum

def GetKnightLegalMoves(board, position, player):
    if board[position] != 11 and board[position] != 21:
        return -1
    accum = []
    # corners
    if position == 0:
        for i in [10, 17]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    elif position == 7:
        for i in [6, 15]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    elif position == 56:
        for i in [-6, -15]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    elif position == 63:
        for i in [-10, -17]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    # one in from corners (up/down direction)
    elif position == 8:
        for i in [10, 17, -6]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    elif position == 15:
        for i in [6, 15, -10]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    elif position == 48:
        for i in [-6, -15, 10]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    elif position == 55:
        for i in [-10, -17, 6]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    # one in from corners (right/left direction)
    elif position == 1:
        for i in [10, 17, 15]:
            if not (19-player) < board[position+i] < (26-player):
                accum = accum + [position+i]
    elif position == 6:
        for i in [6, 15, 17]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    elif position == 57:
        for i in [-6, -15, -17]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    elif position == 62:
        for i in [-10, -17, -15]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    # one in from corners (diaganol direction)
    elif position == 9:
        for i in [10, 17, -6, 15]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    elif position == 14:
        for i in [6, 15, -10, 17]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    elif position == 49:
        for i in [-6, -15, 10, -17]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    elif position == 54:
        for i in [-10, -17, 6, -15]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    # 4 middle top row
    elif 1 < position < 6:
        for i in [6, 10, 15, 17]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    # 4 middle left row
    elif 15 < position < 41 and position%8 == 0:
        for i in [-6, 10, -15, 17]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    # 4 middle right column
    elif 22 < position < 48 and position%8 == 7:
        for i in [6, -10, 15, -17]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    # 4 middle bottom row
    elif 57 < position < 62:
        for i in [-6, -10, -15, -17]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    # 4 middle second row
    elif 9 < position < 14:
        for i in [-10, -6, 6, 10, 15, 17]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    # 4 middle second column row
    elif 15 < position < 42 and position%8 == 1:
        for i in [-17, 15, -6, 10, -15, 17]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    # 4 middle seventh column
    elif 21 < position < 48 and position%8 == 6:
        for i in [-15, -17, 6, -10, 15, -17]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    # 4 middle seventh row
    elif 49 < position < 54:
        for i in [6, 10, -6, -10, -15, -17]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    # middle 16 squares
    else:
        for i in [-6, 6, -10, 10, -15, 15, -17, 17]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    return accum

def GetBishopLegalMoves(board, position, player):
    accum = []
    # up-left
    up_left_cnt = -9
    while True:
        if 0 <= position <= 7 or position%8 == 0:
            break
        elif 0 <= position + up_left_cnt <= 7 or (position + up_left_cnt) % 8 == 7:
            if not (-1+player) < board[position+up_left_cnt] < (6+player):
                accum = accum + [position+up_left_cnt]
            break
        elif board[position+up_left_cnt] == 0:
            accum = accum + [position+up_left_cnt]
            up_left_cnt = up_left_cnt - 9
        elif (29-player) < board[position+up_left_cnt] < (36-player):
            accum = accum + [position+up_left_cnt]
            break
        elif (-1+player) < board[position+up_left_cnt] < (6+player):
            break
    # up-right
    up_right_cnt = -7
    while True:
        if 0 <= position <= 7 or position % 8 == 7:
            break
        elif 0 <= position + up_right_cnt <= 7 or (position + up_right_cnt) % 8 == 0:
            if not (-1+player) < board[position+up_right_cnt] < (6+player):
                accum = accum + [position+up_right_cnt]
            break
        elif board[position + up_right_cnt] == 0:
            accum = accum + [position + up_right_cnt]
            up_right_cnt = up_right_cnt - 7
        elif (29-player) < board[position + up_right_cnt] < (36-player):
            accum = accum + [position + up_right_cnt]
            break
        elif (-1+player) < board[position+up_right_cnt] < (6+player):
            break
    # down-left
    down_left_cnt = 7
    while True:
        if 56 <= position <= 63 or position % 8 == 0:
            break
        elif 56 <= position + down_left_cnt <= 63 or (position + down_left_cnt) % 8 == 7:
            if not (-1+player) < board[position+down_left_cnt] < (6+player):
                accum = accum + [position+down_left_cnt]
            break
        elif board[position + down_left_cnt] == 0:
            accum = accum + [position + down_left_cnt]
            down_left_cnt = down_left_cnt + 7
        elif (29-player) < board[position + down_left_cnt] < (36-player):
            accum = accum + [position + down_left_cnt]
            break
        elif (-1+player) < board[position + down_left_cnt] < (6+player):
            break
    # down_right
    down_right_cnt = 9
    while True:
        if 56 <= position <= 63 or position % 8 == 7:
            break
        elif 56 <= position + down_right_cnt <= 63 or (position + down_right_cnt) % 8 == 0:
            if not (-1+player) < board[position] < (6+player):
                accum = accum + [position+down_right_cnt]
            break
        elif board[position + down_right_cnt] == 0:
            accum = accum + [position + down_right_cnt]
            down_right_cnt = down_right_cnt + 9
        elif (29-player) < board[position + down_right_cnt] < (36-player):
            accum = accum + [position + down_right_cnt]
            break
        elif(-1+player) < board[position+down_right_cnt] < (6+player):
            break
    return accum

def GetRookLegalMoves(board, position, player):
    # leftwards
    accum = []
    left_cnt = -1
    while True:
        if position % 8 == 0:
            break
        elif (position + left_cnt) % 8 == 7:
            break
        elif board[position + left_cnt] == 0:
            accum = accum + [position + left_cnt]
            left_cnt = left_cnt - 1
        elif (29 - player) < board[position + left_cnt] < (36 - player):
            accum = accum + [position + left_cnt]
            break
        elif (-1 + player) < board[position + left_cnt] < (6 + player):
            break
    # rightwards
    right_cnt = 1
    while True:
        if position % 8 == 7:
            break
        elif (position + right_cnt) % 8 == 0:
            break
        elif board[position + right_cnt] == 0:
            accum = accum + [position + right_cnt]
            right_cnt = right_cnt + 1
        elif (29 - player) < board[position + right_cnt] < (36 - player):
            accum = accum + [position + right_cnt]
            break
        elif (-1 + player) < board[position + right_cnt] < (6 + player):
            break
    # upwards
    up_cnt = -8
    while True:
        if 0 <= position <= 7:
            break
        elif 0 <= position + up_cnt <= 7:
            if not (-1+player) < board[position+up_cnt] < (6+player):
                accum = accum + [position+up_cnt]
            break
        elif board[position + up_cnt] == 0:
            accum = accum + [position + up_cnt]
            up_cnt = up_cnt - 8
        elif (29 - player) < board[position + up_cnt] < (36 - player):
            accum = accum + [position + up_cnt]
            break
        elif (-1 + player) < board[position + up_cnt] < (6 + player):
            break
    # downwards
    down_cnt = 8
    while True:
        if 56 <= position <= 63:
            break
        elif 56 <= position + down_cnt <= 63:
            if not (-1+player) < board[position+down_cnt] < (6+player):
                accum = accum + [position+down_cnt]
            break
        elif board[position + down_cnt] == 0:
            accum = accum + [position + down_cnt]
            down_cnt = down_cnt + 8
        elif (29 - player) < board[position + down_cnt] < (36 - player):
            accum = accum + [position + down_cnt]
            break
        elif (-1 + player) < board[position + down_cnt] < (6 + player):
            break
    return accum

def GetQueenLegalMoves(board, position, player):
    return GetRookLegalMoves(board, position, player)+GetBishopLegalMoves(board, position, player)

def GetKingLegalMoves(board, position, player):
    if board[position] != 15 and board[position] != 25:
        return -1
    accum = []
    # top-left corner case
    if position == 0:
        for i in [1, 8, 9]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    # top-right corner case
    elif position == 7:
        for i in [-1, 8, 9]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    # bottom-left corner case
    elif position == 56:
        for i in [1, -7, -8]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    # bottom-right corner case
    elif position == 63:
        for i in [-1, -8, -9]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    # left of board case
    elif 1 < position < 55 and position%8 == 0:
        for i in [-8, -7, 1, 8, 9]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    # top of board case
    elif 0 < position < 7:
        for i in [-1, 1, 7, 8, 9]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    # right of board case
    elif 7 < position < 63 and position%8 == 7:
        for i in [-8, -9, 7, 8, 1]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    # bottom of board case
    elif 56 < position < 63:
        for i in [-1, 1, -7, -8, -9]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position+i]
    else:
        for i in [-9, -8, -7, -1, 1, 7, 8, 9]:
            if not (-1+player) < board[position+i] < (6+player):
                accum = accum + [position + i]
    return accum

def IsPositionUnderThreat(board, position, player):
    accum = []
    for i in range(0, len(board), 1):
        if (29-player) < board[i] < (36-player):
            accum = accum + GetPieceLegalMoves(board, i)
    for i in accum:
        if i == position:
            return True
        else:
            return False

def white_player_moves(x):
    # white player moves
    PrintBoard(x)
    pieceW = int(input("White player - which piece would you like to move?\n"))
    moveW = int(input("Where would you like to move it?\n"))
    a = GetPieceLegalMoves(x, pieceW)
    acc = []
    for i in a:
        if moveW == i:
            acc = acc + [i]
            x[moveW] = x[pieceW]
            x[pieceW] = 0
            break
    if acc == []:
        print("Invalid move! Choose again!")
        return white_player_moves(x)

def black_player_moves(x):
    # black player moves
    moves = random.choice(move_generator(x, 20))
    pieceB = moves[0]
    moveB = moves[1][0]
    x[moveB] = x[pieceB]
    x[pieceB] = 0

def move_generator(board, player):
    accum = []
    L = GetPlayerPositions(board, player)
    for i in L:
        j = GetPieceLegalMoves(board, i)
        for h in j:
            k = IsPositionUnderThreat(board, h, player)
            if not k:
                accum = accum + [[i, [h, k]]]
    return accum

def gen_candidateMoves(board, player):
    candidateMoves = []
    m = move_generator(board, player)
    for i in m:
        cm = [[i[0], i[1][0]], 0]
        score = 0.0
        if board[i[1][0]] != 0:
            score = score + float(board[i[1][0]])
        score = score + GetPieceScore(board, i[1][0], player) - GetPieceScore(board, i[0], player)
        cm[1] = score
        candidateMoves = candidateMoves + [cm]
    for i in range(0, len(candidateMoves), 1):
        score = GenMoveScore(board, candidateMoves[i][0][0], candidateMoves[i][0][1], candidateMoves, player)
        candidateMoves[i][1] = candidateMoves[i][1] + score
    return candidateMoves

def make_move(board, fro, to):
    board[to] = board[fro]
    board[fro] = 0
    return True

def GetPieceScore(board, position, player):

    pawnW = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, \
        0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5, \
        0.5, 0.5, -1.0, 0.0, 0.0, -1.0, 0.5, 0.5, \
        0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0, \
        0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5, \
        1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0, \
        5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, \
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    knightW = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, \
        0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5, \
        0.5, 0.5, -1.0, 0.0, 0.0, -1.0, 0.5, 0.5, \
        0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0, \
        0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5, \
        1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0, \
        5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, \
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    bishopW = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, \
        0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5, \
        0.5, 0.5, -1.0, 0.0, 0.0, -1.0, 0.5, 0.5, \
        0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0, \
        0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5, \
        1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0, \
        5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, \
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    rookW = [0.0]*3 + [0.5]*2 + [0.0]*3 + [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5]*6 + [0.5] + [1.0]*6 +[0.5] + [0.0]*8
    queenW = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, \
        0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5, \
        0.5, 0.5, -1.0, 0.0, 0.0, -1.0, 0.5, 0.5, \
        0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0, \
        0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5, \
        1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0, \
        5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, \
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    kingW = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, \
        0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5, \
        0.5, 0.5, -1.0, 0.0, 0.0, -1.0, 0.5, 0.5, \
        0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0, \
        0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5, \
        1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0, \
        5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, \
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    if player == 10:
        if board[position] == 10:
            return pawnW[position]
        elif board[position] == 11:
            return knightW[position]
        elif board[position] == 12:
            return bishopW[position]
        elif board[position] == 13:
            return rookW[position]
        elif board[position] == 14:
            return queenW[position]
        elif board[position] == 15:
            return kingW[position]
        else:
            return 0

    if player == 20:
        pawnB = pawnW[::-1]
        knightB = knightW[::-1]
        bishopB = bishopW[::-1]
        rookB = rookW[::-1]
        queenB = queenW[::-1]
        kingB = kingW[::-1]

        if board[position] == 20:
            return pawnB[position]
        elif board[position] == 21:
            return knightB[position]
        elif board[position] == 22:
            return bishopB[position]
        elif board[position] == 23:
            return rookB[position]
        elif board[position] == 24:
            return queenB[position]
        elif board[position] == 25:
            return kingB[position]
        else:
            return 0

def GenMoveScore(board, pos1, pos2, candidateMoves, player):
        score = 0.0
        for i in range(0, len(candidateMoves), 1):
            if board[candidateMoves[i][0][1]] != 0:
                score = score + float(4.0*(board[candidateMoves[i][0][1]])*(board[candidateMoves[i][0][1]]))
                if board[candidateMoves[i][0][1]] == 15 or board[candidateMoves[i][0][1]] == 25:
                    score = score + 20000
                if board[candidateMoves[i][0][1]] == 14 or board[candidateMoves[i][0][1]] == 22:
                    score = score + 200
                if board[candidateMoves[i][0][1]] == 13 or board[candidateMoves[i][0][1]] == 23:
                    score = score + 20
                if board[candidateMoves[i][0][1]] == 12 or board[candidateMoves[i][0][1]] == 22:
                    score = score + 2
                if board[candidateMoves[i][0][1]] == 11 or board[candidateMoves[i][0][1]] == 21:
                    score = score - 2
        score = score + GetPieceScore(board, pos2, player) - GetPieceScore(board, pos1, player)
        return score

def gen_evalTree(board, player):
    if player == 10:
        opp_player = 20
    elif player == 20:
        opp_player = 10
    cm = gen_candidateMoves(board, player)
    for i in range(0, len(cm)):
        copy = list(board)
        make_move(copy, cm[i][0][0], cm[i][0][1])
        c = gen_candidateMoves(copy, opp_player)
        cm[i] = cm[i] + [c]
    return cm

def minimax(node, depth, maxp):

    if depth == 0:
        return node

    if maxp:
        value = -10000
        for i in node:
            value = max(value, minimax(i[2], depth-1, False))
        return value
    else:
        value = 10000
        for i in node:
            move = []
            value = min(value, minimax(i[1], depth-1, True))
        return value

def ChooseMove(evalTree, y):
    accum = []
    for i in evalTree:
        for j in i[2]:
            if y == j[1]:
                accum = accum + [i[0]]
    if accum == []:
        for q in evalTree:
            accum = accum + [q[0]]
    move = random.choice(accum)
    return move

def chessPlayer(board, player):
    candidateMoves = gen_candidateMoves(board, player)
    evalTree = gen_evalTree(board, player)
    scoreval = minimax(evalTree, 2, player)
    move = ChooseMove(evalTree, scoreval)
    status = True
    return [status, move, candidateMoves, evalTree]