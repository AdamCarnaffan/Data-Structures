from ChessLib import *

class Tree:

   def __init__(self, board, player, players_data, move=[], depth=True):
      self.board = board
      self.player = player
      self.p_data = players_data
      self.next = []
      self.genscore()
      self.moveinfo = move
      self.depth = depth

   def genscore(self):
      self.score = 0
      for i in range(0, max(len(self.p_data[0]), len(self.p_data[1])), 1):
         for j in range(0, 2, 1):
            if len(self.p_data[j]) > i:
               self.score += PieceValue(self.p_data[j][i][0])
               self.score += PositionValue(self.p_data[j][i][0], self.p_data[j][i][1])
               self.score += OptionsRating(self.p_data[j][i][0], self.p_data[j][i][2])
      self.score += RooksConnected(self.p_data[0], 10)
      self.score += RooksConnected(self.p_data[1], 10)
      return True

   def fetchboard(self):
      return self.board
   
   def fetchscore(self):
      print(self.score)
      return True
   
   def fetchpd(self, index=-1):
      if index == 0 or index == 1:
         return self.p_data[index]
      elif index == -1:
         return self.p_data
      return False     
   
   def addnext(self, child):
      self.next += [child]
      return True

