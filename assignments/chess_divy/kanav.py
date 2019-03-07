def getPiece(name):
   if name=="pawn":
      return 0
   elif name=="knight":
      return 1
   elif name=="bishop":
      return 2
   elif name=="rook":
      return 3
   elif name=="queen":
      return 4
   elif name=="king":
      return 5
   else:
      return -1


def genBoard():
   board=[0]*64
   White=10
   Black=20
   for i in [ White, Black ]:
      if i==White:
         factor=+1
         shift=0
      else:
         factor=-1
         shift=63

      board[shift+factor*7] = board[shift+factor*0] = i+getPiece("rook")
      board[shift+factor*6] = board[shift+factor*1] = i+getPiece("knight")
      board[shift+factor*5] = board[shift+factor*2] = i+getPiece("bishop")
      if i==White:
         board[shift+factor*4] = i+getPiece("queen") # queen is on its own color square
         board[shift+factor*3] = i+getPiece("king")
      else:
         board[shift+factor*3] = i+getPiece("queen") # queen is on its own color square
         board[shift+factor*4] = i+getPiece("king")

      for j in range(0,8):
         board[shift+factor*(j+8)] = i+getPiece("pawn")

   return board


def printBoard(board):
   accum="------------ BLACK SIDE ------------- \n"
   max=63
   for j in range(0,8,1):
      for i in range(max-j*8,max-j*8-8,-1):
         accum=accum+'{0: <5}'.format(board[i])
      accum=accum+"\n"
   accum=accum+"------------ WHITE SIDE ------------- \n"
   return accum

   def GetPlayerPositions(board,player):
    w=10
    b=20
    accum=[]
    a=0
    if (player == w or player == b):
        for i in board:
            if  ((i>=player) and (i<player + 6)):
                accum+= [a]
            a+=1
    return accum 
def GetPlayerPositions(board,player):
    w=10
    b=20
    accum=[]
    a=0
    if (player == w or player == b):
        for i in board:
            if  ((i>=player) and (i<player + 6)):
                accum+= [a]
            a+=1
    return accum 

def IsOnBoard(pos):
   if (pos >= 0) and (pos <= 63):
      return True
   else:
      return False

def IsEmpty(board,pos):
    
    if board[pos]==0:
        return True 
    else:
        return False 

def IsAttack(board,pos,player):
    a=board[pos]
    w=[10,11,12,13,14,15]
    b=[20,21,22,23,24,25]

    if player == 10:
        for i in b:
            if a==i:
                return True 
    else:
        for i in w:
            if a==i:
                return True 
    return False 

#ROOK
def GetRookMoves(board,pos,player):
    accum=[]
    nr = pos%8
    nl = 7-nr
    nd= int(pos/8)
    nu=7-nd
    r=pos-1
    l=pos+1
    u=pos+8
    d=pos-8
   
    for i in range(0,nr):
        if IsEmpty(board,r):
          if (r!= pos): 
            accum+=[r] 
        elif IsAttack(board,r,player):
            accum+=[r]
            break 
        else:
            break 
       
        r-=1

        
    for i in range(0,nl):
        if IsEmpty(board,l):
          if (l!= pos): 
            accum+=[l] 
        elif IsAttack(board,l,player):
            accum+=[l]
            break 
        else:
            break 
        l+=1
    for i in range(0,nu):
        if IsEmpty(board,u):
          if (u!= pos): 
            accum+=[u] 
        elif IsAttack(board,u,player):
            accum+=[u]
            break 
        else:
            break 
        u+=8
    for i in range(0,nd):
        if IsEmpty(board,d):
          if (d!= pos): 
            accum+=[d] 
        elif IsAttack(board,d,player):
            accum+=[d]
            break 
        else:
            break
        d-=8
    return accum 

#PAWN 
def GetPawnMoves(board,pos,player):
    accum=[]
    if player == 10:
        move=[pos+8]
        moves=[pos+9,pos+7]
    else:
        move=[pos-8]
        moves=[pos-9,pos-7]
    for i in move:
        if IsEmpty(board,i):
            accum+=[i]
        else:
            break
    for i in moves:
        if IsAttack(board,i,player):
            accum+=[i]
        
    return accum 

