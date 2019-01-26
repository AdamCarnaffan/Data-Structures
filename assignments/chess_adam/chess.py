def make_board():
    board = []
    for i in range(0, 8, 1):
        for b in range(0, 8, 1):
            board = board + [0]
    return board

def add_pieces(board):
    final = list(board)
    pawnRow = 1
    row = 0
    for i in range(1, 3, 1):
        # Pawns
        for v in range(0, 8, 1):
            final[pawnRow*8+v] = 10*i
        # Knights
        final[8*row+1] = 10*i + 1
        final[8*row+6] = 10*i + 1
        # Bishops
        final[8*row+2] = 10*i + 2
        final[8*row+5] = 10*i + 2
        # Rooks
        final[8*row] = 10*i + 3
        final[8*row+7] = 10*i + 3
        # Queen
        final[8*row+3] = 10*i + 4
        # King
        final[8*row+4] = 10*i + 5
        pawnRow = 6
        row = 7
    return final

def interp_piece(value, odd):
    if value == 0:
        if odd:
            return "_"
        else:
            return "#"
    pieceCode = int(str(value)[1]) # String is always 2 long by here
    if pieceCode == 0:
        return "P"
    elif pieceCode == 1:
        return "N"
    elif pieceCode == 2:
        return "B" # I know this isn't the first letter
    elif pieceCode == 3:
        return "R"
    elif pieceCode == 4:
        return "Q"
    elif pieceCode == 5:
        return "K"


def invert_list(l):
    if len(l) < 1:
        return []
    return [l[len(l)-1]] + invert_list(l[0:len(l)-1])

def display_baord(board):
    inv = invert_list(board)
    for y in range(0, 8, 1):
        line = ""
        for x in range(0, 8, 1):
            line = line + interp_piece(inv[y*8+x], (y + x) % 2)
        print(line)
    return True

def main():
    v = make_board()
    v = add_pieces(v)
    display_baord(v)
    return True

main()
    