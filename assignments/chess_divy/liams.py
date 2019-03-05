def genBoard():
   # generate the board
   board = [0]*64
   # initialize colour offsets
   White = 10
   Black = 20
   # initialize piece values
   pawn = 0
   knight = 1
   bishop = 2
   rook = 3
   queen = 4
   king = 5
   # set pieces on board
   for i in [White,Black]:
      if i == White:
         starting = 0
         direction = 1
      else:
         starting = 63
         direction = -1

      board[starting] = board[starting + direction*7] = i+rook
      board[starting + direction] = board[starting + direction*6] = i+knight
      board[starting + direction*2] = board[starting + direction*5] = i+bishop

      if i == White:
         board[starting + direction*3] =  i+king
         board[starting + direction*4] = i+queen
      else:
         board[starting + direction*3] = i+queen
         board[starting + direction*4] = i+king

      for j in range(0,8,1):
         board[starting + direction*(j+8)] = i+pawn

   return board

def printBoard(board):
   # create blank board positions
   wfirst = ['#','_','#','_','#','_','#','_']
   bfirst = ['_','#','_','#','_','#','_','#']
   # place the appropriate pieces on the board
   printboard = wfirst + bfirst + wfirst + bfirst + wfirst + bfirst + wfirst + bfirst
   for i in range(0,64,1):
      if board[i] == 10:
         printboard[63-i] = 'p'
      if board[i] == 20:
         printboard[63-i] = 'P'
      if board[i] == 11:
         printboard[63-i] = 'k'
      if board[i] == 21:
         printboard[63-i] = 'K'
      if board[i] == 12:
         printboard[63-i] = 'b'
      if board[i] == 22:
         printboard[63-i] = 'B'
      if board[i] == 13:
         printboard[63-i] = 'r'
      if board[i] == 23:
         printboard[63-i] = 'R'
      if board[i] == 14:
         printboard[63-i] = 'q'
      if board[i] == 24:
         printboard[63-i] = 'Q'
      if board[i] == 15:
         printboard[63-i] = 'w'
      if board[i] == 25:
         printboard[63-i] = 'W'

   # print the board out
   accum = []
   print(" Black ")
   for j in range(0,8,1):
      for k in range(0,8,1):
         accum = accum + [printboard[k+8*j]]
      print(accum[0]+' '+accum[1]+' '+accum[2]+' '+accum[3]+' '+accum[4]+' '+accum[5]+' '+accum[6]+' '+accum[7])
      accum = []
   print(" White ")
   return True

def GetPlayerPositions(board,player):
   # return list of positions player occupies
   if type(board) != list:
      print("Board Faulty: Type")
      return []
   if len(board) != 64:
      print("Board Faulty: Size")
      return []
   accum = []
   if player == 10:
      for i in range(0,64,1):
         if (board[i] == 10 or board[i] == 11 or board[i] == 12 or board[i] == 13 or board[i] == 14 or board[i] == 15):
             accum = accum + [i]
      return accum
   elif player == 20:
      for i in range(0,64,1):
         if (board[i] == 20 or board[i] == 21 or board[i] == 22 or board[i] == 23 or board[i] == 24 or board[i] == 25):
             accum = accum + [i]
      return accum
   else:
      print("Player Not Assigned")
      return []

def outside(position):
   # check if position is on outside of board
   if position < 0:
      print("Position Outside Range: < 0")
      return False
   if position > 63:
      print("Position Outside Range: > 63")
      return False
   outnums = [0,1,2,3,4,5,6,7,15,23,31,39,47,55,63,62,61,60,59,58,57,56,48,40,32,24,16,8]
   for i in range(0,28,1):
      if position == outnums[i]:
         return 1
   return 0

def location(position):
   # determine where on the board the piece is
   location = 'middle'	# by default
   if position == 1 or position == 2 or position == 3 or position == 4 or position == 5 or position == 6:
      location = 'bottom'
   if position == 0:
      location = 'bottom right'
   if position == 7:
      location = 'bottom left'
   if position == 15 or position == 23 or position == 31 or position == 39 or position == 47 or position == 55:
      location = 'left'
   if position == 63:
      location = 'top left'
   if position == 62 or position == 61 or position == 60 or position == 59 or position == 58 or position == 57:
      location = 'top'
   if position == 56:
      location = 'top right'
   if position == 48 or position == 40 or position == 32 or position == 24 or position == 16 or position == 8:
      location = 'right'
   return location

