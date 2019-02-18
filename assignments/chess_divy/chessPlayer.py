from time import time
from chessTree import *


start_time = time()


def main():
   board = GenBoard()
   T = Tree(board, 10, GenPlayerData(board), 0)
   T.fetchScore()
   print("--- %s seconds ---" % (time() - start_time))
   return True


main()
