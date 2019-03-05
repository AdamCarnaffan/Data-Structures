import math as mh
import time
import random as rd

class Queue:

   def __init__(self):
      self.store = []

   def push(self, val):
      self.store = self.store + [val]

   def pop(self):
      if len(self.store) < 1:
         return [False, 0]
      else:
         rt = self.store[0]
         self.store = self.store[1:len(self.store)]
         return [True, rt]

   def length(self):
      return len(self.store)

class Data_Node:

   Bias = 54
   MoveLimit = 30

   def __init__(self, board, playing):
      self.next = [] # of Data_Nodes
      self.move = [-1, -1]
      self.sims = 1
      self.score = 0
      self.board = board
      self.playing = playing
      self.over = False

   def get_value(self, parentVisits):
      return (self.score/self.sims) + self.Bias*mh.sqrt(mh.log(parentVisits)/self.sims)

   def make_move(self, mv):
      self.move = mv
      self.board = move(self.board, mv)
      self.playing = 20 if self.playing == 10 else 10
      return True

   def play(self):
      board = list(self.board)
      stps = 0
      ply = self.playing
      indMatch = [-1]*10 + [0] + [-1]*10 + [1]
      king = [find_king(board, 10)]
      king = king + [find_king(board, 20)]
      takes = [0, 0]
      while not check_king(board, king[indMatch[ply]]):
         mv = sample_move(board, ply, False)
         print(mv)
         if len(mv) < 1:
            break
         if board[mv[1]] != 0:
            takes[indMatch[ply]] += 1
         board = move(board, mv)
         if mv[0] == king[indMatch[ply]]:
            king[indMatch[ply]] = mv[1]
         ply = 20 if ply == 10 else 10
         stps = stps + 1
         if stps > 35:
            ply = 3
            break
      if stps == 0:
         self.over = True
      self.score = 1 if ply == self.playing else 0
      other = 10 if self.playing == 20 else 20
      self.score = self.score*998 + 123*(takes[int(self.playing/10)-1]) - 30*(takes[int(other/10)-1])
      return True

   def simulate_node(self, isMove):
      # Generate new possibility
      new = Data_Node(self.board, self.playing)
      self.next = self.next + [new]
      mv = sample_move(new.board, new.playing, isMove)
      if mv == []:
         new.score = -1000
         return 0
      elif str(mv[1])[-1] == 5:
         new.score -= 40
      new.make_move(mv)
      # Simulate to determine score
      new.play()
      return new.score

   def build(self, parSims):
      isNeeded = True if parSims == -1 else False
      if len(self.next) > 0:
         self.sims = self.sims + 1
         best = self
         sms = self.sims if parSims == -1 else parSims
         bestPar = True
         for n in self.next:
            if n.get_value(self.sims) >= best.get_value(sms):
               bestPar = False
               best = n
               sms = self.sims
         if bestPar:
            return -self.simulate_node(isNeeded)
         sc = best.build(self.sims)
         self.score = self.score + sc/24
         return -sc
      else:
         return -self.simulate_node(isNeeded)

   def expand(self):
      if self.over:
         return True
      self.build(-1)
      return False # Returns game completion state
   
   def traverse(self):
      q = Queue()
      q.push([self, self.sims])
      final = []
      while (q.length() > 0):
         s = q.pop()[1]
         final = final + [[s[0].move, s[0].get_value(s[1])]]
         for n in s[0].next:
            q.push([n, s[0].sims])
      return final

   def select_node(self):
      best = None
      val = 0
      for op in self.next:
         new = op.get_value(self.sims)
         if best == None or new > val or (abs(new - val) < 15 and str(self.board[best.move[0]])[-1] == 0):
            best = op
            val = new
      return best

   def visualize(self, indent=0, parVal=-1):
      ind = ''
      parVal = self.sims if parVal == -1 else parVal
      for _ in range(0, indent, 1):
         ind = ind + '   '
      print(ind + str(self.move[1]) ,"-->", str(self.get_value(parVal)))
      for t in self.next:
         t.visualize(indent+1, self.sims)
      return True

   def fetch_candidates(self, player):
      mvs = []
      for n in self.next:
         mvs = mvs + [n.move, n.get_value(self.sims)]
      return mvs

   def get_move(self):
      return self.move


