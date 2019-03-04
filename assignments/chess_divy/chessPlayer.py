from helpers import *
from chessTree import *
#REMOVE LATER
from time import time 
start_time = time()

def printBoard(board):
   accum="---- BLACK SIDE ----\n"
   max=63
   for j in range(0,8,1):
      for i in range(max-j*8,max-j*8-8,-1):
         accum=accum+'{0: <5}'.format(board[i])
      accum=accum+"\n"
   accum=accum+"---- WHITE SIDE ----"
   print(accum)
   return True

def indexBoard():
   accum="---- BLACK SIDE ----\n"
   max=63
   for j in range(0,8,1):
      for i in range(max-j*8,max-j*8-8,-1):
         accum=accum+'{0: <5}'.format(i)
      accum=accum+"\n"
   accum=accum+"---- WHITE SIDE ----"
   print(accum)
   return True


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

def InsertSortNodes(array, nodes):  # sorting by score
   if type(nodes) != list:
      array += [nodes]
   elif nodes != []:
      array += [nodes[0]]
      InsertSortNodes(array, nodes[1::])
   for i in range(len(array) - 1, 0, -1):
      swap_flag = False
      for j in range(i, len(array) - i - 1, -1):
         if array[j].score < array[j - 1].score:
            array[j], array[j - 1]= array[j - 1], array[j]
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

def BubbleSortPDPos(array):
   for i in range(0, len(array), 1):
      swap_flag = False
      for j in range(0, len(array) - 1 - i, 1):
         if array[j][1] > array[j + 1][1]:
            swap = list(array[j])
            swap[2] = list(array[j][2])
            array[j] = list(array[j + 1])
            array[j][2] = list(array[j + 1][2])
            array[j + 1] = list(swap)
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

def BinarySearchPDPos(array, data):
   start, end = 0, len(array) - 1
   while start <= end:
      middle = (end + start)//2
      mid_val = array[middle][1]
      if mid_val == data:
         return middle
      elif mid_val < data:
         start = middle + 1
      else:
         end = middle - 1
   return -1

def IsPositionUnderThreat(opponent_board, position):
   for i in range(0, len(opponent_board), 1):
      if BinarySearch(opponent_board[i][2], position) != -1:
         return True
   return False

def SafetyRating(player, pd):
   p_i = player//10 - 1
   o_i = GenOpponent(player)//10 - 1
   score = 0
   factor = 1
   if player == 10:
      factor = -1
   for i in range(0, len(pd[p_i]), 1):
      if not IsPositionUnderThreat(pd[o_i], pd[p_i][i][1]):
         continue
      score += PieceValue(pd[p_i][i][0]) * factor
   return score

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

def PieceType(piece):
   if piece == 0:
      return -1
   return int(str(piece)[1])

def PieceValue(piece):
   pt = PieceType(piece)
   factor = -1
   if piece//10 == 1:
      factor = 1
   if pt == 0:
      return 50 * factor
   elif pt == 1:
      return 75 * factor
   elif pt == 2:
      return 75 * factor
   elif pt == 3:
      return 100 * factor
   elif pt == 4:
      return 200 * factor
   elif pt == 5:
      return 1000 * factor
   return 0

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
   piece_type = PieceType(piece_id)
   pr_functions = [PawnPV, KnightPV, BishopPV, RookPV, QueenPV, KingPV]
   return pr_functions[piece_type](factor, position)

def PawnPV(factor, position):
   value = PositionRadius(position)
   if value == 0:
      return 50 * factor
   elif value == 1:
      return 30 * factor
   elif value == 2:
      return 0 * factor
   else:
      return 100 * factor

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
   or_functions = [MoreOR, MoreOR, MoreOR, MoreOR, MoreOR, KingOR]
   if player == 10:
      factor = 1
   else:
      factor = -1
   piece_type = PieceType(piece_id)
   return or_functions[piece_type](moves, factor)

def MoreOR(moves, factor):
   return len(moves) * 10 * factor

def KingOR(moves, factor):
   return (8 - len(moves)) * 10 * factor

def RooksConnected(player_data):
   score = 0
   for i in range(0, 2, 1):
      player = (i + 1) * 10
      rook_id, indices = player + 3, []
      for j in range(0, len(player_data[i]), 1):
         if player_data[i][j][0] == rook_id:
            indices += [j]
            if len(indices) == 2:
               if BinarySearch(player_data[i][indices[0]][2], player_data[i][indices[1]][0]) != -1:
                  factor = 1
                  if player == 10:
                     factor = -1
                  score += 25 * factor
                  break
   return score

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
         elif i == 3:  # w king
            board += [15]
         else:  # w queen
            board += [14]
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
         elif i == 59:  # b king
            board += [25]
         else:  # b queen
            board += [24]
   return board

def GetPlayerPositions(board, player):
   positions = []
   for i in range(0, 64, 1):
      if IsPlayer(board, i, player):
         InsertSort(positions, i)
   return positions

