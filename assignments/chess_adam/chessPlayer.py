class Data_Node:
   def __init__(self, board, value, playing):
      self.next = [] # of Data_Nodes
      self.weight = value
      self.state = [board, playing]


def chessPlayer(board: list, player: int) -> list:

   return [] # [ status (bool), move ([piece, move]), candidateMoves (List of [move, weight] values), evalTree (None)]