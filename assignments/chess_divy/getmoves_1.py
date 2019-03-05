from chessPlayer import *


def GetPieceLegalMoves(board, position):
   piece = board[position]
   if piece == 0:
      return False
   move_functions = [GetPawnMoves, GetKnightMoves, GetBishopMoves, GetRookMoves, GetQueenMoves, GetKingMoves]
   current_row = position//8  # between 0 to 7
   player, opponent = piece//10 * 10, 20
   piece_type = PieceType(piece)
   if player == 20:
      opponent = 10
   return move_functions[piece_type](board, position, player, opponent, current_row)

def GetPawnMoves(board, position, player, opponent, row):
   moves = []
   if player == 10:
      factor = 1 
   else:
      factor = -1
   for i in range(position + 7*factor, position + 10*factor, 1*factor):
      if i < 0 or i > 63 or i//8 != row + factor:
         continue
      elif i == position + 8*factor:
         if board[i] == 0:
            InsertSort(moves, i)
         continue
      elif IsPlayer(board, i, opponent):
         InsertSort(moves, i)
   return moves

def GetKnightMoves(board, position, player, opponent, row):
   moves = []
   for i in range(position - 2*8, position + 3*8, 8):
      if not InBoard(i) or i == position:
         continue
      elif abs(i//8 - row) == 2:
         l, r = i - 1, i + 1
         if l//8 == i//8 and (board[l] == 0 or IsPlayer(board, l, opponent)):
            InsertSort(moves, l)
         if r//8 == i//8 and (board[r] == 0 or IsPlayer(board, r, opponent)):
            InsertSort(moves, r)
      else:
         l, r = i - 2, i + 2
         if l//8 == i//8 and (board[l] == 0 or IsPlayer(board, l, opponent)):
            InsertSort(moves, l)
         if r//8 == i//8 and (board[r] == 0 or IsPlayer(board, r, opponent)):
            InsertSort(moves, r)
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
            InsertSort(moves, index)
            continue
         elif IsPlayer(board, index, opponent):
            InsertSort(moves, index)
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
            InsertSort(moves, index)
            continue
         elif IsPlayer(board, index, opponent):
            InsertSort(moves, index)
         directions[j][1] = 0
      else:
         directions[j][1] = 0
   return moves

def GetQueenMoves(board, position, player, opponent, row):
   moves = []
   InsertSort(moves, GetBishopMoves(board, position, player, opponent, row))
   InsertSort(moves, GetRookMoves(board, position, player, opponent, row))
   return moves

def GetKingMoves(board, position, player, opponent, row):
   moves = []
   factor = 1
   for i in range(position + 7, position + 10, 1):
      if not InBoard(i) or i//8 != row + 1:
         continue
      for j in range(i, i - 8*3, -8):
         if j == position:
            continue
         elif InBoard(j) and not IsPlayer(board, i, player):
            InsertSort(moves, j)
   return moves