def rookMoves(board,position,piece,place):
   accum = []
   toggle = 0
   cnt = 1
   # determine the enemy
   if piece < 18:
      enemy = 20
   else:
      enemy = 10
   # determine friendlies
   if piece < 18:
      friendly = 10
   else:
      friendly = 20
   # find moves on the left
   if place != 'left' and place != 'top left' and place != 'bottom left':
      while toggle == 0:
         new = board[position+cnt]
         if new == enemy+0 or new == enemy+1 or new == enemy+2 or new == enemy+3 or new == enemy+4 or new == enemy+5:
            accum = accum + [position+cnt]
            toggle = 1
         elif new == friendly+0 or new == friendly+1 or new == friendly+2 or new == friendly+3 or new == friendly+4 or new == friendly+5:
            toggle = 1
         else:
            loc = location(position+cnt)
            if loc == 'left' or loc == 'top left' or loc == 'bottom left':
               accum = accum + [position+cnt]
               toggle = 1
            else:
               accum = accum + [position+cnt]
         cnt = cnt + 1
   # find moves on the right
   toggle = 0
   cnt = 1
   if place != 'right' and place != 'top right' and place != 'bottom right':
      while toggle == 0:
         new = board[position-cnt]
         if new == enemy+0 or new == enemy+1 or new == enemy+2 or new == enemy+3 or new == enemy+4 or new == enemy+5:
            accum = accum + [position-cnt]
            toggle = 1
         elif new == friendly+0 or new == friendly+1 or new == friendly+2 or new == friendly+3 or new == friendly+4 or new == friendly+5:
            toggle = 1
         else:
            loc = location(position-cnt)
            if loc == 'right' or loc == 'top right' or loc == 'bottom right':
               accum = accum + [position-cnt]
               toggle = 1
            else:
               accum = accum + [position-cnt]
         cnt = cnt + 1
   # find moves toward black side
   toggle = 0
   cnt = 1
   if place != 'top' and place != 'top right' and place != 'top left':
      while toggle == 0:
         new = board[position+cnt*8]
         if new == enemy+0 or new == enemy+1 or new == enemy+2 or new == enemy+3 or new == enemy+4 or new == enemy+5:
            accum = accum + [position+cnt*8]
            toggle = 1
         elif new == friendly+0 or new == friendly+1 or new == friendly+2 or new == friendly+3 or new == friendly+4 or new == friendly+5:
            toggle = 1
         else:
            loc = location(position+cnt*8)
            if loc == 'top' or loc == 'top right' or loc == 'top left':
               accum = accum + [position+cnt*8]
               toggle = 1
            else:
               accum = accum + [position+cnt*8]
         cnt = cnt + 1
   # find moves toward white side
   toggle = 0
   cnt = 1
   if place != 'bottom' and place != 'bottom right' and place != 'bottom left':
      while toggle == 0:
         new = board[position-cnt*8]
         if new == enemy+0 or new == enemy+1 or new == enemy+2 or new == enemy+3 or new == enemy+4 or new == enemy+5:
            accum = accum + [position-cnt*8]
            toggle = 1
         elif new == friendly+0 or new == friendly+1 or new == friendly+2 or new == friendly+3 or new == friendly+4 or new == friendly+5:
            toggle = 1
         else:
            loc = location(position-cnt*8)
            if loc == 'top' or loc == 'top right' or loc == 'top left':
               accum = accum + [position-cnt*8]
               toggle = 1
            else:
               accum = accum + [position-cnt*8]
         cnt = cnt + 1
   return accum

