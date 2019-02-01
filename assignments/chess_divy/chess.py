def GetPlayerPositions(board, player):  # location of all player pieces
   if player != 10 or player != 20 or type(board) != list:
      return False
   positions = []
   for i in range(0, len(board), 1):
      if board[i] >= player:
         positions += [i]
   return positions

def GetPieceLegalMoves(board, position):  # legal moves of piece at position
   if position < 0 and position > 63 or type(board) != list:
      return False
   piece = board[position]
   moves = []
   player = 10
   opponent = 20
   if str(piece)[0] != 1:
      player = 20
      opponent = 10
   peice_type = int(str(peice)[1])  # we now know player and type of piece
   pass

def GetPawnMoves(board, position, player):
   factor = 1  
   opponent = 2
   if player == 20:
      factor = -1
      opponent = 1 
   # remove line 24 -> 28 in all get functions and pass via call if it's in all of them 
   row = position//8 - factor
   moves = []
   for i in range(position + (7*factor), positon + (10*factor), i += factor):
      if i < 0 or i > 63 or i//8 != row:
         continue
      elif board[i] == 0 or int(str(board[i])[0]) == opponent:
         moves += [i]
   return moves

def GetKnightMoves(board, position, player):
   factor = 1
   opponent = 2
   if player == 20:
      factor = -1
      opponent = 1
   row = position//8
   for i in range(position -16, position + 17, 8):  # check up 2 left right, up 1 left right 2, inverse for bottom
      if i == abs(position + 16):
         if i - 1 



def tester():
   return True  
