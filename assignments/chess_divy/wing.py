def genBoard():
    board=[0]*64
    board[0]=13
    board[1]=11
    board[2]=12
    board[3]=15
    board[4]=14
    board[5]=12
    board[6]=11
    board[7]=13
    
    for i in range(0,8,1):
            board[i+8]=10
            board[i+48]=20

    board[56]=23
    board[57]=21
    board[58]=22
    board[59]=25
    board[60]=24
    board[61]=22
    board[62]=21
    board[63]=23
    return board

def printBoard(board):
    bored=[]
    for i in range(0,8,1):
        for h in range(0,8,1):
           if (i%2==0) and (h%2==0):
               bored+=["#"]
           elif(h%2==1)and(i%2==0):
               bored+=["_"]
           elif(h%2==0)and(i%2==1):
               bored+=["_"]
           elif[h%2==1]and[i%2==0]:
               bored+=["#"]
    for i in range(0,64,1):
        if board[i]==10:
            bored[i]="p"
        elif board[i]==11:
            bored[i]="n"
        elif board[i]==12:
            bored[i]="b"
        elif board[i]==13:
            bored[i]="r"
        elif board[i]==14:
            bored[i]="q"
        elif board[i]==15:
            bored[i]="k"
        elif board[i]==20:
            bored[i]="P"
        elif board[i]==21:
            bored[i]="N"
        elif board[i]==22:
            bored[i]="B"
        elif board[i]==23:
            bored[i]="R"
        elif board[i]==24:
            bored[i]="Q"
        elif board[i]==25:
            bored[i]="K"

    i=7
    while i>=0:
        for j in range(7,-1,-1):
            print(bored[i*8 + j], end = " ")
        print("      ", end = " ")
        for h in range(7,-1,-1):
            if(i*8 + h)>9:
                print((i*8 + h), end = " ")
            else:
                print(str(i*8 + h) + " ", end = " ")
        print("")
        i=i-1
    bored=[]

def GetPlayerPositions(board,player):
    cum=[]
    for i in range(0,64,1):
        if (board[i]>=player) and (board[i]<=(player+5)):
            cum+=[i]
    if player>10 or player<10:
        if player !=20:
            cum =[]
    return cum

def IsOnBoard(pos):
    if (pos>=0) and (pos<64):
        return True
    else:
        return False

def GetPieceLegalMoves(board,position):
    col=position%8
    if position<8:
        row=0
    elif position<16:
        row=1
    elif position<24:
        row=2
    elif position<32:
        row=3
    elif position<40:
        row=4
    elif position<48:
        row=5
    elif position<56:
        row=6
    else:
        row=7
    if board[position]==0:
        return []
    elif board[position]==10:
        return GetMovesWPawn(board,position)
    elif board[position]==20:
        return GetMovesBPawn(board,position)
    elif board[position]==12 or board[position]==22:
        return GetBishopMoves(board,position,col)
    elif board[position]==15 or board[position]==25:
        return GetKingMoves(board,position,col)
    #Knight
    elif board[position]== 21 or board[position]==11:
        return GetKnightMoves(board,position,row,col)
    elif board[position]==13 or board[position]==23:
        return GetRookMoves(board,position,col)
    elif board[position]==14 or board[position]==24:
        return GetBishopMoves(board,position,col) + GetRookMoves(board,position,col)

def GetRookMoves(board,pos,col):
    cum=[]
    up=pos+8
    down=pos-8
    if board[pos]==13 or board [pos]==14:
        enemy=20
    else:
        enemy=10
    for i in range(1,col+1,1):
        if board[pos-i]==0:
            cum+=[pos-i]
        elif (board[pos-i]-enemy)>=0 and (board[pos-i]-enemy)<=5:
            cum+=[pos-i]
            break
        else:
            break
    for i in range(1,8-col,1):
        if board[pos+i]==0:
            cum+=[pos+i]
        elif (board[pos+i]-enemy)>=0 and (board[pos+i]-enemy)<=5:
            cum+=[pos+i]
            break
        else:
            break
    while IsOnBoard(up):
        if board[up]==0:
            cum+=[up]
        elif (board[up]-enemy)>=0 and (board[up]-enemy)<=5:
            cum+=[up]
            break
        else:
            break
        up+=8
    while IsOnBoard(down):
        if board[down]==0:
            cum+=[down]
        elif (board[down]-enemy)>=0 and (board[down]-enemy)<=5:
            cum+=[down]
            break
        else:
            break
        down=down-8
    return cum