def bishopMoves(board,position,piece,place):
   accum = []
   toggle = 0
   cnt = 1
   # determine the enemy
   if piece < 18:
      enemy = 20
   else:
      enemy = 10
   # determine friendlies
   if piece < 18:
      friendly = 10
   else:
      friendly = 20
   # find moves on the left up diagonal
   if place != 'left' and place != 'top left' and place != 'bottom left' and place != 'top' and place != 'top right':
      while toggle == 0:
         new = board[position+cnt*8+cnt]
         if new == enemy+0 or new == enemy+1 or new == enemy+2 or new == enemy+3 or new == enemy+4 or new == enemy+5:
            accum = accum + [position+cnt*8+cnt]
            toggle = 1
         elif new == friendly+0 or new == friendly+1 or new == friendly+2 or new == friendly+3 or new == friendly+4 or new == friendly+5:
            toggle = 1
         else:
            loc = location(position+cnt*8+cnt)
            if loc == 'left' or loc == 'top left' or loc == 'bottom left' or loc == 'top' or loc == 'top right':
               accum = accum + [position+cnt*8+cnt]
               toggle = 1
            else:
               accum = accum + [position+cnt*8+cnt]
         cnt = cnt + 1
   # find moves on the right up diagonal
   toggle = 0
   cnt = 1
   if place != 'right' and place != 'top right' and place != 'bottom right' and place != 'top left' and place != 'top':
      while toggle == 0:
         new = board[position+cnt*8-cnt]
         if new == enemy+0 or new == enemy+1 or new == enemy+2 or new == enemy+3 or new == enemy+4 or new == enemy+5:
            accum = accum + [position+cnt*8-cnt]
            toggle = 1
         elif new == friendly+0 or new == friendly+1 or new == friendly+2 or new == friendly+3 or new == friendly+4 or new == friendly+5:
            toggle = 1
         else:
            loc = location(position+cnt*8-cnt)
            if loc == 'right' or loc == 'top right' or loc == 'bottom right' or loc == 'top left' or loc == 'top':
               accum = accum + [position+cnt*8-cnt]
               toggle = 1
            else:
               accum = accum + [position+cnt*8-cnt]
         cnt = cnt + 1
   # find moves on the left down diagonal
   toggle = 0
   cnt = 1
   if place != 'left' and place != 'top left' and place != 'bottom left' and place != 'bottom' and place != 'bottom right':
      while toggle == 0:
         new = board[position-cnt*8+cnt]
         if new == enemy+0 or new == enemy+1 or new == enemy+2 or new == enemy+3 or new == enemy+4 or new == enemy+5:
            accum = accum + [position-cnt*8+1]
            toggle = 1
         elif new == friendly+0 or new == friendly+1 or new == friendly+2 or new == friendly+3 or new == friendly+4 or new == friendly+5:
            toggle = 1
         else:
            loc = location(position-cnt*8+cnt)
            if loc == 'left' or loc == 'top left' or loc == 'bottom left' or loc == 'bottom' or loc == 'bottom right':
               accum = accum + [position-cnt*8+cnt]
               toggle = 1
            else:
               accum = accum + [position-cnt*8+cnt]
         cnt = cnt + 1
   # find moves on the right down diagonal
   toggle = 0
   cnt = 1
   if place != 'bottom' and place != 'bottom right' and place != 'bottom left' and place != 'right' and place != 'top right':
      while toggle == 0:
         new = board[position-cnt*8-cnt]
         if new == enemy+0 or new == enemy+1 or new == enemy+2 or new == enemy+3 or new == enemy+4 or new == enemy+5:
            accum = accum + [position-cnt*8-cnt]
            toggle = 1
         elif new == friendly+0 or new == friendly+1 or new == friendly+2 or new == friendly+3 or new == friendly+4 or new == friendly+5:
            toggle = 1
         else:
            loc = location(position-cnt*8-cnt)
            if loc == 'bottom' or loc == 'bottom right' or loc == 'bottom left' or loc == 'right' or loc == 'top right':
               accum = accum + [position-cnt*8-cnt]
               toggle = 1
            else:
               accum = accum + [position-cnt*8-cnt]
         cnt = cnt + 1
   return accum

