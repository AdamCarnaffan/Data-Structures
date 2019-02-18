from ChessLib import *

class Tree:

   def __init__(self, board, player, players_data, depth):
      self.board = board
      self.player = player
      self.p_data = players_data
      self.next = []
      self.genscore()
      self.depth = depth
      print(self.p_data)
    
   def genscore(self):
      self.score = 0
      print(self.p_data[1])
      for i in range(0, max(len(self.p_data[0]), len(self.p_data[1])), 1):
         for j in range(0, 2, 1):
            if len(self.p_data[j]) > i:
               self.score += PieceValue(self.p_data[j][i][0])
      return True

   def fetchScore(self):
      print(self.score)
      return True


