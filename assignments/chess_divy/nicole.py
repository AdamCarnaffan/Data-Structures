import random

def InitEmptyBoard():
    board = []
    for i in range (0,64,1):
        board = board + [0]
    return board

#print(InitEmptyBoard())
#print(len(InitEmptyBoard()))

def InitBoard (board):
    for i in range (0,64,1):
        if (i==0) or (i==7):
            board[i] = 13
        elif (i==1) or (i==6):
            board[i] = 11
        elif (i==2) or (i==5):
            board[i] = 12
        elif (i==3):
            board[i] = 15
        elif (i==4):
            board[i] = 14
        elif (i>=8) and (i<16):
            board[i] = 10
        elif (i>=48) and (i<56):
            board[i] = 20
        elif (i==56) or (i==63):
            board[i] = 23
        elif (i==57) or (i==62):
            board[i] = 21
        elif (i==58) or (i==61):
            board[i] = 22
        elif (i==59):
            board[i] = 25
        elif (i==60):
            board[i] = 24
    return board

# print(InitBoard(InitEmptyBoard()))

def InitNumberBoard():
    NumberBoard = [] 
    for i in range (0,64,1):
        NumberBoard = NumberBoard + [i]
    return NumberBoard

# print(InitNumberBoard())

def PrintNumberBoard(board):
    print("------INDEX BOARD------")
    printnumberboard = ""
    for i in range (7,-1,-1):
        for j in range (7,-1,-1):
            printnumberboard = printnumberboard + str(board[i*8+j]) + " "
            if board[i*8+j]<=9:
                printnumberboard = printnumberboard + " "
        print(printnumberboard)
        printnumberboard = ""
    print("-----------------------")
    return True

# PrintNumberBoard(InitNumberBoard())

def GetPlayerPositions (board,player):
    PlayerOccupied = []
    for i in range (0,64,1):
        if (player==10):
            if (board[i]>=10) and (board[i]<20):
                PlayerOccupied = PlayerOccupied + [i]
        elif (player==20):
            if (board[i]>=20):
                PlayerOccupied = PlayerOccupied + [i]
        else:
            return -1 
    return PlayerOccupied
            
# print(GetPlayerPositions(InitBoard(InitEmptyBoard()),20))

def PrintBoard(board):
    printboard = ""
    for i in range (7,-1,-1):
        for j in range (7,-1,-1):
            if board[i*8+j]==10:
                printboard = printboard + "p" + "  " 
            if board[i*8+j]==11:
                printboard = printboard + "kn" + " "
            if board[i*8+j]==12:
                printboard = printboard + "b" + "  " 
            if board[i*8+j]==13:
                printboard = printboard + "r" + "  " 
            if board[i*8+j]==14:
                printboard = printboard + "q" + "  " 
            if board[i*8+j]==15:
                printboard = printboard + "k" + "  " 
            if (board[i*8+j]==0):
                printboard = printboard + str(board[i*8+j]) + "  "
            if board[i*8+j]==20:
                printboard = printboard + "P" + "  " 
            if board[i*8+j]==21:
                printboard = printboard + "KN" + " "
            if board[i*8+j]==22:
                printboard = printboard + "B" + "  " 
            if board[i*8+j]==23:
                printboard = printboard + "R" + "  " 
            if board[i*8+j]==24:
                printboard = printboard + "Q" + "  " 
            if board[i*8+j]==25:
                printboard = printboard + "K" + "  " 
        print(printboard)
        printboard = ""
    print("-----------------------")
    return True

# PrintBoard(InitBoard(InitEmptyBoard()))

def GetColour(board,position):
    if position>63 or position<0:
        return -1
    if board[position]>=20:
        colour = "Black"
    elif board[position]==0:
        colour = "Empty Space"
    else:
        colour = "White"
    return colour

# print(GetColour(InitBoard(InitEmptyBoard()),-2))

def TestBoard():
    TestBoard = []
    for i in range(0,64,1):
        TestBoard = TestBoard + [0]

    TestBoard[56] = 15
    TestBoard[63] = 11
    TestBoard[51] = 20
    TestBoard[34] = 25
    TestBoard[4] = 13

    return TestBoard

# print(TestBoard())
# Tester = TestBoard()
# PrintBoard(Tester)
# print(GetColour(Tester,6))

