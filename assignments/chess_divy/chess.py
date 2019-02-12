def GenBoard():
   board = []
   for i in range(64):
      if i >= 16 and i <= 47:  # no pieces
         board.append(0)
      elif i <= 7:  # back w rank
         if i == 0 or i == 7:  # w rooks
            board.append(13)
         elif i == 1 or i == 6:  # w knights
            board.append(11)
         elif i == 2 or i == 5:  # w bishops
            board.append(12)
         elif i == 3:  # queen
            board.append(14)
         else:  # b king
            board.append(15)
      elif i <= 15:  # w pawns
         board.append(10)
      elif i >= 48 and i <=55:  # b pawns 
         board.append(20)
      elif i >=56:  # back b rank
         if i == 56 or i == 63:  # b rooks
            board.append(23)
         elif i == 57 or i == 62:  # b knights
            board.append(21)
         elif i == 58 or i == 61:  # b bishops
            board.append(22)
         elif i == 59:  # b queen
            board.append(24)
         else:  # b king
            board.append(25)
   return board

def DisplayBoard(board):
   display = ""
   for i in range(7, -1, -1):
      for j in range(i + 7, i, -1): 
         index = 
         print(index)
      break
   return 

def GetPlayerPositions(board, player):  # location of all player pieces
   if player != 10 or player != 20 or type(board) != list:
      return False
   positions = []
   for i in range(0, len(board), 1):
      if board[i] >= player:
         positions += [i]
   return positions

def GetPieceLegalMoves(board, position):  # legal moves of piece at position
   if position < 0 or position > 63 or type(board) or board[position] == 0:
      return False
   moves = []
   current_row = position//8
   player = int(str(value[0]) + "0")
   opponent = 20
   piece_type = int(str(value[1]))
   if player == 20:
      opponent = 10
   if piece_type == 0:
      moves = GetPawnMoves(board, position, player, opponent)
   else: 
      pass
   return moves
   
   

def GetPawnMoves(board, position, player, opponent):
   if player == 10:
      factor = 1
   else:
      factor -1
   for i in range(factor)
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
         if i - 1:
            pass
   pass

def test():
   board = GenBoard()
   DisplayBoard(board)
   return True  

test()