def GetBishopMoves(board,pos,col):
    cum=[]
    if board[pos]==12 or board[pos]==14:
        enemy=20
    else:
        enemy=10
    for i in range(1,col+1,1):
        if IsOnBoard(pos+(7*i)):
            if board[pos+(7*i)]==0:
                cum+=[pos+(7*i)]
            elif (board[pos+(7*i)]-enemy)>=0 and (board[pos+(7*i)]-enemy)<=5:
                cum+=[pos+(7*i)]
                break
            else:
                break
    for i in range(1,8-col,1):
        if IsOnBoard(pos+(9*i)):
            if board[pos+(9*i)]==0:
                cum+=[pos+(9*i)]
            elif (board[pos+(9*i)]-enemy)>=0 and (board[pos+(9*i)]-enemy)<=5:
                cum+=[pos+(9*i)]
                break
            else:
                break
    for i in range(1,col+1,1):
        if IsOnBoard(pos-(9*i)):
            if board[pos-(9*i)]==0:
                cum+=[pos-(9*i)]
            elif (board[pos-(9*i)]-enemy)>=0 and (board[pos-(9*i)]-enemy)<=5:
                cum+=[pos-(9*i)]
                break
            else:
                break
    for i in range(1,8-col,1):
        if IsOnBoard(pos-(7*i)):
            if board[pos-(7*i)]==0:
                cum+=[pos-(7*i)]
            elif (board[pos-(7*i)]-enemy)>=0 and (board[pos-(7*i)]-enemy)<=5:
                cum+=[pos-(7*i)]
                break
            else:
                break
    return cum

def GetKingMoves(board,position,col):
    cum=[]
    if board[position]==15:
        enemy=20
    else:
        enemy=10

    if col>0:
        if board[position-1]==0:
            cum+=[position-1]
        elif (board[position-1]-enemy)>=0 and (board[position-1]-enemy)<=5:
            cum+=[position-1]
    if col<7:
        if board[position+1]==0:
            cum+=[position+1]
        elif (board[position+1]-enemy)>=0 and (board[position+1]-enemy)<=5:
            cum+=[position+1]
    for i in range(0,3,1):
        if IsOnBoard(position+7+i):
            if board[position+7+i]==0:
                cum+=[position+7+i]
            elif (board[position+7+i]-enemy)>=0 and (board[position+7+i]-enemy)<=5:
                cum+=[position+7+i]
    for i in range(0,3,1):
        if IsOnBoard(position-7-i):
            if board[position-7-i]==0:
                cum+=[position-7-i]
            elif (board[position-7-i]-enemy)>=0 and (board[position-7-i]-enemy)<=5:
                cum+=[position-7-i]
    return cum
def GetKnightMoves(board,position,row,col):
    cum=[]
    if board[position]==21:
        enemy=10
    else:
        enemy=20
    if col>0:
        if IsOnBoard(position+15):
            if board[position+15]==0:
                cum+=[position+15]
            elif (board[position+15]-enemy)>=0 and(board[position+15]-enemy<=5):
                cum+=[position+15]
        if IsOnBoard(position-17):
            if board[position-17]==0:
                cum+=[position-17]
            elif (board[position-17]-enemy)>=0 and(board[position-17]-enemy)<=5:
                cum+=[position-17]
    if col>1:
        if IsOnBoard(position+6):
            if board[position + 6] == 0:
                cum += [position + 6]
            elif (board[position + 6] - enemy) >= 0 and (board[position + 6]-enemy) <= 5:
                cum += [position + 6]
        if IsOnBoard(position - 10):
            if board[position - 10] == 0:
                cum += [position - 10]
            elif (board[position - 10] - enemy) >= 0 and (board[position - 10]-enemy) <= 5:
                cum += [position - 10]
    if col<6:
        if IsOnBoard(position+10):
            if board[position + 10] == 0:
                cum += [position + 10]
            elif (board[position + 10] - enemy) >= 0 and (board[position + 10]-enemy) <=5:
                cum += [position+10]
        if IsOnBoard(position - 6):
            if board[position-6] == 0:
                cum += [position - 6]
            elif ((board[position-6] -enemy) >= 0) and ((board[position - 6] - enemy) <= 5):
                cum+=[position - 6]
    if col<7:
        if IsOnBoard(position+17):
            if board[position + 17] == 0:
                cum += [position + 17]
            elif (board[position + 17] - enemy) >= 0 and (board[position + 17]-enemy) <=5:
                cum += [position+17]
        if IsOnBoard(position - 15):
            if board[position-15] == 0:
                cum += [position - 15]
            elif ((board[position-15] -enemy) >= 0) and ((board[position - 15] - enemy) <= 5):
                cum+=[position - 15]

    return cum

    #White Pawn