def sample_move(board, player, isMove):
   pieces = GetPlayerPositions(board, player)
   if len(pieces) < 1:
      return []
   mvs = []
   # Add bias to pieces that can take
   step = 0
   plKing = find_king(board, player) if isMove else -1
   while len(mvs) < 1:
      pc = pieces[rd.randint(0, len(pieces)-1)] if len(pieces) > 1 else pieces[0]
      mvs = GetPieceLegalMoves(board, pc, plKing)
      step = step + 1
      if isMove and step < 4:
         mvs = moves_take(board, mvs)
         continue
      if len(mvs) < 1 and plKing != -1:
         ll = find_king_safe_moves(board, player, plKing)
         if len(ll) < 1:
            return []
         mvs = ll[1]
         pc = ll[0]
         break
      if step > 100:
         return []
   return [pc, mvs[rd.randint(0, len(mvs)-1)] if len(mvs) > 1 else mvs[0]]

def find_king_safe_moves(board, player, king):
   mvs = []
   for p in GetPlayerPositions(board, player):
      v = GetPieceLegalMoves(board, p, king)
      if len(v) > 0:
         mvs = mvs + [[p, v]]
         break
   if mvs == []:
      return []
   return [mvs[0][0], mvs[0][1]]

def moves_take(board, moves):
   final = []
   for v in moves:
      if board[v] != 0:
         final = final + [v]
   return final

def find_king(board, player):
   st = 0 if player == 1 else 63
   trav = 1 if st == 0 else -1
   for n in range(st, 64*trav + st, trav):
      if board[n] == player + 5:
         return n
   return -1 

def check_king(board, king): # King can get rekt
   if str(board[king])[-1] != 5 or king < 0 or (IsPositionUnderThreat(board, king)):
      return True
   return False

def move(board, move):
   b = list(board)
   b[move[1]] = b[move[0]]
   b[move[0]] = 0
   return b

def GetPlayerPositions(board, player):
   s = int(player / 10)
   final = []
   for ind,b in enumerate(board):
      if int(str(b)[0]) == s:
         final += [ind]
   return final

def IsPositionUnderThreat(board, position):
   if position == 0:
      return False
   opp = 20 if str(board[position])[0] == "1" else 10
   pcs = GetPlayerPositions(board, opp)
   for v in pcs:
      for m in GetPieceLegalMoves(board, v, -1):
         if m == position:
            return True
   return False

def GetPieceLegalMoves(board, position, kingP):
   validMove = [pawn, knight, bishop, rook, queen, king]
   pieceType = int(str(board[position])[-1])
   player = int(str(board[position])[0])
   opp = "2" if player == 1 else "1"
   final = []
   for v in range(0, 64, 1):
      if (validMove[pieceType](position, v, player) and positionIsAvailable(board, player, v) and not getCollisions(board, pieceType, position, v)):
         if pieceType == 0 and board[v] != 0:
            continue
         if kingP != -1:
            kng = kingP
            if str(board[position])[-1] == "5":
               kng = v
            simBoard = move(board, [position, v])
            if IsPositionUnderThreat(simBoard, kng):
               continue
         final += [v]
      elif pieceType == 0 and pawnMove(position, v, player) and str(board[v])[0] == opp:
         final += [v]
   return final

def pawnMove(initial, final, player):
   f = [final % 8, int(final / 8)]
   i = [initial % 8, int(initial / 8)]
   diffx = abs(f[0]-i[0])
   diffy = f[1]-i[1]
   if (player == 1 and diffy == -1) or (player == 2 and diffy == 1):
      if diffx == 1:
         return True
   return False

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

def getPossibleMoves(board, player):
   fin = []
   pec = GetPlayerPositions(board, player)
   for n in pec:
      fin = fin + GetPieceLegalMoves(board, n, -1)
   return fin

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

def chessPlayer(board: list, player: int) -> list:
   state = Data_Node(board, player)
   t = time.time()
   while time.time() - t < 6:
      if state.expand():
         break
   # Selection from state
   status = False
   if state.next != []:
      status = True
   return [status, state.select_node().get_move(), state.fetch_candidates(player), state.traverse()] # [ status (bool), move ([piece, move]), candidateMoves (List of [move, weight] values), evalTree (None)]