def knightMoves(board,position,piece,place):
   accum = []
   # determine the enemy
   if piece < 18:
      enemy = 20
   else:
      enemy = 10
   # check positioning on the board
   left_up = 1
   left_up_up = 1
   left_down_down = 1
   left_down = 1
   right_up = 1
   right_up_up = 1
   right_down = 1
   right_down_down = 1
   if place == 'left' or place == 'top left' or place == 'bottom left':
      left_up = 0
      left_up_up = 0
      left_down_down = 0
      left_down = 0
   if place == 'right' or place == 'top right' or place == 'bottom right':
      right_up = 0
      right_up_up = 0
      right_down_down = 0
      right_down = 0
   if place == 'top' or place == 'top right' or place == 'top left':
      left_up = 0
      left_up_up = 0
      right_up = 0
      right_up_up = 0
   if place == 'bottom' or place == 'bottom left' or place == 'bottom right':
      left_down = 0
      left_down_down = 0
      right_down = 0
      right_down_down = 0
   test1 = location(position+1)
   test2 = location(position-1)
   test3 = location(position+8)
   test4 = location(position-8)
   if test1 == 'top left' or test1 == 'top right' or test1 == 'bottom left' or test1 == 'bottom right':
      place = 'middle'
   if test2 == 'top left' or test2 == 'top right' or test2 == 'bottom left' or test2 == 'bottom right':
      place = 'middle'
   if test3 == 'top left' or test3 == 'top right' or test3 == 'bottom left' or test3 == 'bottom right':
      place = 'middle'
   if test4 == 'top left' or test4 == 'top right' or test4 == 'bottom left' or test4 == 'bottom right':
      place = 'middle'
   if place == 'middle':
      ltry = location(position+1)
      rtry = location(position-1)
      utry = location(position+8)
      dtry = location(position-8)
      if ltry == 'left' or ltry == 'top left' or ltry == 'bottom left':
         left_up = 0
         left_down = 0
      if rtry == 'right' or rtry == 'top right' or rtry == 'bottom right':
         right_up = 0
         right_down = 0
      if utry == 'top' or utry == 'top left' or utry == 'top right':
         left_up_up = 0
         right_up_up = 0
      if dtry == 'bottom' or dtry == 'bottom left' or dtry == 'bottom right':
         left_down_down = 0
         right_down_down = 0
   if right_up_up == 1:
      hit = board[position+15]
      if hit == enemy+0 or hit == enemy+1 or hit == enemy+2 or hit == enemy+3 or hit == enemy+4 or hit == enemy+5 or hit == 0:
         accum = accum + [position+15]
   if right_up == 1:
      hit = board[position+6]
      if hit == enemy+0 or hit == enemy+1 or hit == enemy+2 or hit == enemy+3 or hit == enemy+4 or hit == enemy+5 or hit == 0:
         accum = accum + [position+6]
   if right_down == 1:
      hit = board[position-10]
      if hit == enemy+0 or hit == enemy+1 or hit == enemy+2 or hit == enemy+3 or hit == enemy+4 or hit == enemy+5 or hit == 0:
         accum = accum + [position-10]
   if right_down_down == 1:
      hit = board[position-17]
      if hit == enemy+0 or hit == enemy+1 or hit == enemy+2 or hit == enemy+3 or hit == enemy+4 or hit == enemy+5 or hit == 0:
         accum = accum + [position-17]
   if left_down_down == 1:
      hit = board[position-15]
      if hit == enemy+0 or hit == enemy+1 or hit == enemy+2 or hit == enemy+3 or hit == enemy+4 or hit == enemy+5 or hit == 0:
         accum = accum + [position-15]
   if left_down == 1:
      hit = board[position-6]
      if hit == enemy+0 or hit == enemy+1 or hit == enemy+2 or hit == enemy+3 or hit == enemy+4 or hit == enemy+5 or hit == 0:
         accum = accum + [position-6]
   if left_up == 1:
      hit = board[position+10]
      if hit == enemy+0 or hit == enemy+1 or hit == enemy+2 or hit == enemy+3 or hit == enemy+4 or hit == enemy+5 or hit == 0:
         accum = accum + [position+10]
   if left_up_up == 1:
      hit = board[position+17]
      if hit == enemy+0 or hit == enemy+1 or hit == enemy+2 or hit == enemy+3 or hit == enemy+4 or hit == enemy+5 or hit == 0:
         accum = accum + [position+17]
   return accum