def GetMovesWPawn(board,position):
    cum=[]
    enemy=20
    if position > 55:
            return []
    else:
        if IsOnBoard(position+8):
            if board[position+8]==0:
                cum+=[position+8]
        if (position+1)%8!=0:
            if (board[position + 9]-enemy)<=5 and (board[position+9]-enemy)>=0:
                cum+=[position+9]
        if (position)%8!=0:
            if (board[position + 7]-enemy)>=0 and (board[position+7]-enemy)<=5:
                cum+=[position+7]

        return cum
    #Black Pawn
def GetMovesBPawn(board,position):
    cum=[]
    enemy=10
    if position<8:
        return []
    else:
        if IsOnBoard(position-8):
            if board[position-8]==0:
                cum+=[position-8]
        if (position+1)%8!=0:
            if (board[position - 7]-enemy)<=5 and (board[position-7]-enemy)>=0:
                cum+=[position-7]
        if (position)%8!=0:
            if (board[position -9]-enemy)<=5 and (board[position-9]-enemy)>=0:
                cum+=[position-9]
        return cum

def IsPositionUnderThreat(board,pos,player):
    cum=[]
    if player==10:
        op=20
    else:
        op=10
    enemy=GetPlayerPositions(board,op)
    for i in enemy:
        cum+=GetPieceLegalMoves(board,i)
    for i in range(0,len(cum),1):
        if pos==cum[i]:
            return True
    return False

def getPieceVal(board,pos):
    if board[pos]==10 or board[pos]==20:
        return 10.0
    elif board[pos]==11 or board[pos]==21:
        return 30.0
    elif board[pos]==12 or board[pos]==22:
        return 30.0
    elif board[pos]==23 or board[pos]==13:
        return 50.0
    elif board[pos]==24 or board[pos]==14:
        return 100.0
    elif board[pos]==15 or board[pos]==25:
        return 900.0
    else:
        return 0

def maximum(poop):
    val=0.0
    if len(poop)<1:
        return 0.0
    for i in range(0, len(poop)):
        if poop[i]>val:
            val=poop[i]
    return val

def chessPlayer(board,player):
    if player!= 10:
        if player!=20:
            return [False,0,0,0]
    points=[]
    cum=[]
    places = GetPlayerPositions(board, player)
    count=0
    for i in range(0,len(places),1): #for all the possible positions i have
        if len(GetPieceLegalMoves(board,places[i]))>0: #if there are possible moves
            cum+=[[places[i]]]
            points+=[[0.0]]
            mymove1=GetPieceLegalMoves(board,places[i])
            for h in range(0,len(mymove1)):
                board2=list(board)
                board2[mymove1[h]]=board2[cum[count][0]]
                board2[cum[count][0]]=0
                points[count]+=[[0.0]]
                points[count][h+1][0]+= getposval(board2,mymove1[h]) - getposval(board,cum[count][0])
                if board2[mymove1[h]]!=0:
                    points[count][h+1][0]+= getPieceVal(board,mymove1[h])
                L = GetPlayerPositions(board2,player)
                accum=[]
                cumshot=[]
                for y in range(0, len(places)):
                    if IsPositionUnderThreat(board,places[y],player):
                        cumshot+=[getPieceVal(board,places[y])]
                for y in range(0, len(L)):
                    if IsPositionUnderThreat(board2,L[y],player):
                        accum+=[getPieceVal(board2, L[y])]
                points[count][h+1][0]-= (maximum(accum)+maximum(cumshot))

                cum[count]+=[[mymove1[h]]]

            count+=1

    candidates=[]
    evalT=[]
    top=-10000.0
    mark=0
    for i in range(0,len(cum)):
        for g in range(1,len(cum[i])):
            candidates+=[[[cum[i][0],cum[i][g][0]],points[i][g][0]]]
            evalT+=[[cum[i][0],cum[i][g][0]]]
    for i in range(0,len(candidates)):
        if candidates[i][1]>top:

            top=candidates[i][1]
            mark=i
    move=candidates[mark][0]
    return [True,move,candidates,evalT]

