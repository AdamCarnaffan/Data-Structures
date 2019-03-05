from random import *



def init():
    board=[]
    for i in range(0,64):
        board = board + [0]
    for i in range(0,8):
        board[8+i] = 10
        board[48+i] = 20
    board[0] = 13
    board[1] = 11
    board[2] = 12
    board[3] = 15
    board[4] = 14
    board[5] = 12
    board[6] = 11
    board[7] = 13
    board[56] = 23
    board[57] = 21
    board[58] = 22
    board[59] = 25
    board[60] = 24
    board[61] = 22
    board[62] = 21
    board[63] = 23
    return board


def PrintBoard(board):
    pboard=[]
    for i in range(0, 8):
        for j in range(0, 8):
            if j % 2 == 0 and i % 2 == 0:
                pboard = pboard + ["_"]
            elif j % 2 == 1 and i % 2 == 0:
                pboard = pboard + ["#"]
            elif j % 2 == 0 and i % 2 == 1:
                pboard = pboard + ["#"]
            elif j % 2 == 1 and i % 2 == 1:
                pboard = pboard + ["_"]
    for i in range(0,64):
        if board[i] == 10:
            pboard[i] = "p"
        elif board[i] == 11:
            pboard[i] = "n"
        elif board[i] == 12:
            pboard[i] = "b"
        elif board[i] == 13:
            pboard[i] = "r"
        elif board[i] == 14:
            pboard[i] = "q"
        elif board[i] == 15:
            pboard[i] = "k"
        elif board[i] == 20:
            pboard[i] = "P"
        elif board[i] == 21:
            pboard[i] = "N"
        elif board[i] == 22:
            pboard[i] = "B"
        elif board[i] == 23:
            pboard[i] = "R"
        elif board[i] == 24:
            pboard[i] = "Q"
        elif board[i] == 25:
            pboard[i] = "K"
    i = 7
    while i>=0:
        j=7
        while j>=0:
            print(pboard[i*8 + j], end = " ")
            j = j - 1
        print("      ", end = " ")
        k=7
        while k>=0:
            if (i*8 + k) >9:
                print((i*8 + k), end = " ")
            else:
                print(str(i * 8 + k) + " ", end=" ")
            k = k - 1
        print("")
        i = i -1
    pboard=[]

def IsOnBoard(pos):
   if (pos >= 0) and (pos <= 63):
      return True
   else:
      return False

