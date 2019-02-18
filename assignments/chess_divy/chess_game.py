from ChessLib_org import GenBoard, InBoard, GetPieceLegalMoves, DisplayBoard

def two_player():
    board = GenBoard()
    end_flag, player = False, 10
    DisplayBoard(board)
    while True:
        if player == 10:
            try:
                pos = int(input("Enter a piece-position to move:"))
                if not InBoard(pos):
                    raise
                moves = GetPieceLegalMoves(board, pos)
                print(moves)
                new_pos = int(input("Enter a position to move to:"))
                if not InBoard(new_pos) or pos == new_pos:
                    raise
                if new_pos not in moves:
                    raise
                if board[new_pos] == 25:
                    end_flag = True
                board[pos], board[new_pos] = 0, board[pos]
                player = 20
                DisplayBoard(board)
            except:
                print("Invalid input, try again")
                continue
        if end_flag:
            break
        if player == 20:
            try:
                pos = int(input("Enter a piece-position to move:"))
                if not InBoard(pos):
                    raise
                moves = GetPieceLegalMoves(board, pos)
                print(moves)
                new_pos = int(input("Enter a position to move to:"))
                if not InBoard(new_pos) or pos == new_pos:
                    raise
                if new_pos not in moves:
                    raise
                if board[new_pos] == 15:
                    end_flag = True
                board[pos], board[new_pos] = 0, board[pos]
                player = 10
                DisplayBoard(board)
            except:
                print("Invalid input, try again")
                continue
        if end_flag:
            break
    return True

two_player()
                    
                