def GetRow(position):
    if position>63 or position<0:
        return -1
    if position>=0 and position<=7:
        row = 7
    elif position>=8 and position<=15:
        row = 6
    elif position>=16 and position<=23:
        row = 5
    elif position>=24 and position<=31:
        row = 4 
    elif position>=32 and position<=39:
        row = 3
    elif position>=40 and position<=47:
        row = 2
    elif position>=48 and position<=55:
        row = 1
    elif position>=56 and position<=63:
        row = 0
    return row

# print(GetRow(56))

def GetColumn(position):
    if position>63 or position<0:
        return -1
    num = position%8
    if num==0:
        return 7
    if num==1:
        return 6
    if num==2:
        return 5
    if num==3:
        return 4
    if num==4:
        return 3
    if num==5:
        return 2
    if num==6:
        return 1
    if num==7:
        return 0

# print(GetColumn(44))

def GetPieceLegalMoves(board,position):
    PossibleMoves = []
    if position>63 or position<0:
        return -1
    if board[position] == 10:  #White Pawn
        if position%8 == 0:
            if board[position+8]==0:
                PossibleMoves = PossibleMoves + [position+8]
            if GetColour(board,position+9) == "Black":
                PossibleMoves = PossibleMoves + [position+9]
        elif (position+1)%8 == 0:
            if board[position+8]==0:
                PossibleMoves = PossibleMoves + [position+8]
            if GetColour(board,position+7) == "Black":
                PossibleMoves = PossibleMoves + [position+7]
        else:
            if board[position+8]==0:
                PossibleMoves = PossibleMoves + [position+8]
            if GetColour(board,position+7) == "Black":
                PossibleMoves = PossibleMoves + [position+7]
            if GetColour(board,position+9) == "Black":
                PossibleMoves = PossibleMoves + [position+9]    
    if board[position] == 20: #Black Pawn
        if position%8 == 0:
            if board[position-8]==0:
                PossibleMoves = PossibleMoves + [position-8]
            if GetColour(board,position-7) == "White":
                PossibleMoves = PossibleMoves + [position-7]
        elif (position-1)%8 == 0:
            if board[position-8]==0:
                PossibleMoves = PossibleMoves + [position-8]
            if GetColour(board,position-9) == "White":
                PossibleMoves = PossibleMoves + [position-9]
        else:
            if board[position-8]==0:
                PossibleMoves = PossibleMoves + [position-8]
            if GetColour(board,position-7) == "White":
                PossibleMoves = PossibleMoves + [position-7]
            if GetColour(board,position-9) == "White":
                PossibleMoves = PossibleMoves + [position-9]
    if board[position] == 13: #White Rook
        d = 1
        u = 1
        r = 1
        l = 1
        while d < 8 and position-8*d>=0:
            if GetColour(board,position-8*d) == "White":
                break
            elif GetColour(board,position-8*d) == "Black":
                PossibleMoves = PossibleMoves + [position-8*d]
                break
            elif board[position-8*d]==0:
                PossibleMoves = PossibleMoves + [position-8*d]
                d+=1
        while u < 8 and position+8*u<=63:
            if GetColour(board,position+8*u) == "White":
                break
            elif GetColour(board,position+8*u) == "Black":
                PossibleMoves = PossibleMoves + [position+8*u]
                break
            elif board[position+8*u]==0:
                PossibleMoves = PossibleMoves + [position+8*u]
                u+=1
        while r < 8 and position-r>=((7-GetRow(position))*8):
            if GetColour(board,position-r) == "White":
                break
            elif GetColour(board,position-r) == "Black":
                PossibleMoves = PossibleMoves + [position-r]
                break
            elif board[position-r]==0:
                PossibleMoves = PossibleMoves + [position-r]
                r+=1
        while l < 8 and position+l<=(((7-GetRow(position))*8)+7):
            if GetColour(board,position+l) == "White":
                break
            elif GetColour(board,position+l) == "Black":
                PossibleMoves = PossibleMoves + [position+l]
                break
            elif board[position+l]==0:
                PossibleMoves = PossibleMoves + [position+l]
                l+=1
    if board[position] == 23: #Black Rook
        d = 1
        u = 1
        r = 1
        l = 1
        while d < 8 and position-8*d>=0:
            if GetColour(board,position-8*d) == "Black":
                break
            elif GetColour(board,position-8*d) == "White":
                PossibleMoves = PossibleMoves + [position-8*d]
                break
            elif board[position-8*d]==0:
                PossibleMoves = PossibleMoves + [position-8*d]
                d+=1
        while u < 8 and position+8*u<=63:
            if GetColour(board,position+8*u) == "Black":
                break
            elif GetColour(board,position+8*u) == "White":
                PossibleMoves = PossibleMoves + [position+8*u]
                break
            elif board[position+8*u]==0:
                PossibleMoves = PossibleMoves + [position+8*u]
                u+=1
        while r < 8 and position-r>=((7-GetRow(position))*8):
            if GetColour(board,position-r) == "Black":
                break
            elif GetColour(board,position-r) == "White":
                PossibleMoves = PossibleMoves + [position-r]
                break
            elif board[position-r]==0:
                PossibleMoves = PossibleMoves + [position-r]
                r+=1
        while l < 8 and position+l<=(((7-GetRow(position))*8)+7):
            if GetColour(board,position+l) == "Black":
                break
            elif GetColour(board,position+l) == "White":
                PossibleMoves = PossibleMoves + [position+l]
                break
            elif board[position+l]==0:
                PossibleMoves = PossibleMoves + [position+l]
                l+=1
    if board[position] == 12: #White Bishop
        ul = 1
        ur = 1
        dl = 1
        dr = 1 
        while ul <= min(GetRow(position),GetColumn(position)):
            # print(min(GetRow(position),GetColumn(position)))
            if GetColour(board,position+8*ul+ul) == "White":
                break
            elif GetColour(board,position+8*ul+ul) == "Black":
                PossibleMoves = PossibleMoves + [position+8*ul+ul]
                break
            elif board[position+8*ul+ul]==0:
                PossibleMoves = PossibleMoves + [position+8*ul+ul]
                # print(ul)
                # print(PossibleMoves)
                ul+=1
        while ur <= min(GetRow(position),7-GetColumn(position)):
            # print(min(GetRow(position),7-GetColumn(position)))
            if GetColour(board,position+8*ur-ur) == "White":
                break
            elif GetColour(board,position+8*ur-ur) == "Black":
                PossibleMoves = PossibleMoves + [position+8*ur-ur]
                break
            elif board[position+8*ur-ur]==0:
                PossibleMoves = PossibleMoves + [position+8*ur-ur]
                # print(ur)
                # print(PossibleMoves)
                ur+=1 
        while dl <= min(GetColumn(position),7-GetRow(position)):
            # print(min(GetColumn(position),7-GetRow(position)))
            if GetColour(board,position-8*dl+dl) == "White":
                break
            elif GetColour(board,position-8*dl+dl) == "Black":
                PossibleMoves = PossibleMoves + [position-8*dl+dl]
                break
            elif board[position-8*dl+dl]==0:
                PossibleMoves = PossibleMoves + [position-8*dl+dl]
                # print(dl)
                # print(PossibleMoves)
                dl+=1
        while dr <= min(7-GetColumn(position),7-GetRow(position)):
            # print(min(7-GetColumn(position),7-GetRow(position)))
            if GetColour(board,position-8*dr-dr) == "White":
                break
            elif GetColour(board,position-8*dr-dr) == "Black":
                PossibleMoves = PossibleMoves + [position-8*dr-dr]
                break
            elif board[position-8*dr-dr]==0:
                PossibleMoves = PossibleMoves + [position-8*dr-dr]
                # print(dr)
                # print(PossibleMoves)
                dr+=1
        # print(ul,ur,dl,dr)
    if board[position] == 22: #Black Bishop 
        ul = 1
        ur = 1
        dl = 1
        dr = 1 
        while ul <= min(GetRow(position),GetColumn(position)):
            # print(min(GetRow(position),GetColumn(position)))
            if GetColour(board,position+8*ul+ul) == "Black":
                break
            elif GetColour(board,position+8*ul+ul) == "White":
                PossibleMoves = PossibleMoves + [position+8*ul+ul]
                break
            elif board[position+8*ul+ul]==0:
                PossibleMoves = PossibleMoves + [position+8*ul+ul]
                # print(ul)
                # print(PossibleMoves)
                ul+=1
        while ur <= min(GetRow(position),7-GetColumn(position)):
            # print(min(GetRow(position),7-GetColumn(position)))
            if GetColour(board,position+8*ur-ur) == "Black":
                break
            elif GetColour(board,position+8*ur-ur) == "White":
                PossibleMoves = PossibleMoves + [position+8*ur-ur]
                break
            elif board[position+8*ur-ur]==0:
                PossibleMoves = PossibleMoves + [position+8*ur-ur]
                # print(ur)
                # print(PossibleMoves)
                ur+=1 
        while dl <= min(GetColumn(position),7-GetRow(position)):
            # print(min(GetColumn(position),7-GetRow(position)))
            if GetColour(board,position-8*dl+dl) == "Black":
                break
            elif GetColour(board,position-8*dl+dl) == "White":
                PossibleMoves = PossibleMoves + [position-8*dl+dl]
                break
            elif board[position-8*dl+dl]==0:
                PossibleMoves = PossibleMoves + [position-8*dl+dl]
                # print(dl)
                # print(PossibleMoves)
                dl+=1
        while dr <= min(7-GetColumn(position),7-GetRow(position)):
            # print(min(7-GetColumn(position),7-GetRow(position)))
            if GetColour(board,position-8*dr-dr) == "Black":
                break
            elif GetColour(board,position-8*dr-dr) == "White":
                PossibleMoves = PossibleMoves + [position-8*dr-dr]
                break
            elif board[position-8*dr-dr]==0:
                PossibleMoves = PossibleMoves + [position-8*dr-dr]
                # print(dr)
                # print(PossibleMoves)
                dr+=1
        # print(ul,ur,dl,dr)
    if board[position] == 11: #White Knight
        if GetRow(position)<=5 and GetColumn(position)>=1 and GetColour(board,position-15)!="White":
            PossibleMoves = PossibleMoves + [position-15]
            # print(PossibleMoves)
        if GetRow(position)<=5 and GetColumn(position)<=6 and GetColour(board,position-17)!="White":
            PossibleMoves = PossibleMoves + [position-17]
            # print(PossibleMoves)
        if GetRow(position)<=6 and GetColumn(position)<=5 and GetColour(board,position-10)!="White":
            PossibleMoves = PossibleMoves + [position-10]
            # print(PossibleMoves)
        if GetRow(position)>=1 and GetColumn(position)<=5 and GetColour(board,position+6)!="White":
            PossibleMoves = PossibleMoves + [position+6]
            # print(PossibleMoves)
        if GetRow(position)>=2 and GetColumn(position)<=6 and GetColour(board,position+15)!="White":
            PossibleMoves = PossibleMoves + [position+15]
            # print(PossibleMoves)
        if GetRow(position)>=2 and GetColumn(position)>=1 and GetColour(board,position+17)!="White":
            PossibleMoves = PossibleMoves + [position+17]
            # print(PossibleMoves)
        if GetRow(position)>=1 and GetColumn(position)>=2 and GetColour(board,position+10)!="White":
            PossibleMoves = PossibleMoves + [position+10]
            # print(PossibleMoves)
        if GetRow(position)<=6 and GetColumn(position)>=2 and GetColour(board,position-6)!="White":
            PossibleMoves = PossibleMoves + [position-6]
            # print(PossibleMoves)
    if board[position] == 21: #Black Knight
        if GetRow(position)<=5 and GetColumn(position)>=1 and GetColour(board,position-15)!="Black":
            PossibleMoves = PossibleMoves + [position-15]
            # print(PossibleMoves)
        if GetRow(position)<=5 and GetColumn(position)<=6 and GetColour(board,position-17)!="Black":
            PossibleMoves = PossibleMoves + [position-17]
            # print(PossibleMoves)
        if GetRow(position)<=6 and GetColumn(position)<=5 and GetColour(board,position-10)!="Black":
            PossibleMoves = PossibleMoves + [position-10]
            # print(PossibleMoves)
        if GetRow(position)>=1 and GetColumn(position)<=5 and GetColour(board,position+6)!="Black":
            PossibleMoves = PossibleMoves + [position+6]
            # print(PossibleMoves)
        if GetRow(position)>=2 and GetColumn(position)<=6 and GetColour(board,position+15)!="Black":
            PossibleMoves = PossibleMoves + [position+15]
            # print(PossibleMoves)
        if GetRow(position)>=2 and GetColumn(position)>=1 and GetColour(board,position+17)!="Black":
            PossibleMoves = PossibleMoves + [position+17]
            # print(PossibleMoves)
        if GetRow(position)>=1 and GetColumn(position)>=2 and GetColour(board,position+10)!="Black":
            PossibleMoves = PossibleMoves + [position+10]
            # print(PossibleMoves)
        if GetRow(position)<=6 and GetColumn(position)>=2 and GetColour(board,position-6)!="Black":
            PossibleMoves = PossibleMoves + [position-6]
            # print(PossibleMoves)
    if board[position] == 14: #White Queen
        d = 1
        u = 1
        r = 1
        l = 1
        ul = 1
        ur = 1
        dl = 1
        dr = 1 
        while d < 8 and position-8*d>=0:
            if GetColour(board,position-8*d) == "White":
                break
            elif GetColour(board,position-8*d) == "Black":
                PossibleMoves = PossibleMoves + [position-8*d]
                break
            elif board[position-8*d]==0:
                PossibleMoves = PossibleMoves + [position-8*d]
                d+=1
        while u < 8 and position+8*u<=63:
            if GetColour(board,position+8*u) == "White":
                break
            elif GetColour(board,position+8*u) == "Black":
                PossibleMoves = PossibleMoves + [position+8*u]
                break
            elif board[position+8*u]==0:
                PossibleMoves = PossibleMoves + [position+8*u]
                u+=1
        while r < 8 and position-r>=((7-GetRow(position))*8):
            if GetColour(board,position-r) == "White":
                break
            elif GetColour(board,position-r) == "Black":
                PossibleMoves = PossibleMoves + [position-r]
                break
            elif board[position-r]==0:
                PossibleMoves = PossibleMoves + [position-r]
                r+=1
        while l < 8 and position+l<=(((7-GetRow(position))*8)+7):
            if GetColour(board,position+l) == "White":
                break
            elif GetColour(board,position+l) == "Black":
                PossibleMoves = PossibleMoves + [position+l]
                break
            elif board[position+l]==0:
                PossibleMoves = PossibleMoves + [position+l]
                l+=1
        while ul <= min(GetRow(position),GetColumn(position)):
            # print(min(GetRow(position),GetColumn(position)))
            if GetColour(board,position+8*ul+ul) == "White":
                break
            elif GetColour(board,position+8*ul+ul) == "Black":
                PossibleMoves = PossibleMoves + [position+8*ul+ul]
                break
            elif board[position+8*ul+ul]==0:
                PossibleMoves = PossibleMoves + [position+8*ul+ul]
                # print(ul)
                # print(PossibleMoves)
                ul+=1
        while ur <= min(GetRow(position),7-GetColumn(position)):
            # print(min(GetRow(position),7-GetColumn(position)))
            if GetColour(board,position+8*ur-ur) == "White":
                break
            elif GetColour(board,position+8*ur-ur) == "Black":
                PossibleMoves = PossibleMoves + [position+8*ur-ur]
                break
            elif board[position+8*ur-ur]==0:
                PossibleMoves = PossibleMoves + [position+8*ur-ur]
                # print(ur)
                # print(PossibleMoves)
                ur+=1 
        while dl <= min(GetColumn(position),7-GetRow(position)):
            # print(min(GetColumn(position),7-GetRow(position)))
            if GetColour(board,position-8*dl+dl) == "White":
                break
            elif GetColour(board,position-8*dl+dl) == "Black":
                PossibleMoves = PossibleMoves + [position-8*dl+dl]
                break
            elif board[position-8*dl+dl]==0:
                PossibleMoves = PossibleMoves + [position-8*dl+dl]
                # print(dl)
                # print(PossibleMoves)
                dl+=1
        while dr <= min(7-GetColumn(position),7-GetRow(position)):
            # print(min(7-GetColumn(position),7-GetRow(position)))
            if GetColour(board,position-8*dr-dr) == "White":
                break
            elif GetColour(board,position-8*dr-dr) == "Black":
                PossibleMoves = PossibleMoves + [position-8*dr-dr]
                break
            elif board[position-8*dr-dr]==0:
                PossibleMoves = PossibleMoves + [position-8*dr-dr]
                # print(dr)
                # print(PossibleMoves)
                dr+=1
        # print(ul,ur,dl,dr)
    if board[position] == 24: #Black Queen
        d = 1
        u = 1
        r = 1
        l = 1
        ul = 1
        ur = 1
        dl = 1
        dr = 1 
        while d < 8 and position-8*d>=0:
            if GetColour(board,position-8*d) == "Black":
                break
            elif GetColour(board,position-8*d) == "White":
                PossibleMoves = PossibleMoves + [position-8*d]
                break
            elif board[position-8*d]==0:
                PossibleMoves = PossibleMoves + [position-8*d]
                d+=1
        while u < 8 and position+8*u<=63:
            if GetColour(board,position+8*u) == "Black":
                break
            elif GetColour(board,position+8*u) == "White":
                PossibleMoves = PossibleMoves + [position+8*u]
                break
            elif board[position+8*u]==0:
                PossibleMoves = PossibleMoves + [position+8*u]
                u+=1
        while r < 8 and position-r>=((7-GetRow(position))*8):
            if GetColour(board,position-r) == "Black":
                break
            elif GetColour(board,position-r) == "White":
                PossibleMoves = PossibleMoves + [position-r]
                break
            elif board[position-r]==0:
                PossibleMoves = PossibleMoves + [position-r]
                r+=1
        while l < 8 and position+l<=(((7-GetRow(position))*8)+7):
            if GetColour(board,position+l) == "Black":
                break
            elif GetColour(board,position+l) == "White":
                PossibleMoves = PossibleMoves + [position+l]
                break
            elif board[position+l]==0:
                PossibleMoves = PossibleMoves + [position+l]
                l+=1
        while ul <= min(GetRow(position),GetColumn(position)):
            # print(min(GetRow(position),GetColumn(position)))
            if GetColour(board,position+8*ul+ul) == "Black":
                break
            elif GetColour(board,position+8*ul+ul) == "White":
                PossibleMoves = PossibleMoves + [position+8*ul+ul]
                break
            elif board[position+8*ul+ul]==0:
                PossibleMoves = PossibleMoves + [position+8*ul+ul]
                # print(ul)
                # print(PossibleMoves)
                ul+=1
        while ur <= min(GetRow(position),7-GetColumn(position)):
            # print(min(GetRow(position),7-GetColumn(position)))
            if GetColour(board,position+8*ur-ur) == "Black":
                break
            elif GetColour(board,position+8*ur-ur) == "White":
                PossibleMoves = PossibleMoves + [position+8*ur-ur]
                break
            elif board[position+8*ur-ur]==0:
                PossibleMoves = PossibleMoves + [position+8*ur-ur]
                # print(ur)
                # print(PossibleMoves)
                ur+=1 
        while dl <= min(GetColumn(position),7-GetRow(position)):
            # print(min(GetColumn(position),7-GetRow(position)))
            if GetColour(board,position-8*dl+dl) == "Black":
                break
            elif GetColour(board,position-8*dl+dl) == "White":
                PossibleMoves = PossibleMoves + [position-8*dl+dl]
                break
            elif board[position-8*dl+dl]==0:
                PossibleMoves = PossibleMoves + [position-8*dl+dl]
                # print(dl)
                # print(PossibleMoves)
                dl+=1
        while dr <= min(7-GetColumn(position),7-GetRow(position)):
            # print(min(7-GetColumn(position),7-GetRow(position)))
            if GetColour(board,position-8*dr-dr) == "Black":
                break
            elif GetColour(board,position-8*dr-dr) == "White":
                PossibleMoves = PossibleMoves + [position-8*dr-dr]
                break
            elif board[position-8*dr-dr]==0:
                PossibleMoves = PossibleMoves + [position-8*dr-dr]
                # print(dr)
                # print(PossibleMoves)
                dr+=1
        # print(ul,ur,dl,dr)
    if board[position] == 15: #White King
        if GetColour(board,position-8) != "White" and GetRow(position)<=6:
            PossibleMoves = PossibleMoves + [position-8]

        if GetColour(board,position+8) != "White" and GetRow(position)>=1:
            PossibleMoves = PossibleMoves + [position+8]
        
        if GetColour(board,position+1) != "White" and GetColumn(position)>=1:
            PossibleMoves = PossibleMoves + [position+1]

        if GetColour(board,position-1) != "White" and GetColumn(position)<=6:
            PossibleMoves = PossibleMoves + [position-1]

        if GetColour(board,position-9) != "White" and GetRow(position)<=6 and GetColumn(position)<=6:
            PossibleMoves = PossibleMoves + [position-9]

        if GetColour(board,position-7) != "White" and GetRow(position)<=6 and GetColumn(position)>=1:
            PossibleMoves = PossibleMoves + [position-7]
        
        if GetColour(board,position+7) != "White" and GetRow(position)>=1 and GetColumn(position)<=6:
            PossibleMoves = PossibleMoves + [position+7]

        if GetColour(board,position+9) != "White" and GetRow(position)>=1 and GetColumn(position)>=1:
            PossibleMoves = PossibleMoves + [position+9]
    if board[position] == 25: #Black King
        if GetColour(board,position-8) != "Black" and GetRow(position)<=6:
            PossibleMoves = PossibleMoves + [position-8]

        if GetColour(board,position+8) != "Black" and GetRow(position)>=1:
            PossibleMoves = PossibleMoves + [position+8]
        
        if GetColour(board,position+1) != "Black" and GetColumn(position)>=1:
            PossibleMoves = PossibleMoves + [position+1]

        if GetColour(board,position-1) != "Black" and GetColumn(position)<=6:
            PossibleMoves = PossibleMoves + [position-1]

        if GetColour(board,position-9) != "Black" and GetRow(position)<=6 and GetColumn(position)<=6:
            PossibleMoves = PossibleMoves + [position-9]

        if GetColour(board,position-7) != "Black" and GetRow(position)<=6 and GetColumn(position)>=1:
            PossibleMoves = PossibleMoves + [position-7]
        
        if GetColour(board,position+7) != "Black" and GetRow(position)>=1 and GetColumn(position)<=6:
            PossibleMoves = PossibleMoves + [position+7]

        if GetColour(board,position+9) != "Black" and GetRow(position)>=1 and GetColumn(position)>=1:
            PossibleMoves = PossibleMoves + [position+9]
    return PossibleMoves