def kingMoves(board,position,piece,place):
   accum = []
   # determine the enemy
   if piece < 18:
      enemy = 20
   else:
      enemy = 10
   top = 1
   left = 1
   right = 1
   down = 1
   if place == 'top' or place == 'top left' or place == 'top right':
      top = 0
   if place == 'left' or place == 'top left' or place == 'bottom left':
      left = 0
   if place == 'bottom' or place == 'bottom left' or place == 'bottom right':
      down = 0
   if place == 'right' or place == 'top right' or place == 'bottom right':
      right = 0
   if top == 1:
      above = board[position+8]
      if (above == enemy+0 or above == enemy+1 or above == enemy+2 or above == enemy+3 or above == enemy+4 or above == 0):
         accum = accum + [position+8]
   if top == 1 and left == 1:
      ablef = board[position+9]
      if (ablef == enemy+0 or ablef == enemy+1 or ablef == enemy+2 or ablef == enemy+3 or ablef == enemy+4 or ablef == 0 ):
         accum = accum + [position+9]
   if top == 1 and right == 1:
      abrig = board[position+7]
      if (abrig == enemy+0 or abrig == enemy+1 or abrig == enemy+2 or abrig == enemy+3 or abrig == enemy+4 or abrig == 0 ):
         accum = accum + [position+7]
   if left == 1:
      sidlef = board[position+1]
      if (sidlef == enemy+0 or sidlef == enemy+1 or sidlef == enemy+2 or sidlef == enemy+3 or sidlef == enemy+4 or sidlef == 0 ):
         accum = accum + [position+1]
   if right == 1:
      sidrig = board[position-1]
      if (sidrig == enemy+0 or sidrig == enemy+1 or sidrig == enemy+2 or sidrig == enemy+3 or sidrig == enemy+4 or sidrig == 0 ):
         accum = accum + [position-1]
   if down == 1:
      below = board[position-8]
      if (below == enemy+0 or below == enemy+1 or below == enemy+2 or below == enemy+3 or below == enemy+4 or below == 0):
         accum = accum + [position-8]
   if down == 1 and right == 1:
      belrig = board[position-9]
      if (belrig == enemy+0 or belrig == enemy+1 or belrig == enemy+2 or belrig == enemy+3 or belrig == enemy+4 or belrig == 0 ):
         accum = accum + [position-9]
   if down == 1 and left == 1:
      bellef = board[position-7]
      if (bellef == enemy+0 or bellef == enemy+1 or bellef == enemy+2 or bellef == enemy+3 or bellef == enemy+4 or bellef == 0 ):
         accum = accum + [position-7]
   return accum

def GetPieceLegalMoves(board,position):
   # determine position number
   if position < 0:
      print("Position is Not on Board")
      return False
   if position > 63:
      print("Position is Not on Board")
      return False
   piece = board[position]
   # initialize list for possible positions
   accum = []
   # find the location ond outside positions
   out = outside(position) # returns 1 for outside, 0 for middle
   place = location(position) # returns bottom,top,left,right or top/bottom right/left
   # determine moves for the white pawn (white side perspective for )
   if piece == 10:
      if out == 0:
         left = board[position+7]
         right = board[position+9]
         forward = board[position+8]
         if forward == 0:
            accum = accum + [position+8]
         if left == 20 or left == 21 or left == 22 or left == 23 or left == 24 or left == 25:
            accum = accum + [position+7]
         if right == 20 or right == 21 or right == 22 or right == 23 or right == 24 or right == 25:
            accum = accum + [position+9]
      if out == 1:
         if place == 'left':
            right = board[position+9]
            forward = board[position+8]
            if forward == 0:
               accum = accum + [position+8]
            if right == 20 or right == 21 or right == 22 or right == 23 or right == 24 or right == 25:
               accum = accum + [position+9]
         if place == 'right':
            left = board[position+7]
            forward = board[position+8]
            if forward == 0:
               accum = accum + [position+8]
            if left == 20 or left == 21 or left == 22 or left == 23 or left == 24 or left == 25:
               accum = accum + [position+7]

   # determine moves for the black pawn (black side perspective for right/left)
   if piece == 20:
      if out == 0:
         left = board[position-9]
         right = board[position-7]
         forward = board[position-8]
         if forward == 0:
            accum = accum + [position-8]
         if left == 10 or left == 11 or left == 12 or left == 13 or left == 14 or left == 15:
            accum = accum + [position-9]
         if right == 10 or right == 11 or right == 12 or right == 13 or right == 14 or right == 15:
            accum = accum + [position-7]
      if out == 1:
         if place == 'left':
            left = board[position-9]
            forward = board[position-8]
            if forward == 0:
               accum = accum + [position-8]
            if left == 10 or left == 11 or left == 12 or left == 13 or left == 14 or left == 15:
               accum = accum + [position-9]
         if place == 'right':
            right = board[position-7]
            forward = board[position-8]
            if forward == 0:
               accum = accum + [position-8]
            if right == 10 or right == 11 or right == 12 or right == 13 or right == 14 or right == 15:
               accum = accum + [position-7]

   # find moves for the rooks
   if piece == 13 or piece == 23:
      accum = rookMoves(board,position,piece,place)

   # find moves for the bishops
   if piece == 12 or piece == 22:
      accum = bishopMoves(board,position,piece,place)

   # find moves for the queens
   if piece == 14 or piece == 24:
      accum = rookMoves(board,position,piece,place)
      accum = accum + bishopMoves(board,position,piece,place)

   # find moves for the knights
   if piece == 11 or piece == 21:
      accum = knightMoves(board,position,piece,place)

   # find moves for the kings
   if piece == 15 or piece == 25:
      accum = kingMoves(board,position,piece,place)

   return accum

