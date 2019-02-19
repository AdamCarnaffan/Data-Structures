from time import time
from helpers import *
start_time = time()

def InsertSort(array, data):
   if type(data) != list:
      array += [data]
   elif data != []:
      array += [data[0]]
      InsertSort(array, data[1::])
   for i in range(len(array) - 1, 0, -1):
      swap_flag = False
      for j in range(i, len(array) - i - 1, -1):
         if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            swap_flag = True
      if not swap_flag:
         break
   return True

def BubbleSort(array):
   for i in range(0, len(array), 1):
      swap_flag = False
      for j in range(0, len(array) - 1 - i, 1):
         if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
            swap_flag = True
      if not swap_flag:
         break
   return True

def BinarySearch(array, data):
   start, end = 0, len(array) - 1
   while start <= end:
      middle = (end + start)//2
      mid_val = array[middle]
      if mid_val == data:
         return middle
      elif mid_val < data:
         start = middle + 1
      else:
         end = middle - 1
   return -1

def IsPositionUnderThreat(board, opponent_board, postion):
   for i in opponent_board:
      moves = GetPieceLegalMoves(board, i)
      if postion in moves:
         return True
   return False

def InBoard(index):
   if index < 0 or index > 63:
      return False
   return True

def IsPlayer(board, index, player):
   if board[index] < player or board[index] > player + 5:
      return False
   return True

def GenOpponent(player):
   if player == 10:
      return 20
   elif player == 20:
      return 10
   return False

def PieceValue(piece):
   if piece == 10:  # pawns
      return 25
   elif piece == 20:
      return -25
   elif piece == 11:  # knights
      return 50
   elif piece == 21:
      return -50
   elif piece == 12:  # bishops
      return 55
   elif piece == 22:  
      return -55
   elif piece == 13:  # rooks
      return 75
   elif piece == 23:
      return -75
   elif piece == 14:  # quuens
      return 175
   elif piece == 24:
      return -175
   elif piece == 15:  # kings
      return 1000
   elif piece == 25:
      return -1000
   return False

def PositionRadius(position):
   if position in [27, 28, 35, 26]:
      return 0
   c1 = 0
   while (position - c1) % 8 != 0:
      c1 += 1
   if c1 == 0 or c1 == 7 or position - c1 == 56 or position - c1 == 0:
      return 3
   row = position//8
   if row == 1 or row == 6 or (position + 2) % 8 == 0 or (position - 1) % 8 == 0:
      return 2
   else:
      return 1

def PositionValue(piece_id, position):
   player = (piece_id//10) * 10
   if player == 10:
      factor = 1
   else:
      factor = -1
   piece_type = int(str(piece_id)[1])
   pr_functions = [PawnPV, KnightPV, BishopPV, RookPV, QueenPV, KingPV]
   return pr_functions[piece_type](factor, position)

def PawnPV(factor, position):
   value = PositionRadius(position)
   if value == 0:
      return 50 * factor
   elif value == 1:
      return 25 * factor
   elif value == 2:
      return 0 * factor
   else:
      return -10 * factor

def KnightPV(factor, position):
   value = PositionRadius(position)
   if value == 0:
      return 0 * factor
   elif value == 1:
      return 50 * factor
   elif value == 2:
      return 25 * factor
   else:
      return -10 * factor

def BishopPV(factor, position):
   value = PositionRadius(position)
   if value == 0:
      return 0 * factor
   elif value == 1:
      return 25 * factor
   elif value == 2:
      return 50 * factor
   else:
      return 10 * factor

def RookPV(factor, position):
   value = PositionRadius(position)
   if value == 0 or value == 1:
      return 25 * factor
      return 25 * factor
   elif value == 2:
      return 40 * factor
   else:
      return 50 * factor

def QueenPV(factor, position):
   value = PositionRadius(position)
   if value == 0:
      return 20 * factor
   elif value == 1:
      return 10 * factor
   elif value == 2:
      return 50 * factor
   else:
      return 50 * factor

def KingPV(factor, position):
   value = PositionRadius(position)
   if value == 0:
      return 10 * factor
   elif value == 1:
      return 25 * factor
   elif value == 2:
      return 40 * factor
   else:
      return 70 * factor

def OptionsRating(piece_id, moves):
   player = (piece_id//10) * 10
   if player == 10:
      factor = 1
   else:
      factor = -1
   piece_type = int(str(piece_id)[1])
   if piece_id == 5:
      return KingOR(moves, factor)
   else:
      return MoreOR(moves, factor)

def KingOR(moves, factor):
   return (8 - len(moves)) * 10 * factor

def MoreOR(moves, factor):
   return len(moves) * 10 * factor

def RooksConnected(player_board, player):
   r = 13
   if player == 20:
      r = 23
   index = BinarySearch(player_board, [r])
   if index == -1:
      return 0
   elif player_board[index + 1] == r:
      second = index + 1
   elif player_board[index - 1] == r:
      second = index - 1
   else:
      return 0
   if BinarySearch(player_board[index][2], player_board[second][1]) == -1:
      return 0
   else:
      return -75

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
   return board

def GetPlayerPositions(board, player):  # location of all player pieces
   if (player != 10 or player != 20) and type(board) != list:
      return False
   positions = []
   for i in range(0, 64, 1):
      if IsPlayer(board, i, player):
         InsertSort(positions, i)
   return positions

def GenPlayerData(board):  # [piece, position, [availible moves]]
   player_data = [[], []]
   for i in range(0, len(player_data), 1):
      player_data[i] = GetPlayerPositions(board, (i+1)*10)
      for j in range(0, len(player_data[i]), 1):
         player_data[i][j] = [board[player_data[i][j]]] + [player_data[i][j]] + [GetPieceLegalMoves(board, player_data[i][j])]
      BubbleSort(player_data[i])
   return player_data

# Piece Move Functions
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

def MovePieceT(board, pd, player, cur_pos, new_pos):  
   return True

def test():
   board = GenBoard()
   IndexBoard()
   a = GenPlayerData(board)
   print("--- %s seconds ---" % (time() - start_time))
   return True
