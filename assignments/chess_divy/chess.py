def GenBoard():
   board = []
   for i in range(64):
      if i >= 16 and i <= 47:  # no pieces
         board += [0]
      elif i <= 7:  # back w rank
         if i == 0 or i == 7:  # w rooks
            board += [13]
         elif i == 1 or i == 6:  # w knights
            board += [11]
         elif i == 2 or i == 5:  # w bishops
            board += [12]
         elif i == 3:  # queen
            board += [14]
         else:  # b king
            board += [15]
      elif i <= 15:  # w pawns
         board += [10]
      elif i >= 48 and i <=55:  # b pawns 
         board += [20]
      elif i >=56:  # back b rank
         if i == 56 or i == 63:  # b rooks
            board += [23]
         elif i == 57 or i == 62:  # b knights
            board += [21]
         elif i == 58 or i == 61:  # b bishops
            board += [22]
         elif i == 59:  # b queen
            board += [24]
         else:  # b king
            board += [25]
   return board

def DisplayBoard(board):
   display = ""
   for i in range(7, -1, -1):  # row
      for j in range(8 * i, 8 * i + 8, 1): 
         piece = board[j]
         if piece == 0:
            if (j//8) % 2 == 0:
               if j % 2 == 0:
                  display += "_"
               else:
                  display += "#"
            else:
               if j % 2 == 0:
                  display += "#"
               else:
                  display += "_"
         elif piece <= 15:
            if piece == 10:
               display += "P"
            elif piece == 11:
               display += "N"
            elif piece == 12:
               display += "B"
            elif piece == 13:
               display += "R"
            elif piece == 14:
               display += "Q"
            else:
               display += "K"
         elif piece <= 25:
            if piece == 20:
               display += "p"
            elif piece == 21:
               display += "n"
            elif piece == 22:
               display += "b"
            elif piece == 23:
               display += "r"
            elif piece == 24:
               display += "q"
            else:
               display += "k"
         if j == i*8 + 7:
            display += "\n"
         else:
            display += " "
   print(display)
   return True

def GetPlayerPositions(board, player):  # location of all player pieces
   if player != 10 or player != 20 or type(board) != list:
      return False
   positions = []
   for i in range(0, len(board), 1):
      if board[i] >= player:
         positions += [i]
   return positions

def GetPieceLegalMoves(board, position):  # legal moves of piece at position
   if position < 0 or position > 63 or type(board) != list or board[position] == 0:
      return False
   moves = []
   current_row = position//8  # between 0 to 7
   player = int(str(board[position])[0])  # 1 or 2
   opponent = 2
   piece_type = int(str(board[position])[1])  # between 0 to 5
   if player == 2:  # 1 is white, 2 is black
      opponent = 1
   if piece_type == 0:
      moves = GetPawnMoves(board, position, player, opponent, current_row)
   else: 
      pass
   return moves

def GetPawnMoves(board, position, player, opponent, row):
   if player == 1:
      factor = 1
   else:
      factor = -1
   next_row = row + factor
   moves = []
   for i in range(position + 7*factor, position + 10*factor, 1*factor):
      #print(i, player, opponent, row, next_row)
      if i < 0 or i > 63 or i//8 != next_row:
         continue
      elif i == position + 8*factor or int(str(i)[1]) == opponent:
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
         if i - 1:
            pass
   pass

def test():
   board = GenBoard()
   DisplayBoard(board)
   moves = GetPieceLegalMoves(board, 8)
   return True  

test()