def value(board):
   # sum the pieces on the board (+ for white and - for black)
   sum = 0
   for i in range(0,64,1):
      place = location(i)
      if board[i] == 10:
         sum = sum + 10.0
         if i >= 48 and i <= 55:
            sum = sum + 5.0
         for j in [47,46,41,40,37,34,9,10,13,14]:
            if i == j:
               sum = sum + 1.0
         for j in [8,15,16,23,32,33,38,39]:
            if i == j:
               sum = sum + 0.5
         for j in [43,44]:
            if i == j:
               sum = sum + 3.0
         for j in [35,36]:
            if i == j:
               sum = sum + 2.5
         for j in [27,28,42,45]:
            if i == j:
               sum = sum + 2.0
         for j in [17,22]:
            if i == j:
               sum = sum - 0.5
         for j in [18,21]:
            if i == j:
               sum = sum - 1.0
         for j in [11,12]:
            if i == j:
               sum = sum - 2.0
      if board[i] == 20:
         sum = sum - 10
         if i <= 15 and i >= 8:
            sum = sum - 5.0
         for j in [16,17,22,23,26,29,54,53,50,49]:
            if i == j:
               sum = sum - 1.0
         for j in [55,48,47,40,31,30,25,24]:
            if i == j:
               sum = sum - 0.5
         for j in [20,19]:
            if i == j:
               sum = sum - 3.0
         for j in [28,27]:
            if i == j:
               sum = sum - 2.5
         for j in [36,35,21,18]:
            if i == j:
               sum = sum - 2.0
         for j in [46,41]:
            if i == j:
               sum = sum + 0.5
         for j in [45,42]:
            if i == j:
               sum = sum + 1.0
         for j in [52,51]:
            if i == j:
               sum = sum + 2.0
      if board[i] == 11:
         sum = sum + 30.0
         if place == 'top right' or place == 'top left' or place == 'bottom right' or place == 'bottom left':
            sum = sum - 5.0
         if place == 'left' or place =='right' or place == 'top' or place == 'bottom':
            sum = sum - 3.0
            for j in [1,6,8,15,48,55,57,62]:
               if i == j:
                  sum = sum - 1.0
         for j in [9,14,49,54]:
            if i == j:
               sum = sum - 2.0
         for j in [11,12,17,22,33,38]:
            if i == j:
               sum = sum + 0.5
         for j in [18,21,42,45]:
            if i == j:
               sum = sum + 1.0
         for j in [19,20,26,29,34,37,43,44]:
            if i == j:
               sum = sum + 1.5
         for j in [27,28,35,36]:
            if i == j:
               sum = sum + 2.0
      if board[i] == 21:
         sum = sum - 30
         if place == 'top right' or place == 'top left' or place == 'bottom right' or place == 'bottom left':
            sum = sum + 5.0
         if place == 'left' or place =='right' or place == 'top' or place == 'bottom':
            sum = sum + 3.0
            for j in [1,6,8,15,48,55,57,62]:
               if i == j:
                  sum = sum + 1.0
         for j in [9,14,49,54]:
            if i == j:
               sum = sum + 2.0
         for j in [52,51,46,41,30,25]:
            if i == j:
               sum = sum - 0.5
         for j in [18,21,42,45]:
            if i == j:
               sum = sum - 1.0
         for j in [19,20,26,29,34,37,43,44]:
            if i == j:
               sum = sum - 1.5
         for j in [27,28,35,36]:
            if i == j:
               sum = sum - 2.0
      if board[i] == 12:
         sum = sum + 30
         if place == 'top right' or place == 'top left' or place == 'bottom right' or place == 'bottom left':
            sum = sum - 2.0
         if place == 'left' or place =='right' or place == 'top' or place == 'bottom':
            sum = sum - 1.0
         for j in [17,18,19,20,21,22,26,27,28,29,35,36,43,44]:
            if i == j:
               sum = sum + 1.0
         for j in [9,14,33,34,37,38,42,45]:
            if i == j:
               sum = sum + 0.5
      if board[i] == 22:
         sum = sum - 30
         if place == 'top right' or place == 'top left' or place == 'bottom right' or place == 'bottom left':
            sum = sum + 2.0
         if place == 'left' or place =='right' or place == 'top' or place == 'bottom':
            sum = sum + 1.0
         for j in [46,45,44,43,42,41,37,36,35,34,28,27,20,19]:
            if i == j:
               sum = sum - 1.0
         for j in [54,49,30,29,34,26,25,21,18]:
            if i == j:
               sum = sum - 0.5
      if board[i] == 13:
         sum = sum + 50
         for j in [3,4,48,55]:
            if i == j:
               sum = sum + 0.5
         for j in [49,50,51,52,53,54]:
            if i == j:
               sum = sum + 1.0
         for j in [8,16,24,32,40,7,15,23,31,39]:
            if i == j:
               sum = sum - 0.5
      if board[i] == 23:
         sum = sum - 50
         for j in [60,59,15,8]:
            if i == j:
               sum = sum - 0.5
         for j in [14,13,12,11,10,9]:
            if i == j:
               sum = sum - 1.0
         for j in [55,47,39,31,23,56,48,40,32,24]:
            if i == j:
               sum = sum + 0.5
      if board[i] == 14:
         sum = sum + 90
         if place == 'top right' or place == 'top left' or place == 'bottom right' or place == 'bottom left':
            sum = sum - 2.0
         for j in [3,4,24,32,39,59,60]:
            if i == j:
               sum = sum - 0.5
         for j in [1,2,5,6,8,16,15,23,40,48,47,55,57,58,61,62]:
            if i == j:
               sum = sum - 1.0
         for j in [13,22,18,19,20,21,26,27,28,29,34,35,36,37,42,43,44,45]:
            if i == j:
               sum = sum + 0.5
      if board[i] == 24:
         sum = sum - 90
         if place == 'top right' or place == 'top left' or place == 'bottom right' or place == 'bottom left':
            sum = sum + 2.0
         for j in [3,4,39,31,24,59,60]:
            if i == j:
               sum = sum + 0.5
         for j in [1,2,5,6,8,16,15,23,40,48,47,55,57,58,61,62]:
            if i == j:
               sum = sum + 1.0
         for j in [50,41,18,19,20,21,26,27,28,29,34,35,36,37,42,43,44,45]:
            if i == j:
               sum = sum - 0.5
      if board[i] == 15:
         sum = sum + 900
         for j in [35,36,43,44,51,52,59,60]:
            if i == j:
               sum = sum - 5.0
         for j in [27,28,33,34,41,42,49,50,57,58,37,38,45,46,53,54,61,62]:
            if i == j:
               sum = sum - 4.0
         for j in [25,26,29,30,32,40,48,56,39,47,55,63]:
            if i == j:
               sum = sum - 3.0
         for j in [24,31,17,18,19,20,21,22]:
            if i == j:
               sum = sum - 2.0
         for j in [16,23]:
            if i == j:
               sum = sum - 1.0
         for j in [3,6]:
            if i == j:
               sum = sum + 1.0
         for j in [0,7,8,9,14,15]:
             if i == j:
                sum = sum + 2.0
         for j in [1,6]:
             if i == j:
                sum = sum + 3.0
      if board[i] == 25:
         sum = sum - 900
         for j in [28,27,16,19,12,11,4,3]:
            if i == j:
               sum = sum + 5.0
         for j in [36,35,30,29,22,21,14,13,6,5,26,25,18,17,10,9,2,1]:
            if i == j:
               sum = sum + 4.0
         for j in [38,37,34,33,31,23,15,7,24,16,8,0]:
            if i == j:
               sum = sum + 3.0
         for j in [39,32,46,45,44,43,42,41]:
            if i == j:
               sum = sum + 2.0
         for j in [47,40]:
            if i == j:
               sum = sum + 1.0
         for j in [60,57]:
            if i == j:
               sum = sum - 1.0
         for j in [63,56,55,54,49,48]:
             if i == j:
                sum = sum - 2.0
         for j in [62,57]:
             if i == j:
                sum = sum - 3.0
   sum = sum - 1.0
   return sum

