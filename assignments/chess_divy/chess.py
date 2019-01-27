def GetPlayerPositions(board, player):  # location of all player pieces
   if player != 10 or player != 20 or type(board) != list:
      return False
   positions = []
   for i in range(0, len(board), 1):
      if board[i] >= player:
         positions += [i]
    return positions

def GetPieceLegalMoves(board, position):  # legal moves of piece at position
   if position < 0 and position > 63 or type(board) != list:
      return False
   piece = board[position]
   moves = []
   player = 10
   opponent = 20
   if str(piece)[0] != 1:
      player = 20
      opponent = 10
   peice_type = int(str(peice)[1])  # we now know player and type of piece
   row  = (position + 1)//8
   if peice_type == 0:  # pawn moves
      if player == 10:
         for i in range(position + 7, position + 10, 1):
            if i > 63:
               break
            if board[i] == 0 or str(i)[0] == '2':
               moves += [i]
      else:
         for i in range(position - 7, position - 10, -1):
            if i < 0:
               break
            if board[i] == 0 or str(i)[0] == '1':
               moves += [i]
      return moves
   elif peice_type == 1:  # knight moves
      for i in range(position-2, position + 3, 2):
         if i < 0 or i > 63:
            continue
         
        