#king 
def GetKingMoves(board,pos,player):
    accum=[]
    moves=[pos-1,pos+1,pos-8,pos+8,pos+7,pos+9,pos-7,pos-9]
    for i in moves:
        if IsOnBoard(i) and IsEmpty(board,i):
            accum+=[i]
        elif IsOnBoard(i) and IsAttack(board,i,player):
            accum+=[i]
    return accum 

#BISHOP

def GetBishopMoves(board,pos,player):
   nr = pos % 8
   nl = 7 - (pos % 8)
   accum=[]
   ul = pos
   ll = pos
   ur = pos
   lr = pos
   for i in range(0,nr,1):
     
      lr -= 9
      if IsOnBoard(lr):
        if IsEmpty(board,lr):
          accum += [lr]
    
        elif IsAttack(board,lr,player):
          accum+=[lr]
          break 
        else:
          break 
   for i in range(0,nr,1):
      ur += 7
      if IsOnBoard(ur):
        if IsEmpty(board,ur):
          accum += [ur]
    
        elif IsAttack(board,ur,player):
          accum+=[ur]
          break 
        else:
          break 
      
   for i in range(0,nl,1):
      ul+= 9
      if IsOnBoard(ul):
        if IsEmpty(board,ul):
          accum += [ul]
    
        elif IsAttack(board,ul,player):
          accum+=[ul]
          break 
        else:
          break 
     
   for i in range(0,nl,1):
      ll-=7
      if IsOnBoard(ll):
        if IsEmpty(board,ll):
          accum += [ll]
    
        elif IsAttack(board,ll,player):
          accum+=[ll]
          break 
        else:
          break 
   return accum

#knight 
def GetKnightMoves(board,pos,player):
    accum=[]
    init = [0]*2
    fin = [0]*2
    init[0] = pos % 8
    init[1] = int(pos / 8)
    for v in range(0, 64):
        fin[0] = v % 8
        fin[1] = int(v / 8)
        diffx = abs(init[0] - fin[0])
        diffy = abs(init[1] - fin[1])
        if str(board[v])[0] != str(player)[0]:
            if diffx == 2 and diffy == 1:
                accum = accum + [v]
            elif diffy == 2 and diffx == 1:
                accum = accum + [v]
    return accum

#Queen
def GetQueenMoves(board,pos,player):
   return GetRookMoves(board,pos,player) + GetBishopMoves(board,pos,player)

def GetPieceLegalMoves(board,pos):
    accum=[]
    a=board[pos]
 
    if a>19:
        player=20
    else:
        player=10
    if a==10 or a==20:
        #pawn
      accum=GetPawnMoves(board,pos,player)
    elif a==11 or a==21:
        #knight
      accum=GetKnightMoves(board,pos,player)
    elif a==12 or a==22:
        #bishop
      accum=GetBishopMoves(board,pos,player)
    elif a==13 or a==23:
        #rook
      accum=GetRookMoves(board,pos,player)
    elif a==14 or a==24:
        #queen
      accum=GetQueenMoves(board,pos,player)
    elif a==15 or a==25:
        #king
      accum=GetKingMoves(board,pos,player)
    else:
        return []
    return accum

def IsPositionUnderThreat(board,position,player):
    accum=[]
    if player==10:
      a=GetPlayerPositions(board,20)
    else:
      a=GetPlayerPositions(board,10)
    for i in a:
        accum+=GetPieceLegalMoves(board,i)
    for k in accum:
        if position==k:
            return True 
    return False

class tree:
    def __init__(self, x,move):
        self.store = [x, []]
        self.move=move

    def AddSuccessor(self, x):
        self.store[1] = self.store[1] + [x]
        return True
    