def IsPositionUnderThreat(board,position,player):
   # determine opposing player
   if player == 10:
      enemy = 20
   elif player == 20:
      enemy = 10
   else:
      return False
   # find all possible squares the opposing team is attacking
   enplace = []
   accum = []
   i = 0
   enplace = GetPlayerPositions(board,enemy)
   for i in range(0,len(enplace),1):
      accum = accum + [GetPieceLegalMoves(board,enplace[i])]
   # find if the postition is in the list (being attacked)
   j = 0
   toggle = 0
   for j in range(0,len(accum),1):
      for k in range(0,len(accum[j]),1):
         if accum[j][k] == position:
            toggle = 1
   # return True if attacked or False if not
   if toggle == 1:
      return True
   else:
      return False

def move(board,position,moving):
   # execute a move
   if (position > 63 or moving > 63):
      return [] # Error check for problems with move
   temp = list(board)
   temp[moving] = temp[position]
   temp[position] = 0
   return temp

def analyze(board,player):
   if len(board) != 64:
      return False
   # analyze the board
   accum = []
   pos = GetPlayerPositions(board, player)
   for i in pos:
      moves = GetPieceLegalMoves(board,i)
      for j in moves:
         val = value(move(board,i,j))
         accum = accum + [[[i,j],val]]
   return accum