def getposval(board,pos):
    if board[pos]== 15 or board[pos]==25:
        val = [2.0, 3.0, 1.0, 0.0, 0.0, 1.0, 3.0, 2.0, \
            2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0, \
             -1.0,-2.0,-2.0,-2.0,-2.0,-2.0,-2.0,1.0, \
             -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0, \
             -3.0, -4.0, -4.0, -5.0, -5.0, -4.0 ,-4.0, -3.0, \
             -3.0, -4.0, -4.0, -5.0, -5.0, -4.0 ,-4.0, -3.0, \
             -3.0, -4.0, -4.0, -5.0, -5.0, -4.0 ,-4.0, -3.0, \
             -3.0, -4.0, -4.0, -5.0, -5.0, -4.0 ,-4.0, -3.0]
        if board[pos]==15:
            return val[pos]
        else:
            return val[63-pos]
    elif board[pos]==13 or board[pos]==23:
        val = [0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0, \
         -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5, \
         -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5, \
         -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5, \
         -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5, \
         -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5, \
         0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, \
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        if board[pos]==13:
            return val[pos]
        else:
            return val[63-pos]
    elif board[pos]==11 or board[pos]==21:
        val=[-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0, \
         -4.0, -2.0, 0.0, 0.5, 0.5, 0.0, -2.0, -4.0, \
         -3.0, 0.5, 1.0, 1.5, 1.5, 1.0, 0.5, -3.0, \
         -3.0, 0.0, 1.5, 2.0, 2.0, 1.5, 0.0, -3.0, \
         -3.0, 0.5, 1.5, 2.0, 2.0, 1.5, 0.5, -3.0, \
         -3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0, \
         -4.0, -2.0, 0.0, 0.0, 0.0, 0.0, -2.0, -4.0, \
         -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]
        if board[pos]==11:
            return val[pos]
        else:
            return val[63-pos]
    elif board[pos]==24 or board[pos]==14:
        val = [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0, \
         -1.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, -1.0, \
         -1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0, \
         0.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5, \
         -0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5, \
         -1.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0, \
         -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, \
        -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]
        if board[pos]==14:
            return val[pos]
        else:
            return val[63-pos]
    elif board[pos]==12 or board[pos]==22:
        val = [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0, \
         -1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, -1.0, \
         -1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0, \
         -1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.0, \
         -1.0, 0.5, 0.5, 1.0, 1.0, 0.5, 0.5, -1.0, \
         -1.0, 0.0, 0.5, 1.0, 1.0, 0.5, 0.0, -1.0, \
         -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, \
         -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]
        if board[pos]==12:
            return val[pos]
        else:
            return val[63-pos]
    elif board[pos]==10 or board[pos]==20:
        val = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, \
         0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5, \
         0.5, -0.5, -1.0, 0.0, 0.0, -1.0, -0.5, 0.5, \
         0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0, \
         0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5, \
         1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0, \
         5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, \
         10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0]
        if board[pos]==10:
            return val[pos]
        else:
            return val[63-pos]
    else:
        return 0.0




def playchess():
    board=genBoard()
    printBoard(board)
    done=False
    wvalid=False
    bvalid=False
    while not(done):
        while not(wvalid):
            white=input("Enter Valid White Move: ")
            if len(white)==4:
                pos=int(white[0]+white[1])
                move=int(white[2]+white[3])
                if (board[pos]-10)>=0 and (board[pos]-10)<=5:
                    legal=GetPieceLegalMoves(board,pos)
                    for i in range(0,len(legal),1):
                        if move==legal[i]:
                            board[move]=board[pos]
                            board[pos]=0
                            wvalid = True
                            break
        wvalid=False
        printBoard(board)
        while not(bvalid):
            beep=chessPlayer(board,20)
            pos=beep[1][0]
            move=beep[1][1]
            print(beep)
           # black=input("Enter Valid Black Move: ")
           # if len(black)==4:
              #  pos=int(black[0]+black[1])
               # move=int(black[2]+black[3])
            if (board[pos]-20)>=0 and (board[pos]-20)<=5:
                legal=GetPieceLegalMoves(board,pos)
                for i in range(0,len(legal),1):
                    if move==legal[i]:
                        board[move]=board[pos]
                        board[pos]=0
                        bvalid=True

        printBoard(board)
        bvalid=False
    return True

x=genBoard()
x[48]=13
print(GetPieceLegalMoves(x,55))