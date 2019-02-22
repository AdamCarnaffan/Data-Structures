from time import time
from helpers import *
from chessTree import *


start_time = time()

def chessPlayer(board, player):
   status, move, candidiateMoves, evalTree = True, [], [], []
   root = Tree(board, player, GenPlayerData(board))
   q = Queue()
   q.put(root)
   temp = 0
   indexBoard()
   printBoard(board)
   while time() - start_time < 10:
      node = q.get()
      node.gennexts(q)
      temp += 1
      if temp == 1:
         root.disptree()
         break
   if move == []:
      status = False
   
   
   return [status, move, candidiateMoves, evalTree]

#remove later:
current_board = GenBoard()
print(chessPlayer(current_board, 10))
print("---", time() - start_time, "seconds ---")