def GetLegalMoves(board,pos):
    moves=[]
    if board[pos] == 10:
        if board[pos+8] == 0:
            moves=moves+[pos+8]
        if board[pos+7] != 0 and board[pos+7]>16:
            if pos % 8 != 0:
                moves = moves+[pos+7]
        if board[pos+9] != 0 and board[pos+9]>16:
            if (pos+1) % 8 != 0:
                moves = moves+[pos+9]
        return moves
    elif board[pos] == 20:
        if board[pos-8] == 0:
            moves=moves+[pos-8]
        if board[pos-7] != 0 and board[pos-7]<16:
            if (pos+1) % 8 == 0:
                board=board
            else :
                moves = moves+[pos-7]
        if board[pos-9] != 0 and board[pos-9]<16:
            if pos % 8 == 0:
                board=board
            else :
                moves = moves+[pos-9]
        return moves
    elif board[pos] == 13 or board[pos] == 23:
        nl = pos % 8
        nr = 7 - (pos % 8)
        nd = pos // 8
        nu = 7 - (pos // 8)
        accum = []
        # print nl,nr,nd,nu
        l = r = u = d = pos
        for i in range(0, nl, 1):
            l -= 1
            if IsOnBoard(l):
                if board[pos] > 20:
                    if board[l] < 20 and board[l] != 0:
                        accum += [l]
                        break
                    elif board[l] == 0:
                        accum += [l]
                elif board[pos] < 20:
                    if board[l] > 19 and board[l] != 0:
                        accum += [l]
                        break
                    elif board[l] == 0:
                        accum += [l]

        for i in range(0, nr, 1):
            r += 1
            if IsOnBoard(r):
                if board[pos] > 20:
                    if board[r] < 20 and board[r] != 0:
                        accum += [r]
                        break
                    elif board[r] == 0:
                        accum += [r]
                elif board[pos] < 20:
                    if board[r] > 19 and board[r] != 0:
                        accum += [r]
                        break
                    elif board[r] == 0:
                        accum += [r]

        for i in range(0, nd, 1):
            d -= 8
            if IsOnBoard(d):
                if board[pos] > 20:
                    if board[d] < 20 and board[d] != 0:
                        accum += [d]
                        break
                    elif board[d] == 0:
                        accum += [d]
                    elif board[d] > 19 and board[d] != 0:
                        break
                elif board[pos] < 20:
                    if board[d] > 19 and board[d] != 0:
                        accum += [d]
                        break
                    elif board[d] == 0:
                        accum += [d]
                    elif board[d] < 20 and board[d] != 0:
                        break
        for i in range(0, nu, 1):
            u += 8
            if IsOnBoard(u):
                if board[pos] > 20:
                    if board[u] < 20 and board[u] != 0:
                        accum += [u]
                        break
                    elif board[u] == 0:
                        accum += [u]
                    elif board[u] > 19 and board[u] != 0:
                        break
                elif board[pos] < 20:
                    if board[u] > 19 and board[u] != 0:
                        accum += [u]
                        break
                    elif board[u] == 0:
                        accum += [u]
                    elif board[u] < 20 and board[u] != 0:
                        break
        moves = list(accum)
    elif board[pos] == 12 or board[pos] == 22:
        nr = pos % 8
        nl = 7 - (pos % 8)
        ul = pos
        ll = pos
        ur = pos
        lr = pos
        accum2 = []
        for i in range(0, nr, 1):
            lr -= 9
            if IsOnBoard(lr):
                if board[pos] > 20:
                    if board[lr] < 20 and board[lr] != 0:
                        accum2 += [lr]
                        break
                    elif board[lr] == 0:
                        accum2 += [lr]
                    elif board[lr] > 19 and board[lr] != 0:
                        break
                elif board[pos] < 20:
                    if board[lr] > 19 and board[lr] != 0:
                        accum2 += [lr]
                        break
                    elif board[lr] == 0:
                        accum2 += [lr]
                    elif board[lr] < 20 and board[lr] != 0:
                        break

        for i in range(0, nr, 1):
            ur += 7
            if IsOnBoard(ur):
                if board[pos] > 20:
                    if board[ur] < 20 and board[ur] != 0:
                        accum2 += [ur]
                        break
                    elif board[ur] == 0:
                        accum2 += [ur]
                    elif board[ur] > 19 and board[ur] != 0:
                        break
                elif board[pos] < 20:
                    if board[ur] > 19 and board[ur] != 0:
                        accum2 += [ur]
                        break
                    elif board[ur] == 0:
                        accum2 += [ur]
                    elif board[ur] < 20 and board[ur] != 0:
                        break
        for j in range(0, nl, 1):
            ul += 9
            if IsOnBoard(ul):
                if board[pos] > 20:
                    if board[ul] < 20 and board[ul] != 0:
                        accum2 += [ul]
                        break
                    elif board[ul] == 0:
                        accum2 += [ul]
                    elif board[ul] > 19 and board[ul] != 0:
                        break
                elif board[pos] < 20:
                    if board[ul] > 19 and board[ul] != 0:
                        accum2 += [ul]
                        break
                    elif board[ul] == 0:
                        accum2 += [ul]
                    elif board[ul] < 20 and board[ul] != 0:
                        break
        for j in range(0, nl, 1):
            ll -= 7
            if IsOnBoard(ll):
                if board[pos] > 19:
                    if board[ll] < 20 and board[ll] != 0:
                        accum2 += [ll]
                        break
                    elif board[ll] == 0:
                        accum2 += [ll]
                    elif board[ll] > 19 and board[ll] != 0:
                        break
                elif board[pos] < 20:
                    if board[ll] > 19 and board[ll] != 0:
                        accum2 += [ll]
                        break
                    elif board[ll] == 0:
                        accum2 += [ll]
                    elif board[ll] < 20 and board[ll] != 0:
                        break
        moves = list(accum2)
    elif board[pos] == 14 or board[pos] == 24:
        nl = pos % 8
        nr = 7 - (pos % 8)
        nd = pos // 8
        nu = 7 - (pos // 8)
        accum=[]
        # print nl,nr,nd,nu
        l = r = u = d = pos
        for i in range(0, nl, 1):
            l -= 1
            if IsOnBoard(l):
                if board[pos] > 20:
                    if board[l] < 20 and board[l] != 0:
                        accum += [l]
                        break
                    elif board[l] == 0:
                        accum += [l]
                elif board[pos] < 20:
                    if board[l] > 19 and board[l] != 0:
                        accum += [l]
                        break
                    elif board[l] == 0:
                        accum += [l]

        for i in range(0, nr, 1):
            r += 1
            if IsOnBoard(r):
                if board[pos] > 20:
                    if board[r] < 20 and board[r] != 0:
                        accum += [r]
                        break
                    elif board[r] == 0:
                        accum += [r]
                elif board[pos] < 20:
                    if board[r] > 19 and board[r] != 0:
                        accum += [r]
                        break
                    elif board[r] == 0:
                        accum += [r]

        for i in range(0, nd, 1):
            d -= 8
            if IsOnBoard(d):
                if board[pos] > 20:
                    if board[d] < 20 and board[d] != 0:
                        accum += [d]
                        break
                    elif board[d] == 0:
                        accum += [d]
                    elif board[d] > 19 and board[d] != 0:
                        break
                elif board[pos] < 20:
                    if board[d] > 19 and board[d] != 0:
                        accum += [d]
                        break
                    elif board[d] == 0:
                        accum += [d]
                    elif board[d] < 20 and board[d] != 0:
                        break
        for i in range(0, nu, 1):
            u += 8
            if IsOnBoard(u):
                if board[pos] > 20:
                    if board[u] < 20 and board[u] != 0:
                        accum += [u]
                        break
                    elif board[u] == 0:
                        accum += [u]
                    elif board[u] > 19 and board[u] != 0:
                        break
                elif board[pos] < 20:
                    if board[u] > 19 and board[u] != 0:
                        accum += [u]
                        break
                    elif board[u] == 0:
                        accum += [u]
                    elif board[u] < 20 and board[u] != 0:
                        break
        nr = pos % 8
        nl = 7 - (pos % 8)
        ul = pos
        ll = pos
        ur = pos
        lr = pos
        accum2 = []
        for i in range(0, nr, 1):
            lr -= 9
            if IsOnBoard(lr):
                if board[pos] > 20:
                    if board[lr] < 20 and board[lr] != 0:
                        accum2 += [lr]
                        break
                    elif board[lr] == 0:
                        accum2 += [lr]
                    elif board[lr] > 19 and board[lr] != 0:
                        break
                elif board[pos] < 20:
                    if board[lr] > 19 and board[lr] != 0:
                        accum2 += [lr]
                        break
                    elif board[lr] == 0:
                        accum2 += [lr]
                    elif board[lr] < 20 and board[lr] != 0:
                        break

        for i in range(0, nr, 1):
            ur += 7
            if IsOnBoard(ur):
                if board[pos] > 20:
                    if board[ur] < 20 and board[ur] != 0:
                        accum2 += [ur]
                        break
                    elif board[ur] == 0:
                        accum2 += [ur]
                    elif board[ur] > 19 and board[ur] != 0:
                        break
                elif board[pos] < 20:
                    if board[ur] > 19 and board[ur] != 0:
                        accum2 += [ur]
                        break
                    elif board[ur] == 0:
                        accum2 += [ur]
                    elif board[ur] < 20 and board[ur] != 0:
                        break
        for j in range(0, nl, 1):
            ul += 9
            if IsOnBoard(ul):
                if board[pos] > 20:
                    if board[ul] < 20 and board[ul] != 0:
                        accum2 += [ul]
                        break
                    elif board[ul] == 0:
                        accum2 += [ul]
                    elif board[ul] > 19 and board[ul] != 0:
                        break
                elif board[pos] < 20:
                    if board[ul] > 19 and board[ul] != 0:
                        accum2 += [ul]
                        break
                    elif board[ul] == 0:
                        accum2 += [ul]
                    elif board[ul] < 20 and board[ul] != 0:
                        break
        for j in range(0, nl, 1):
            ll -= 7
            if IsOnBoard(ll):
                if board[pos] > 19:
                    if board[ll] < 20 and board[ll] != 0:
                        accum2 += [ll]
                        break
                    elif board[ll] == 0:
                        accum2 += [ll]
                    elif board[ll] > 19 and board[ll] != 0:
                        break
                elif board[pos] < 20:
                    if board[ll] > 19 and board[ll] != 0:
                        accum2 += [ll]
                        break
                    elif board[ll] == 0:
                        accum2 += [ll]
                    elif board[ll] < 20 and board[ll] != 0:
                        break
        moves = list(accum + accum2)

    elif board[pos] == 15:
        if (pos+1)<63:
            if (board[pos + 1] == 0 or board[pos + 1] > 16) and (pos+1)%8 !=0 and (pos+1)<63:
                moves = moves + [pos + 1]
        if pos !=0:
            if (board[pos - 1] == 0 or board[pos - 1] > 16) and pos % 8 != 0 and pos !=0:
                moves = moves + [pos - 1]
        if (pos - 7)>=0:
            if (board[pos - 7] == 0 or board[pos - 7] > 16) and (pos+1)%8 !=0 and (pos-7)>=0:
                moves = moves + [pos - 7]
        if (pos - 8)>=0:
            if (board[pos - 8] == 0 or board[pos - 8] > 16) and (pos-8)>=0:
                moves = moves + [pos - 8]
        if (pos - 9)>=63:
            if (board[pos - 9] == 0 or board[pos - 9] > 16) and pos%8 !=0 and (pos-9)>=0:
                moves = moves + [pos - 9]
        if (pos + 7) < 63:
            if (board[pos + 7] == 0 or board[pos + 7] > 16) and pos%8 !=0 and (pos+7)<63:
                moves = moves + [pos + 7]
        if (pos + 8) < 63:
            if (board[pos + 8] == 0 or board[pos + 8] > 16) and (pos+8)<63:
                moves = moves + [pos + 8]
        if (pos+9)<63:
            if (board[pos + 9] == 0 or board[pos + 9] > 16) and (pos+1)%8 !=0 and (pos+9)<63:
                moves = moves + [pos + 9]
        temp = moves
        moves = []
        x = GetPlayerPositions(board, 20)
        opp = []
        for i in x:
            if board[i] !=25:
                opp = opp + GetLegalMoves(board, i)
        for i in temp:
            check = 0
            for j in opp:
                if i == j:
                    check = 1
                elif protected(board,i,20) > 0:
                    check = 1
            if check == 0:
                moves = moves + [i]
    elif board[pos] == 25:
        if (pos+1)<63:
            if (board[pos + 1] == 0 or board[pos + 1] < 16) and (pos+1)%8 !=0 and (pos+1)<63:
                moves = moves + [pos + 1]
        if pos !=0:
            if (board[pos - 1] == 0 or board[pos - 1] < 16) and pos % 8 != 0 and pos !=0:
                moves = moves + [pos - 1]
        if (pos - 7)>=0:
            if (board[pos - 7] == 0 or board[pos - 7] < 16) and (pos+1)%8 !=0 and (pos-7)>=0:
                moves = moves + [pos - 7]
        if (pos - 8)>=0:
            if (board[pos - 8] == 0 or board[pos - 8] < 16) and (pos-8)>=0:
                moves = moves + [pos - 8]
        if (pos - 9)>=63:
            if (board[pos - 9] == 0 or board[pos - 9] < 16) and pos%8 !=0 and (pos-9)>=0:
                moves = moves + [pos - 9]
        if (pos + 7) < 63:
            if (board[pos + 7] == 0 or board[pos + 7] < 16) and pos%8 !=0 and (pos+7)<63:
                moves = moves + [pos + 7]
        if (pos + 8) < 63:
            if (board[pos + 8] == 0 or board[pos + 8] < 16) and (pos+8)<63:
                moves = moves + [pos + 8]
        if (pos+9)<63:
            if (board[pos + 9] == 0 or board[pos + 9] < 16) and (pos+1)%8 !=0 and (pos+9)<63:
                moves = moves + [pos + 9]
        temp = moves
        moves = []
        x=GetPlayerPositions(board,10)
        opp = []
        for i in x:
            if board[i] != 15:
                opp = opp + GetLegalMoves(board,i)
        for i in temp:
            check = 0
            for j in opp:
                if i == j:
                    check = 1
                elif protected(board,i,10) > 0:
                    check = 1
            if check == 0:
                moves = moves + [i]

    elif board[pos] == 11:
            if (pos+17)<63:
                if (board[pos + 17] == 0 or board[pos + 17] > 16) and (pos+1)%8 !=0:
                  moves = moves + [pos + 17]
            if (pos+15)<63:
                if (board[pos + 15] == 0 or board[pos + 15] > 16) and pos % 8 != 0:
                    moves = moves + [pos + 15]
            if (pos-17)>=0:
                if (board[pos - 17] == 0 or board[pos - 17] > 16) and pos%8 !=0:
                    moves = moves + [pos - 17]
            if (pos - 15)>=0:
                if (board[pos - 15] == 0 or board[pos - 15] > 16) and (pos+1)%8 != 0:
                    moves = moves + [pos - 15]
            if (pos-10)>=0:
                if (board[pos - 10] == 0 or board[pos - 10] > 16) and pos%8 !=0 and pos%8 != 1:
                    moves = moves + [pos - 10]
            if (pos+10)<63:
                if (board[pos + 10] == 0 or board[pos + 10] > 16) and pos%8 != 7 and pos%8 != 6:
                    moves = moves + [pos + 10]
            if (pos+6)<63:
                if (board[pos + 6] == 0 or board[pos + 6] > 16) and pos%8 !=0 and pos%8 != 1:
                    moves = moves + [pos + 6]
            if (pos-6)>=0:
                if (board[pos - 6] == 0 or board[pos - 6] > 16) and pos%8 != 7 and pos%8 != 6:
                    moves = moves + [pos - 6]
    elif board[pos] == 21:
            if (pos+17)<63:
                if (board[pos + 17] == 0 or board[pos + 17] < 16) and (pos+1)%8 !=0:
                  moves = moves + [pos + 17]
            if (pos+15)<63:
                if (board[pos + 15] == 0 or board[pos + 15] < 16) and pos % 8 != 0:
                    moves = moves + [pos + 15]
            if (pos-17)>=0:
                if (board[pos - 17] == 0 or board[pos - 17] < 16) and pos%8 !=0:
                    moves = moves + [pos - 17]
            if (pos - 15)>=0:
                if (board[pos - 15] == 0 or board[pos - 15] < 16) and (pos+1)%8 != 0:
                    moves = moves + [pos - 15]
            if (pos-10)>=0:
                if (board[pos - 10] == 0 or board[pos - 10] < 16) and pos%8 !=0 and pos%8 != 1:
                    moves = moves + [pos - 10]
            if (pos+10)<63:
                if (board[pos + 10] == 0 or board[pos + 10] < 16) and pos%8 != 7 and pos%8 != 6:
                    moves = moves + [pos + 10]
            if (pos+6)<63:
                if (board[pos + 6] == 0 or board[pos + 6] < 16) and pos%8 !=0 and pos%8 != 1:
                    moves = moves + [pos + 6]
            if (pos-6)>=0:
                if (board[pos - 6] == 0 or board[pos - 6] < 16) and pos%8 != 7 and pos%8 != 6:
                    moves = moves + [pos - 6]
    return moves


def GetPlayerPositions(board,player):
    wpieces=[]
    bpieces=[]
    if player == 10:
        for i in range(0,64):
            if board[i] > 0 and board[i] <20:
                wpieces = wpieces + [i]
        return wpieces
    elif player == 20:
        for i in range(0,64):
            if board[i] > 15 and board[i] <30:
                bpieces = bpieces + [i]
        return bpieces

def protected(board,pos,player):
    temp = board[pos]
    if player == 10:
        board[pos] = 20
    else:
        board[pos] = 10
    scr=0
    opp=[]
    x=GetPlayerPositions(board,player)
    for i in x:
        if player == 10 and board[i] != 15:
            opp = opp + GetLegalMoves(board, i)
        elif player == 20 and board[i] != 25:
            opp = opp + GetLegalMoves(board, i)
    for j in opp:
        if j == pos:
            scr += 1
    board[pos] = temp
    return scr


def IsPositionUnderThreat(board,pos,player):
    if player == 10:
        x=GetPlayerPositions(board,20)
        for i in x:
            if i != 25:
                y=GetLegalMoves(board,i)
                for j in y:
                    if j == pos:
                        return True
    elif player == 20:
        x=GetPlayerPositions(board,10)
        for i in x:
            if i != 15:
                y=GetLegalMoves(board,i)
                for j in y:
                    if j == pos:
                        return True
    return False

def col(pos):
    return 8-(pos%8)

def row(pos):
    return (pos//8) + 1

def CheckMate(board,player):
    x=GetPlayerPositions(board,player)
    if player == 10:
        for i in x:
            if board[i] == 15:
                n = i
        if IsPositionUnderThreat(board,n,10):
            if GetLegalMoves(board,n) == []:
                return True
    elif player == 20:
        for i in x:
            if board[i] == 25:
                n = i
        if IsPositionUnderThreat(board,n,20):
            if GetLegalMoves(board,n) == []:
                return True




def move(board, new, old):
    x = GetLegalMoves(board, old)
    if x == []:
        return False
    for i in x:
        if new == i and board[old] == 10 and row(new) == 8:
            board[new] = 14
            board[old] = 0
        elif new == i and board[old] == 20 and row(new) == 0:
            board[new] = 24
            board[old] = 0
        elif new == i:
            board[new] = board[old]
            board[old] = 0
    return True

class queue:
    def __init__(self):
        self.x = []
        self.cnt = 0


    def add(self, val):
        self.x = self.x + [val]
        return True;


    def delete(self):
        r = self.x[0]
        self.x = self.x[1:len(self.x)]
        return r


    def empty(self):
        if self.x == []:
            return True
        else:
            return False


def score(board, player):
    score = 0
    if player == 10:
        x = GetPlayerPositions(board, 10)
        y = GetPlayerPositions(board, 20)
        for i in x:
            if board[i] != 15:
                score += 10 * (board[i] - 9)
                if board[i] == 11:
                    score += 10
                if board[i] == 14:
                    score += 50
                if board[i] == 13:
                    score += 20

        for a in y:
            if board[a] != 25:
                score -= 10 * (board[a] - 19)
                if board[a] == 21:
                    score -= 10
                if board[a] == 24:
                    score -= 50
                if board[a] == 23:
                    score -= 20
        for j in x:
            score += len(GetLegalMoves(board, j))
        for b in y:
            score -= len(GetLegalMoves(board, b))
        for k in x:
            score += 2*protected(board,k,10)
        for c in y:
            score -= 2*protected(board,c,20)
        for l in x:
            if (row(l) == 5 or row(l) == 4) and (col(l) == 5 or col(l) == 4):
                score += 4
            elif (row(l) == 6 or row(l) == 3) and 2<col(l)<7:
                score += 2
            elif (col(l) == 6 or col(l) == 3) and 2<row(l)<7:
                score += 2
            elif (row(l) == 7 or row(l) == 2) and 1<col(l)<8:
                score += 1
            elif (col(l) == 7 or col(l) == 2) and 1<row(l)<8:
                score += 1
        for d in y:
            if (row(d) == 5 or row(d) == 4) and (col(d) == 5 or col(d) == 4):
                score -= 4
            elif (row(d) == 6 or row(d) == 3) and 2<col(d)<7:
                score -= 2
            elif (col(d) == 6 or col(d) == 3) and 2<row(d)<7:
                score -= 2
            elif (row(d) == 7 or row(d) == 2) and 1<col(d)<8:
                score -= 1
            elif (col(d) == 7 or col(d) == 2) and 1<row(d)<8:
                score -= 1
        for m in x:
            if board[m] != 15:
                if IsPositionUnderThreat(board,m,player):
                    score -= 25
        for e in y:
            if board[e] != 25:
                if IsPositionUnderThreat(board,e,player):
                    score += 25
        if CheckMate(board, 10):
            score -= 1000
        if CheckMate(board, 20):
            score += 1000
    elif player == 20:
        y = GetPlayerPositions(board, 10)
        x = GetPlayerPositions(board, 20)
        for i in x:
            if board[i] != 25:
                if board[i] != 25:
                    score += 10 * (board[i] - 19)
                    if board[i] == 21:
                        score += 10
                    if board[i] == 24:
                        score += 50
                    if board[i] == 23:
                        score += 20
            if board[i] == 25:
                score +=1000
        for a in y:
            if board[a] != 15:
                score -= 10 * (board[a] - 9)
                if board[a] == 11:
                    score -= 10
                if board[a] == 14:
                    score -= 50
                if board[a] == 13:
                    score -= 20
            if board[a] == 15:
                score -=1000
        for j in x:
            score += len(GetLegalMoves(board, j))
        for b in y:
            score -= len(GetLegalMoves(board, b))
        for k in x:
            score += 2*protected(board,k,20)
        for c in y:
            score -= 2*protected(board,c,10)
        for l in x:
            if (row(l) == 5 or row(l) == 4) and (col(l) == 5 or col(l) == 4):
                score += 4
            elif (row(l) == 6 or row(l) == 3) and 2<col(l)<7:
                score += 2
            elif (col(l) == 6 or col(l) == 3) and 2<row(l)<7:
                score += 2
            elif (row(l) == 7 or row(l) == 2) and 1<col(l)<8:
                score += 1
            elif (col(l) == 7 or col(l) == 2) and 1<row(l)<8:
                score += 1
        for d in y:
            if (row(d) == 5 or row(d) == 4) and (col(d) == 5 or col(d) == 4):
                score -= 4
            elif (row(d) == 6 or row(d) == 3) and 2<col(d)<7:
                score -= 2
            elif (col(d) == 6 or col(d) == 3) and 2<row(d)<7:
                score -= 2
            elif (row(d) == 7 or row(d) == 2) and 1<col(d)<8:
                score -= 1
            elif (col(d) == 7 or col(d) == 2) and 1<row(d)<8:
                score -= 1
        for m in x:
            if board[m] != 25:
                if IsPositionUnderThreat(board,m,player):
                    score -= 25
        for e in y:
            if board[e] != 15:
                if IsPositionUnderThreat(board,e,player):
                    score += 25
        if CheckMate(board, 10):
            score += 1000
        if CheckMate(board, 20):
            score -= 1000
    return score

def canMoves(board,player,player2):
    new = list(board)
    root = [new,[]]
    root[1] = candidateMoves3(new,player,root[1])
    for i in root[1]:
        i[1] = candidateMoves3(i[0],player2,i[1])
    return root

def candidateMoves3(board, player, root):
    x=GetPlayerPositions(board, player)
    for i in x:
        t = GetLegalMoves(board,i)
        for j in t:
            new = list(board)
            move(new,j,i)
            root = root + [[new,[]]]
    return root

def candidateMoves(board, player, root):
    x=GetPlayerPositions(board, player)
    for i in x:
        t = GetLegalMoves(board,i)
        for j in t:
            new = list(board)
            move(new,j,i)
            root = root + [[new,score(new,player),[]]]
    return root

def candidateMoves2(board, player, root):
    x=GetPlayerPositions(board, player)
    for i in x:
        t = GetLegalMoves(board,i)
        for j in t:
            new = list(board)
            move(new,j,i)
            root = root + [[[j,i],score(new,player)]]
    return root

def minimax(board,player,player2):
    new = list(board)
    root = [new, score(new,player), []]
    root[2] = candidateMoves(new, player, root[2])
    for i in root[2]:
        i[2] = candidateMoves(i[0], player2, i[2])
        avg = -100000000000
        for k in range(0,len(i[2])):
            if i[2][k][1] > avg:
                avg = i[2][k][1]
        i[1] =avg
    return root[2]

def chessPlayer(board,player):
    #return move
    if player == 10:
        player2 = 20
    else:
        player2 = 10
    ll = list(minimax(board,player,player2))
    root=[]
    lc = candidateMoves2(board,player,root)
    move = []
    score = 0
    for i in range(0,len(ll)):
        if ll[i][1] > score:
            score = ll[i][1]
            move = lc[i][0]
    status = False
    if move != []:
        status = True
    return [status, move, lc, evalTree(canMoves(board,player,player2))]

def evalTree(l):
    x = queue()
    x.add(l)
    lis = []
    while x.empty() == False:
        r = x.delete()
        lis += [r[0]]
        for i in r[1]:
            x.add(i)
    return (lis)






