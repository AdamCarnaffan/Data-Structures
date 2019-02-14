def GenBoard():
   board = []
   for i in range(0, 64, 1):
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
   board[35] = 23
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

def IndexBoard():
   display = ""
   for i in range(7, -1, -1):  # row
      for j in range(8 * i, 8 * i + 8, 1):
         display += str(j)
         if j == i*8 + 7:
            display += "\n"
         else:
            display += " "
   print(display)
   return True

def InBoard(index):
   if index < 0 or index > 63:
      return False
   return True

def IsPlayer(board, index, player):
   if board[index] < player or board[index] > player + 5:
      return False
   return True

def GetPlayerPositions(board, player):  # location of all player pieces
   if (player != 10 or player != 20) and type(board) != list:
      return False
   positions = []
   for i in range(0, 64, 1):
      if IsPlayer(board, i, player):
         positions += [i]
   return positions

def GetPieceLegalMoves(board, position):  # legal moves of piece at position
   if position < 0 or position > 63 or type(board) != list or board[position] == 0:
      return False
   move_functions = [GetPawnMoves, GetKnightMoves, GetBishopMoves, GetRookMoves, GetQueenMoves, GetKingMoves]
   current_row = position//8  # between 0 to 7
   player, opponent = board[position]//10 * 10, 20
   piece_type = int(str(board[position])[1])
   if player == 20:
      opponent = 10
   return move_functions[piece_type](board, position, player, opponent, current_row)

def GetPawnMoves(board, position, player, opponent, row):
   moves = []
   if player == 1:
      factor = 1 
   else:
      factor = -1
   for i in range(position + 7*factor, position + 10*factor, 1*factor):
      if i < 0 or i > 63 or i//8 != row + factor:
         continue
      elif i == position + 8*factor:
         if board[i] == 0:
            moves += [i]
         continue
      elif IsPlayer(board, i, opponent):
         moves += [i]
   return moves

def GetKnightMoves(board, position, player, opponent, row):
   moves = []
   for i in range(position - 2*8, position + 3*8, 8):
      if not InBoard(i) or i == position:
         continue
      elif abs(i//8 - row) == 2:
         l, r = i - 1, i + 1
         if l//8 == i//8 and (board[l] == 0 or IsPlayer(board, l, opponent)):
            moves += [l]
         if r//8 == i//8 and (board[r] == 0 or IsPlayer(board, r, opponent)):
            moves += [r]
      else:
         l, r = i - 2, i + 2
         if l//8 == i//8 and (board[l] == 0 or IsPlayer(board, l, opponent)):
            moves += [l]
         if r//8 == i//8 and (board[r] == 0 or IsPlayer(board, r, opponent)):
            moves += [r]
   return moves

def GetBishopMoves(board, position, player, opponent, row):
   moves, directions, n, j = [], [-1, 1, -1, 1], 1, -1
   while directions != [0, 0, 0, 0]:
      j += 1
      if j > 0 and j % 2 == 0:
         n *= -1
         if j == 4:
            j = 0
            n = abs(n) + 1
      if not directions[j]:
         continue
      index = position + 8*n + directions[j]*n
      if InBoard(index) and abs(index//8 - row) == abs(n):
         if board[index] == 0:
            moves += [index]
            continue
         elif IsPlayer(board, index, opponent):
            moves += [index]
         directions[j] = 0
      else:
         directions[j] = 0
   return moves   

def GetRookMoves(board, position, player, opponent, row):
   moves, directions, n, j = [], [[1, 1], [-1, 1], [0, 1], [0, 1]], 1, -1
   while directions != [[1, 0], [-1, 0], [0, 0], [0, 0]]:
      j += 1
      if j == 4:
         j = 0
         n += 1
      if not directions[j][1]:
         continue
      index = position + 8*n*directions[j][0] + n*directions[abs(3 - j)][0]
      if InBoard(index) and abs(index//8 - row) == abs(n*directions[j][0]):
         if board[index] == 0:
            moves += [index]
            continue
         elif IsPlayer(board, index, opponent):
            moves += [index]
         directions[j][1] = 0
      else:
         directions[j][1] = 0
   return moves

def GetQueenMoves(board, position, player, opponent, row):
   pass

def GetKingMoves(board, position, player, opponent, row):
   pass

def test():
   board = GenBoard()
   #DisplayBoard(board)
   IndexBoard()
   moves = GetPieceLegalMoves(board, 35)
   print(moves)
   return True  

test()