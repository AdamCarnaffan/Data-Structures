from chessPlayer import chessPlayer
import time
import random

def make_board():
   board = []
   for _ in range(0, 8, 1):
      for _ in range(0, 8, 1):
         board = board + [0]
   return board

def add_pieces(board):
   final = list(board)
   pawnRow = 1
   row = 0
   for i in range(1, 3, 1):
      # Pawns
      # for v in range(0, 8, 1):
      #    final[pawnRow*8+v] = 10*i
      # Knights
      final[8*row+1] = 10*i + 1
      final[8*row+6] = 10*i + 1
      # Bishops
      final[8*row+2] = 10*i + 2
      final[8*row+5] = 10*i + 2
      # Rooks
      final[8*row] = 10*i + 3
      final[8*row+7] = 10*i + 3
      # Queen
      final[8*row+3] = 10*i + 4
      # King
      final[8*row+4] = 10*i + 5
      pawnRow = 6
      row = 7
   return final

def interp_piece(value, odd):
   if value == 0:
      if odd:
         return "_"
      else:
         return "#"
   plr = int(str(value)[0])
   final = ""
   pieceCode = int(str(value)[1]) # String is always 2 long by here
   if pieceCode == 0:
      final = "P"
   elif pieceCode == 1:
      final = "N" # I know this isn't the first letter
   elif pieceCode == 2:
      final = "B" 
   elif pieceCode == 3:
      final = "R"
   elif pieceCode == 4:
      final = "Q"
   elif pieceCode == 5:
      final = "K"
   if plr == 1:
      return final
   else:
      return final.lower()

def invert_list(l):
   if len(l) < 1:
      return []
   return [l[len(l)-1]] + invert_list(l[0:len(l)-1])

def display_baord(board):
   inv = invert_list(board)
   for y in range(0, 8, 1):
      line = ""
      for x in range(0, 8, 1):
         line = line + interp_piece(inv[y*8+x], (y + x) % 2)
      print(line)
   return True

def GetPlayerPositions(board, player):
   s = int(player / 10)
   final = []
   for ind,b in enumerate(board):
      if int(str(b)[0]) == s:
         final += [ind]
   return final

def IsPositionUnderThreat(board, position, player):
   opp = 2 if player == 1 else 1
   mvs = []
   for v in range(0, 64, 1):
      if (int(str(board[position])[0]) == opp):
         mvs += GetPieceLegalMoves(board, v)
   if (position in mvs):
      return True
   return False

def GetPieceLegalMoves(board, position):
   validMove = [pawn, knight, bishop, rook, queen, king]
   pieceType = int(str(board[position])[-1])
   player = int(str(board[position])[0])
   final = []
   for v in range(0, 64, 1):
      if (validMove[pieceType](position, v, player) and positionIsAvailable(board, player, v) and not getCollisions(board, pieceType, position, v)):
         final += [v]
   return final

def get_path_points(f, i):
   if f == i:
      return []
   path = []
   final = [f % 8, int(f / 8)]
   initial = [i % 8, int(i / 8)]
   direction = [0, 0]
   direction[0] = int(abs(final[0] - initial[0])/(final[0] - initial[0])) if final[0] - initial[0] != 0 else 0
   direction[1] = int(abs(final[1] - initial[1])/(final[1] - initial[1])) if final[1] - initial[1] != 0 else 0
   if final[0] == initial[0]:
      for v in range(int(initial[1] + direction[1]), int(final[1]), direction[1]):
         path = path + [final[0] + 8*v]
   elif final[1] == initial[1]:
      for v in range(int(initial[0] + direction[0]), int(final[0]), direction[0]):
         path = path + [v + 8*final[1]]
   else:
      if abs(final[0] - initial[0]) != abs(final[1] - initial[1]):
         return []
      for v in range(1, int(abs(final[0] - initial[0])), 1):
         path = path + [(initial[0] + direction[0]*v) + (initial[1] + direction[1]*v)*8]
   return path

def positionIsAvailable(board, player, pos):
   if int(str(board[pos])[0]) != player:
      return True
   return False

def getCollisions(board, piece, curr, targ):
   if (piece == 1):
      return False
   pts = get_path_points(targ, curr)
   for b in pts:
      if (board[b] != 0):
         return True
   return False

def pawn(final, initial, player):
   if player == 2 and final-initial == 8:
      return True
   if player == 1 and initial-final == 8:
      return True
   return False

def knight(final, initial, player):
   f = [final % 8, int(final / 8)]
   i = [initial % 8, int(initial / 8)]
   diffx = abs(i[0] - f[0])
   diffy = abs(i[1] - f[1])
   if diffx == 2 and diffy == 1:
      return True
   elif diffx == 1 and diffy == 2:
      return True
   return False

def bishop(final, initial, player):
   f = [final % 8, int(final / 8)]
   i = [initial % 8, int(initial / 8)]
   if abs(i[0] - f[0]) == abs(i[1] - f[1]):
      return True
   return False

def rook(final, initial, player):
   f = [final % 8, int(final / 8)]
   i = [initial % 8, int(initial / 8)]
   diffx = abs(i[0] - f[0])
   diffy = abs(i[1] - f[1])
   if diffx == 0 and diffy != 0:
      return True
   elif diffy == 0 and diffx != 0:
      return True
   return False

def queen(final, initial, player):
   f = [final % 8, int(final / 8)]
   i = [initial % 8, int(initial / 8)]
   diffx = abs(i[0] - f[0])
   diffy = abs(i[1] - f[1])
   if diffx == diffy:
      return True
   elif diffx == 0 and diffy != 0:
      return True
   elif diffy == 0 and diffx != 0:
      return True
   return False

def king(final, initial, player):
   f = [final % 8, int(final / 8)]
   i = [initial % 8, int(initial / 8)]
   diffx = abs(i[0] - f[0])
   diffy = abs(i[1] - f[1])
   if diffx > 1 or diffy > 1:
      return False
   return True

def GD(board, player):
   print("=-=-=-=-=--=-=-=-=-=")
   print("Current Player: {0}".format(player))
   display_baord(board)
   return True

def main():
   for _ in range(0, 2, 1):
      v = make_board()
      v = add_pieces(v)
      player = 10
      moves = 0
      while moves < 20:
         GD(v, player)
         t = time.time()
         move = chessPlayer(v, player)
         print(time.time() - t)
         try:
            if not move[0]:
               continue
            pos = move[1][0]
            new = move[1][1]
            if pos == new:
               continue
         except:
            print("Move input invalid")
            continue
         if int(str(v[pos])[0])*10 != player or not (new in GetPieceLegalMoves(v, pos)):
            print("Move input invalid")
            continue
         v[new] = v[pos]
         v[pos] = 0
         player = 20 if player == 10 else 10
         moves = moves + 1
   return True

main()
   