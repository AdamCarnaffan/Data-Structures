from ChessLib import *

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