from time import time
from queue import Queue
from chessTree import *


start_time = time()


def chessPlayer(board, player):
   IndexBoard()
   root = Tree(board, player, GenPlayerData(board))
   brain = Queue()
   brain.put(root)
   while True:
      curr = brain.get()
      opp = GenOpponent(curr.player)//10
      player = curr.player//10
      for i in curr.fetchpdata(player - 1):
         for j in i[2]:
            IsPositionUnderThreat(board, curr.fetchpd())
            new_board = list(curr.fetchboard)
            new_pd = list(curr.fetchpd())
            MovePieceT(new_board, new_pd, player, i[1], j, i[0])
            move = [j, i[1], i[0]]


      break
   print("---", time() - start_time, "seconds ---")
   return True


chessPlayer(GenBoard(), 10)