def chessplayer(board,player):
   # set a toggle to determine
   if player == 10:
      friendly = 10
      enemy = 20
      factor = 1.0
   elif player == 20:
      friendly = 20
      enemy = 10
      factor = -1.0
   else:
      return False
   # generate tree (3 major for loops looking at a move depth of 4)
   # (3 background for loops using max min algorithm to send value to first tier)
   L = analyze(board,player)
   check = []
   kingpos = -1
   # determine if there is a check/checkmate and make appropriate move
   for i in range(0,len(board),1):
      if board[i] == (player+5):
         kingpos = i
   if IsPositionUnderThreat(board,kingpos,player) == True:
      for i in range(0,len(L),1):
         test = move(board,L[i][0][0],L[i][0][1])
         for j in range(0,len(test),1):
            if test[j] == (player+5):
               kingpos = j
         if IsPositionUnderThreat(test,kingpos,player) == False:
            check = check + [L[i]]
      if len(check) == 0:
         return [False,"CHECKMATE"]
      else:
         L = list(check)
   # create tree
   for i in range(0,len(L),1):
      test1 = move(board,L[i][0][0],L[i][0][1])
      L[i] = [L[i]] + analyze(test1,enemy)
      for j in range(1,len(L[i]),1):
         test2 = move(test1,L[i][j][0][0],L[i][j][0][1])
         L[i][j] = [L[i][j]] + analyze(test2,friendly)
         for y in range(2,len(L[i][j]),1):
            val2 = L[i][1][1][1]*factor
            if L[i][j][y][1]*factor > val2:
               val2 = L[i][j][y][1]*factor
            L[i][j][0][1] = val2*factor
      for z in range(1,len(L[i]),1):
         val3 = L[i][1][1][1]
         if L[i][z][0][1] > val3:
            val3 = L[i][z][1]
         if type(val3) == list:
            val3 = val3[1]
         L[i][0][1] = val3
   #print(L[10])
   #check the best move using the top tier values
   moves = L[0][0][0]
   cnt = L[0][0][1]*factor
   print(cnt)
   for i in range(1,len(L),1):
      if L[i][0][1]*factor > cnt:
         moves = L[i][0][0]
         cnt = L[i][0][1]*factor
   #print(moves)
   return moves