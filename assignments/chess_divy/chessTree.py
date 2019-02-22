from ChessLib import *
from copy import deepcopy


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
      for i in range(0, max(len(self.pd[0]), len(self.p[1])), 1):
         for j in range(0, 2, 1):
            if i >= len(self.pd[j]):
               continue
            score += PieceValue(self.p_data[j][i][0])
            score += PositionValue(self.p_data[j][i][0], self.p_data[j][i][1])
            score += OptionsRating(self.p_data[j][i][0], self.p_data[j][i][2])
      score += RooksConnected(self.p_data)
      return score

   def evalnext()


class Tree:

   def __init__(self, board, player, players_data, move=[], depth=0):
      self.board = board
      self.player = player
      self.p_data = players_data
      self.next = []
      self.moveinfo = move
      self.depth = depth
      self.score = self.genscore()

   def fetchscore(self):
      return self.score

   def fetchboard(self):
      return self.board
   
   def fetchplayer(self):
      return self.player

   def fetchpd(self, index=-1):
      if index == 0 or index == 1:
         return self.p_data[index]
      elif index == -1:
         return self.p_data
      return False   

   def genscore(self):
      score = 0
      for i in range(0, max(len(self.p_data[0]), len(self.p_data[1])), 1):
         for j in range(0, 2, 1):
            if len(self.p_data[j]) > i:
               score += PieceValue(self.p_data[j][i][0])
               score += PositionValue(self.p_data[j][i][0], self.p_data[j][i][1])
               score += OptionsRating(self.p_data[j][i][0], self.p_data[j][i][2])
      score += RooksConnected(self.p_data)
      return score

   def gennexts(self, q):
      pd_index = self.player//10 - 1
      for i in range(0, len(self.p_data[pd_index]), 1):
         if self.p_data[pd_index][i][2] == []:
            continue
         piecenodes = []
         for j in self.p_data[pd_index][i][2]:
            new_board, new_pd = list(self.board), deepcopy(self.p_data)
            opp_index = GenOpponent(self.player)//10 - 1
            if new_board[j] != 0:
               rmv = BinarySearchPDPos(new_pd[opp_index], j)
               new_pd[opp_index] = new_pd[opp_index][:rmv] + new_pd[opp_index][rmv + 1:]
            new_board[new_pd[pd_index][i][1]], new_board[j] = 0, new_pd[pd_index][i][0]
            m = [new_pd[pd_index][i][0], new_pd[pd_index][i][1], j]
            new_pd[pd_index][i][1] = j
            new_pd[pd_index][i][2] = GetPieceLegalMoves(new_board, j)
            node = Tree(new_board, (opp_index + 1) * 10, new_pd, m, self.depth + 1)
            InsertSortNodes(piecenodes, node)

         best_node = self.bestscore(piecenodes)
         InsertSortNodes(self.next, best_node)
         q.put(best_node)
      return True

   def bestscore(self, piecenodes):
      if self.player == 10:
         return piecenodes[:-1]
      elif self.player == 20:
         return piecenodes[0]
      return False

   def disptree(self):  # remove later
      s = Stack()
      s.push(self)
      s.push("")
      while len(s.store) != 0:
         indent = s.pop()
         node = s.pop()
         print(indent + str(node.score)+":"+str(node.depth)+":"+str(node.player)+str(node.moveinfo))
         for i in node.next:
            s.push(i)
            s.push(indent + "   ")
      return