# print(GetPieceLegalMoves(Tester,56))

def IsPositionUnderThreat(board,position,player):
    if position>63 or position<0:
        return -1
    if player==10: #White Player
        OccupiedByBlack = GetPlayerPositions(board,20) 
        # print(OccupiedByBlack)
        # print(len(OccupiedByBlack))
        for i in range (0,len(OccupiedByBlack),1):
            LegalMovesByBlack = GetPieceLegalMoves(board,OccupiedByBlack[i])
            # print(OccupiedByBlack[i])
            # print(LegalMovesByBlack)
            if position in LegalMovesByBlack:
                return True 
        return False
    if player==20: #Black Player
        OccupiedByWhite = GetPlayerPositions(board,10) 
        # print(OccupiedByWhite)
        # print(len(OccupiedByWhite))
        for i in range (0,len(OccupiedByWhite),1):
            LegalMovesByWhite = GetPieceLegalMoves(board,OccupiedByWhite[i])
            # print(OccupiedByWhite[i])
            # print(LegalMovesByWhite)
            if position in LegalMovesByWhite:
                return True 
        return False

# print(IsPositionUnderThreat(Tester,56,20))

def GetScore(board):
    WhiteSum = 0 
    BlackSum = 0 
    GetWhitePlayerPositions = GetPlayerPositions(board,10)
    GetBlackPlayerPositions = GetPlayerPositions(board,20)
    for i in range (0,len(GetWhitePlayerPositions),1):
        if board[GetWhitePlayerPositions[i]]==10:
            WhiteSum = WhiteSum + 1.0
        if board[GetWhitePlayerPositions[i]]==11:
            WhiteSum = WhiteSum + 3.0
        if board[GetWhitePlayerPositions[i]]==12:
            WhiteSum = WhiteSum + 3.0
        if board[GetWhitePlayerPositions[i]]==13:
            WhiteSum = WhiteSum + 5.0
        if board[GetWhitePlayerPositions[i]]==14:
            WhiteSum = WhiteSum + 9.0
        if board[GetWhitePlayerPositions[i]]==15:
            WhiteSum = WhiteSum + 90.0
    for j in range (0,len(GetBlackPlayerPositions),1):
        # print(BlackSum)
        # print(GetBlackPlayerPositions)
        # print(board[GetBlackPlayerPositions[j]])
        if board[GetBlackPlayerPositions[j]]==20:
            BlackSum = BlackSum - 1.0
        if board[GetBlackPlayerPositions[j]]==21:
            BlackSum = BlackSum - 3.0
        if board[GetBlackPlayerPositions[j]]==22:
            BlackSum = BlackSum - 3.0
        if board[GetBlackPlayerPositions[j]]==23:
            BlackSum = BlackSum - 5.0
        if board[GetBlackPlayerPositions[j]]==24:
            BlackSum = BlackSum - 9.0
        if board[GetBlackPlayerPositions[j]]==25:
            BlackSum = BlackSum - 90.0
    # print(WhiteSum)
    # print(BlackSum)
    return float(WhiteSum + BlackSum)