def GenPlayerData(board):  # [piece, position, [availible moves]]
   player_data = [[], []]
   for i in range(0, 2, 1):
      player_data[i] = GetPlayerPositions(board, (i+1)*10)
      for j in range(0, len(player_data[i]), 1):
         pos = player_data[i][j]
         player_data[i][j] = [board[pos]] + [pos] + [GetPieceLegalMoves(board, pos)]
   return player_data

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

class Queue:

   def __init__(self):
      self.store = []
   
   def put(self, data):
      self.store += [data]
      return True
   
   def get(self):
      data = self.store[0]
      self.store = self.store[1:]
      return data

class Stack:

   def __init__(self):
      self.store = []
   
   def push(self, data):
      self.store += [data]
      return True
   
   def pop(self):
      data = self.store[-1]
      self.store = self.store[:-1]
      return data


class evalTree:

   def __init__(self, board, player, pd, depth, move):
      self.board = board
      self.player = player
      self.pd = pd
      self.depth = depth
      self.move = move
      self.next = []
      self.score = self.genscore()
   
   def genscore(self):
      score = 0
      for i in range(0, max(len(self.pd[0]), len(self.pd[1])), 1):
         for j in range(0, 2, 1):
            if i >= len(self.pd[j]):
               continue
            score += PieceValue(self.pd[j][i][0])
            score += PositionValue(self.pd[j][i][0], self.pd[j][i][1])
            score += OptionsRating(self.pd[j][i][0], self.pd[j][i][2])
      score += RooksConnected(self.pd)
      score += SafetyRating(self.player, self.pd)
      score += SafetyRating(GenOpponent(self.player), self.pd)
      return score

   def evalnext(self, q):
      p_index = self.player//10 - 1
      for i in range(0, len(self.pd[p_index]), 1):
         if self.pd[p_index][i][2] == []:
            continue
         for j in self.pd[p_index][i][2]:
            nB = list(self.board)
            npd = [[], []]
            opp = GenOpponent(self.player)
            o_index = opp//10 - 1
            for n1 in range(0, len(self.pd), 1):
               npd[n1] = list(self.pd[n1])
               for n2 in range(0, len(self.pd[n1]), 1):
                  npd[n1][n2] = list(self.pd[n1][n2])
                  npd[n1][n2][2] = list(self.pd[n1][n2][2])
            if IsPlayer(nB, j, self.player):
               """print(self.player, self.depth)
               print("-------")
               print(npd[p_index], "j is:", j, "i is", i)
               print(nB)"""
               raise ValueError("Clearly player data contains incorrect moves")
            elif IsPlayer(nB, j, opp):
               delete = BinarySearchPDPos(npd[o_index], j)
               if delete == -1:
                  raise ValueError("delete is clearly broken - there is enemy there")
               npd[o_index] = npd[o_index][:delete] + npd[o_index][delete + 1:]
            nM = [npd[p_index][i][0], npd[p_index][i][1], j]
            nB[npd[p_index][i][1]] = 0
            nB[j] = npd[p_index][i][0]
            npd[p_index][i][2] = GetPieceLegalMoves(nB, j)
            npd[p_index][i][1] = j
            for p1 in range(0, len(npd[p_index]), 1):
               if BinarySearch(npd[p_index][p1][2], j) != -1:
                  npd[p_index][p1][2] = GetPieceLegalMoves(nB, npd[p_index][p1][1])
            BubbleSortPDPos(npd[p_index])
            node = evalTree(nB, opp, npd, self.depth + 1, nM)
            InsertSortNodes(self.next, node)
            q.put(node)
      return True

   def fetchscore(self):
      return self.score

   def disptree(self):  # remove later
      s = Stack()
      s.push(self)
      s.push("")
      while len(s.store) != 0:
         indent = s.pop()
         node = s.pop()
         print(indent + str(node.score)+":"+str(node.depth)+":"+str(node.player)+str(node.move))
         for i in node.next:
            s.push(i)
            s.push(indent + "   ")
      return True


def chessPlayer(board, player):
   status, move, candidiateMoves, eT = True, [], [], []
   root = evalTree(board, player, GenPlayerData(board), 0, [])
   q = Queue()
   q.put(root)
   temp_cnt = 0
   indexBoard()
   printBoard(board)
   while time() - start_time < 10:
      node = q.get()
      if node.depth == 4:
         print("DEPTH 4 reached")
         break
      node.evalnext(q)
      temp_cnt += 1
      if len(q.store) == 0 or temp_cnt == -1:
         print("queue ran out somehow", temp_cnt)
         break
   print(len(q.store), "temp cnt:", temp_cnt, q.store[-1].depth)
   if move == []:
      status = False
   return [status, move, candidiateMoves, eT]

#REMOVE LATER:
current_board = GenBoard()
print(chessPlayer(current_board, 10))
print("---", time() - start_time, "seconds ---")
