#REMOVE LATER
from time import time 
start_time = time()


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
         print("DEPTH 3 reached")
         break
      node.evalnext(q)
      temp_cnt += 1
      if len(q.store) == 0 or temp_cnt == -1:
         print("queue ran out somehow", temp_cnt)
         break
   print(len(q.store), "temp cnt:", temp_cnt)
   if move == []:
      status = False
   return [status, move, candidiateMoves, eT]

#REMOVE LATER:
current_board = GenBoard()
print(chessPlayer(current_board, 10))
print("---", time() - start_time, "seconds ---")