def score(board):
   sum=0
   W= GetPlayerPositions(board,10)
   B= GetPlayerPositions(board,20)
   for i in W:
       if board[i]==10:
           sum+=5
       elif board[i]==11:
           sum+=5
       elif board[i]==12:
           sum+=10
       elif board[i]==13:
           sum+=10
       elif board[i]==14:
           sum+=15
       elif board[i]==15:
           sum+=20
   for i in B:
       if board[i]==20:
           sum-=5
       elif board[i]==21:
           sum-=5
       elif board[i]==22:
           sum-=10
       elif board[i]==23:
           sum-=10
       elif board[i]==24:
           sum-=15
       elif board[i]==25:
           sum-=20
   return sum 

def candidatemoves(board,pos):
    l=[]
    
    l=GetPieceLegalMoves(board,pos)
    
    return l

def updateboard(board,player,pos):
   a=GetPieceLegalMoves(board,pos)
   b=0
   for i in a:
       b=board[pos]
       board[i]=b
       board[pos]=0
    

  
            
            
def chessPlayer(board,player):
    nb1=list(board)
    s=score(nb1)
    status=0

    v=GetPlayerPositions(board,player)
    a=tree(s,[])
    x=0
    c=[]
    for i in v:
        nb=list(board)
        b=candidatemoves(board,i)
        x=board[i]

        for k in b:
            board[k]=x
            board[i]=0
            q=tree(score(board),[i,k])
            a.AddSuccessor(q)
    if player ==10:
        b=[]
        c=0
        p=[]
        for t in a.store[1]:
            if c==0:
              b=t
              p+=[t.move,t.store[0]]
            else:
              if t.store[0]>b.store[0]:
                  b=t
              p+=[t.move,t.store[0]]
            c+=1
    
    elif player ==20:
        b=[]
        c=0
        p=[]
        for t in a.store[1]:
            if c==0:
              b=t
              p+=[t.move,t.store[0]]
            else:
              if t.store[0]<b.store[0]:
                  b=t
              p+=[t.move,t.store[0]]
            c+=1
        
    move=b.move
    q=[[[-1,-1],s]]
    q+=list(p)    
    
    if len(move)!=2:
        status = False 
    else:
        status=True
    return [status,move,p,q]
    








def getPiece(name):
   if name=="pawn":
      return 0
   elif name=="knight":
      return 1
   elif name=="bishop":
      return 2
   elif name=="rook":
      return 3
   elif name=="queen":
      return 4
   elif name=="king":
      return 5
   else:
      return -1


def genBoard():
   board=[0]*64
   White=10
   Black=20
   for i in [ White, Black ]:
      if i==White:
         factor=+1
         shift=0
      else:
         factor=-1
         shift=63

      board[shift+factor*7] = board[shift+factor*0] = i+getPiece("rook")
      board[shift+factor*6] = board[shift+factor*1] = i+getPiece("knight")
      board[shift+factor*5] = board[shift+factor*2] = i+getPiece("bishop")
      if i==White:
         board[shift+factor*4] = i+getPiece("queen") # queen is on its own color square
         board[shift+factor*3] = i+getPiece("king")
      else:
         board[shift+factor*3] = i+getPiece("queen") # queen is on its own color square
         board[shift+factor*4] = i+getPiece("king")

      for j in range(0,8):
         board[shift+factor*(j+8)] = i+getPiece("pawn")

   return board


def printBoard(board):
   accum="------------ BLACK SIDE ------------- \n"
   max=63
   for j in range(0,8,1):
      for i in range(max-j*8,max-j*8-8,-1):
         accum=accum+'{0: <5}'.format(board[i])
      accum=accum+"\n"
   accum=accum+"------------ WHITE SIDE ------------- \n"
   return accum

   def GetPlayerPositions(board,player):
    w=10
    b=20
    accum=[]
    a=0
    if (player == w or player == b):
        for i in board:
            if  ((i>=player) and (i<player + 6)):
                accum+= [a]
            a+=1
    return accum 
def GetPlayerPositions(board,player):
    w=10
    b=20
    accum=[]
    a=0
    if (player == w or player == b):
        for i in board:
            if  ((i>=player) and (i<player + 6)):
                accum+= [a]
            a+=1
    return accum 