# print(GetScore(InitBoard(InitEmptyBoard())))

def Maximum(array):
    top = -10000
    mark = 0
    for i in range(0,len(array),1):
        if array[i][1]>top:
            top = array[i][1]
            mark = i
    return array[mark][0]

def BubbleSort(array):
    swap_flag = False
    for j in range(0,len(array)-1,1):
        if array[j][1]>array[j+1][1]:
            swap = list(array[j])
            array[j]=list(array[j+1])
            array[j+1]= swap
            swap_flag=True
        if not swap_flag:
            break
    return array

# print(BubbleSort([[[1,3],85.0],[[3,4],66.2],[[2,3],90.5]]))

class Queue:
    def __init__(self):
        self.queue = []
    
    def add(self,data):
        self.queue = self.queue + [data]
        return True 





InitializedBoard = InitBoard(InitEmptyBoard())

def chessPlayer(board,player):
    
    ReturnValue=[[],[],[],[]]
    q = Queue()

    AllMoves =[]
    NotAtRiskMoves=[]
    PlayerPositions = GetPlayerPositions(board,player)
    for positions in PlayerPositions:
        # print(positions)
        PlayerMoves = GetPieceLegalMoves(board,positions)
        # print(PlayerMoves)
        for moves in PlayerMoves:
            AllMoves = AllMoves + [[positions]+[moves]]
            MoveswScore = []
            for i in range(0,len(AllMoves),1):
                TempBoard=list(board)
                TempBoard[AllMoves[i][1]] = TempBoard[AllMoves[i][0]]
                TempBoard[AllMoves[i][0]] = 0
                MoveswScore = MoveswScore + [[AllMoves[i]]+[GetScore(TempBoard)]]
                SortedMoves = BubbleSort(MoveswScore)
            # print(SortedMoves)
            # print(AllMoves)
                # PrintBoard(TempBoard)
            # print(moves)
            # print(BoardState[moves])
            # print(GetColour(BoardState,moves))
            # PrintBoard(BoardState)
            if IsPositionUnderThreat(board,moves,10) == False:
                NotAtRiskMoves = NotAtRiskMoves + [[positions]+[moves]]
                # print(NotAtRiskMoves)
                # PrintBoard(BoardState)
    # print(NotAtRiskMoves)
    # print(len(NotAtRiskMoves))
    if len(NotAtRiskMoves)!=0:
        NotAtRiskMoveswScore = []
        for i in range(0,len(NotAtRiskMoves),1):
            # print(i)
            TempBoard=list(board)
            # print(NotAtRiskMoves)
            # print(NotAtRiskMoves[i][0])
            TempBoard[NotAtRiskMoves[i][1]] = TempBoard[NotAtRiskMoves[i][0]]
            TempBoard[NotAtRiskMoves[i][0]] = 0
            # PrintBoard(TempBoard)
            NotAtRiskMoveswScore = NotAtRiskMoveswScore + [[NotAtRiskMoves[i]] + [GetScore(TempBoard)]]
        # print(NotAtRiskMoveswScore)
        q.add(NotAtRiskMoveswScore)
        if player==10:
            for i in range(0,len(NotAtRiskMoveswScore),1):
                if NotAtRiskMoveswScore[i][1]!=0:
                    # print(NotAtRiskMoveswScore[i][1])
                    SortedNotAtRiskMoves = BubbleSort(NotAtRiskMoveswScore)
                    # print(SortedNotAtRiskMoves)
                    ReturnValue[1] = SortedNotAtRiskMoves[-1]
                    break
                else:
                    ReturnValue[1] = SortedMoves[random.randint(0,len(SortedMoves)-1)][0]
                    break
        else:
            for i in range(0,len(NotAtRiskMoveswScore),1):
                if NotAtRiskMoveswScore[i][1]!=0:
                    # print(NotAtRiskMoveswScore[i][1])
                    SortedNotAtRiskMoves = BubbleSort(NotAtRiskMoveswScore)
                    # print(SortedNotAtRiskMoves)
                    ReturnValue[1] = SortedNotAtRiskMoves[0]
                    break
                else:
                    ReturnValue[1] = SortedMoves[random.randint(0,len(SortedMoves)-1)][0]
                    break
        # print(SortedMoves)
    else: 
        if player==10:
            ReturnValue[1] = SortedMoves[random.randint(0,len(SortedMoves)-1)][0]
        else:
            ReturnValue[1]=SortedMoves[random.randint(0,len(SortedMoves))][0]

    ReturnValue[2] = [MoveswScore]
    ReturnValue[3] = q.queue

    if len(AllMoves)==0 or len(PlayerPositions)==0:
        ReturnValue[0] = False
    else:
        ReturnValue[0] = True 

    return ReturnValue

# print(chessPlayer(InitializedBoard,10))