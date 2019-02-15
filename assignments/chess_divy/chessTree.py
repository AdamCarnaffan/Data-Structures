

class Tree:

    def __init__(self, board, player, player_board, opponent_board):
        self.board = []
        self.player = player
        self.p_board = player_board
        self.o_board = opponent_board
        self.next = []
        self.score = self.genscore()