def IsOnBoard(pos):
   if (pos >= 0) and (pos <= 63):
      return True
   else:
      return False

def IsEmpty(board,pos):
    
    if board[pos]==0:
        return True 
    else:
        return False 

def IsAttack(board,pos,player):
    a=board[pos]
    w=[10,11,12,13,14,15]
    b=[20,21,22,23,24,25]

    if player == 10:
        for i in b:
            if a==i:
                return True 
    else:
        for i in w:
            if a==i:
                return True 
    return False 

#ROOK
def GetRookMoves(board,pos,player):
    accum=[]
    nr = pos%8
    nl = 7-nr
    nd= int(pos/8)
    nu=7-nd
    r=pos-1
    l=pos+1
    u=pos+8
    d=pos-8
   
    for i in range(0,nr):
        if IsEmpty(board,r):
          if (r!= pos): 
            accum+=[r] 
        elif IsAttack(board,r,player):
            accum+=[r]
            break 
        else:
            break 
       
        r-=1

        
    for i in range(0,nl):
        if IsEmpty(board,l):
          if (l!= pos): 
            accum+=[l] 
        elif IsAttack(board,l,player):
            accum+=[l]
            break 
        else:
            break 
        l+=1
    for i in range(0,nu):
        if IsEmpty(board,u):
          if (u!= pos): 
            accum+=[u] 
        elif IsAttack(board,u,player):
            accum+=[u]
            break 
        else:
            break 
        u+=8
    for i in range(0,nd):
        if IsEmpty(board,d):
          if (d!= pos): 
            accum+=[d] 
        elif IsAttack(board,d,player):
            accum+=[d]
            break 
        else:
            break
        d-=8
    return accum 

#PAWN 
def GetPawnMoves(board,pos,player):
    accum=[]
    if player == 10:
        move=[pos+8]
        moves=[pos+9,pos+7]
    else:
        move=[pos-8]
        moves=[pos-9,pos-7]
    for i in move:
        if IsEmpty(board,i):
            accum+=[i]
        else:
            break
    for i in moves:
        if IsAttack(board,i,player):
            accum+=[i]
        
    return accum 

#king 
def GetKingMoves(board,pos,player):
    accum=[]
    moves=[pos-1,pos+1,pos-8,pos+8,pos+7,pos+9,pos-7,pos-9]
    for i in moves:
        if IsOnBoard(i) and IsEmpty(board,i):
            accum+=[i]
        elif IsOnBoard(i) and IsAttack(board,i,player):
            accum+=[i]
    return accum 

#BISHOP

def GetBishopMoves(board,pos,player):
   nr = pos % 8
   nl = 7 - (pos % 8)
   accum=[]
   ul = pos
   ll = pos
   ur = pos
   lr = pos
   for i in range(0,nr,1):
     
      lr -= 9
      if IsOnBoard(lr):
        if IsEmpty(board,lr):
          accum += [lr]
    
        elif IsAttack(board,lr,player):
          accum+=[lr]
          break 
        else:
          break 
   for i in range(0,nr,1):
      ur += 7
      if IsOnBoard(ur):
        if IsEmpty(board,ur):
          accum += [ur]
    
        elif IsAttack(board,ur,player):
          accum+=[ur]
          break 
        else:
          break 
      
   for i in range(0,nl,1):
      ul+= 9
      if IsOnBoard(ul):
        if IsEmpty(board,ul):
          accum += [ul]
    
        elif IsAttack(board,ul,player):
          accum+=[ul]
          break 
        else:
          break 
     
   for i in range(0,nl,1):
      ll-=7
      if IsOnBoard(ll):
        if IsEmpty(board,ll):
          accum += [ll]
    
        elif IsAttack(board,ll,player):
          accum+=[ll]
          break 
        else:
          break 
   return accum

#knight 
def GetKnightMoves(board,pos,player):
    accum=[]
    init = [0]*2
    fin = [0]*2
    init[0] = pos % 8
    init[1] = int(pos / 8)
    for v in range(0, 64):
        fin[0] = v % 8
        fin[1] = int(v / 8)
        diffx = abs(init[0] - fin[0])
        diffy = abs(init[1] - fin[1])
        if str(board[v])[0] != str(player)[0]:
            if diffx == 2 and diffy == 1:
                accum = accum + [v]
            elif diffy == 2 and diffx == 1:
                accum = accum + [v]
    return accum

#Queen
def GetQueenMoves(board,pos,player):
   return GetRookMoves(board,pos,player) + GetBishopMoves(board,pos,player)

def GetPieceLegalMoves(board,pos):
    accum=[]
    a=board[pos]
 
    if a>19:
        player=20
    else:
        player=10
    if a==10 or a==20:
        #pawn
      accum=GetPawnMoves(board,pos,player)
    elif a==11 or a==21:
        #knight
      accum=GetKnightMoves(board,pos,player)
    elif a==12 or a==22:
        #bishop
      accum=GetBishopMoves(board,pos,player)
    elif a==13 or a==23:
        #rook
      accum=GetRookMoves(board,pos,player)
    elif a==14 or a==24:
        #queen
      accum=GetQueenMoves(board,pos,player)
    elif a==15 or a==25:
        #king
      accum=GetKingMoves(board,pos,player)
    else:
        return []
    return accum

def IsPositionUnderThreat(board,position,player):
    accum=[]
    if player==10:
      a=GetPlayerPositions(board,20)
    else:
      a=GetPlayerPositions(board,10)
    for i in a:
        accum+=GetPieceLegalMoves(board,i)
    for k in accum:
        if position==k:
            return True 
    return False

class tree:
    def __init__(self, x,move):
        self.store = [x, []]
        self.move=move

    def AddSuccessor(self, x):
        self.store[1] = self.store[1] + [x]
        return True
    
def score(board):
   sum=0
   W= GetPlayerPositions(board,10)
   B= GetPlayerPositions(board,20)
   for i in W:
       if board[i]==10:
           sum+=5
       elif board[i]==11:
           sum+=5
       elif board[i]==12:
           sum+=10
       elif board[i]==13:
           sum+=10
       elif board[i]==14:
           sum+=15
       elif board[i]==15:
           sum+=20
   for i in B:
       if board[i]==20:
           sum-=5
       elif board[i]==21:
           sum-=5
       elif board[i]==22:
           sum-=10
       elif board[i]==23:
           sum-=10
       elif board[i]==24:
           sum-=15
       elif board[i]==25:
           sum-=20
   return sum 

def candidatemoves(board,pos):
    l=[]
    
    l=GetPieceLegalMoves(board,pos)
    
    return l

def updateboard(board,player,pos):
   a=GetPieceLegalMoves(board,pos)
   b=0
   for i in a:
       b=board[pos]
       board[i]=b
       board[pos]=0
    

  
            
            
def chessPlayer(board,player):
    nb1=list(board)
    s=score(nb1)
    status=0

    v=GetPlayerPositions(nb1,player)
    a=tree(s,[])
    x=0
    c=[]
    for i in v:
        b=candidatemoves(nb1,i)
        for k in b:
            nb=list(board)
            x=nb[i]
            nb[k]=x
            nb[i]=0
            q=tree(score(nb),[i,k])
            a.AddSuccessor(q)
    if player ==10:
        b=[]
        c=0
        p=[]
        for t in a.store[1]:
            if c==0:
              b=t
              p+=[t.move,t.store[0]]
            else:
              if t.store[0]>b.store[0]:
                  b=t
              p+=[t.move,t.store[0]]
            c+=1
    
    elif player ==20:
        b=[]
        c=0
        p=[]
        for t in a.store[1]:
            if c==0:
              b=t
              p+=[t.move,t.store[0]]
            else:
              if t.store[0]<b.store[0]:
                  b=t
              p+=[t.move,t.store[0]]
            c+=1
        
    move=b.move
    q=[[[-1,-1],s]]
    q+=list(p)    
    
    if len(move)!=2:
        status = False 
    else:
        status=True
    return [status,move,p,q]
    








   
