from random import choice


class TTT:

    def __init__(self):
        self.board = [0, 0, 0, 0, 0, 0, 0 ,0 ,0]
        self.xcnt = 0
        self.ocnt = 0
        self.state = self.analyzeBoard()

    def display(self):
        str_board = []
        for i in range(0, 9, 1):
            if self.board[i] == 0:
                str_board += [str(i)]
            elif self.board[i] == 1:
                str_board += ["X"]
            elif self.board[i] == 2:
                str_board += ["O"]
        disp = " " + str_board[0] + " | " + str_board[1] + " | " + str_board[2]+"\n"
        disp += "---|---|---" + "\n"
        disp += " " + str_board[3] + " | " + str_board[4] + " | " + str_board[5]+"\n"
        disp += "---|---|---"  + "\n"
        disp += " " + str_board[6] + " | " + str_board[7] + " | " + str_board[8]
        print(disp)
        return True

    def analyzeBoard(self):  # -1 - draw, False - inplay, 1 - xwin, 2 - owin
        check = 0
        for i in range(0, 9, 3):
            for j in range(i, i + 3, 1):
                if self.board[j] != 0:
                    check += self.board[j]
                else:
                    check = 0
                    break
            if check == 3:
                return 1
            elif check == 6:
                return 2
        check = 0
        for i in range(0, 3, 1):
            for j in range(i, 9, 3):
                if self.board[j] != 0:
                    check += self.board[j]
                else:
                    check = 0
                    break
            if check == 3:
                return 1
            elif check == 6:
                return 2
        check = 0
        for i in range(0, 9, 4):
            if self.board[i] != 0:
                check += self.board[i]
            else:
                check = 0
                break
        if check == 3:
            return 1
        elif check == 6:
            return 2
        check = 0
        for i in range(2, 7, 2):
            if self.board[i] != 0:
                check += self.board[i]
            else:
                check = 0
                break
        if check == 3:
            return 1
        elif check == 6:
            return 2
        for i in self.board:
            if i == 0:
                return False
        return -1

    def input_move(self, move, position):
        if move == 1:
            self.xcnt += 1
        elif move == 2:
            self.ocnt += 1
        self.board[position] = move
        return True

    def ec_move(self, position):
        if type(position) != int:
            return False
        elif position < 0 or position > 8:
            return False
        elif self.board[position] != 0:
            return False
        return True

    def update_state(self):
        self.state = self.analyzeBoard()
        if self.state == 1:
            print("X WINS!")
            return False
        elif self.state == 2:
            print("O WINS")
            return False
        elif self.state == -1:
            print("The game has drawn!")
            return False
        return True

    def opposite_player(self, player):
        if player == 1:
            return 2
        else:
            return 1

    # Computer Functions
    def critical_move(self, player):
        cpu = TTT()
        cpu.board = list(self.board)
        winning = -1
        lossing = -1
        opponent = cpu.opposite_player(player)
        for i in range(0, 9, 1):
            if cpu.board[i] == 0:
                cpu.board[i] = player
                if cpu.analyzeBoard() == player:
                    winning = i
                    break
                else:
                    cpu.board[i] = opponent
                    if cpu.analyzeBoard() == opponent:
                        lossing = i
                cpu.board[i] = 0
        if winning != -1:
            self.board[winning] = player
        elif lossing != -1:
            self.board[lossing] = player
        else:
            return False
        return True

    def gen_move_options(self):
        options = []
        for i in range(0, 9, 1):
            if self.board[i] == 0:
                options += [i]
        return options

    def gen_randmove(self, player):
        self.board[choice(self.gen_move_options())] = player
        return True

    def make_move(self, player):
        if self.critical_move(player):
            return True
        self.gen_randmove(player)
        return True


def two_player():
    game = TTT()
    x_turn = True
    x = 1
    o = 2
    game.display()
    while True:
        if x_turn:
            try:
                x_pos = int(input("Enter a position for 'X': "))
                check = game.ec_move(x_pos)
                if not check:
                    raise
            except:
                print("Ops, that was an incorrect input!")
                continue
            game.input_move(x, x_pos)
            game.display()
            state = game.update_state()
            if state == False:
                break
            x_turn = False
        if not x_turn:
            try:
                o_pos = int(input("Enter a position for 'O': "))
                check = game.ec_move(o_pos)
                if not check:
                    raise
            except:
                print("Ops, that was an incorrect input!")
                continue
            game.input_move(o, o_pos)
            game.display()
            state = game.update_state()
            if state == False:
                break
            x_turn = True
    return True

def single_player():
    game = TTT()
    while True:
        try:
            human = int(input("Are you playing 'X'(1) or 'O'(2)?"))
            cpu = game.opposite_player(human)
            break
        except:
            print("Ops, that is not a valid player!")
    human_turn = False
    if human == 1:
        human_turn = True
    print("\nTIC TAC TOE")
    game.display()
    while True:
        if human_turn:
            try:
                hmove = int(input("Enter a position to play:"))
                check = game.ec_move(hmove)
                if not check:
                    raise
            except:
                print("Ops, that was an incorrect input!")
                continue
            game.input_move(human, hmove)
            print("\nPlayer move: ")
            game.display()
            state = game.update_state()
            if state == False:
                break
            human_turn = False
        if not human_turn:
            game.make_move(cpu)
            print("\nCPU move: ")
            game.display()
            state = game.update_state()
            if state == False:
                break
            human_turn = True
    return True

def cpu_vs_cpu():
    game = TTT()
    cpu1 = 1
    cpu2 = 2
    human_turn = True
    print("\nTIC TAC TOE")
    game.display()
    while True:
        if human_turn:
            game.make_move(cpu1)
            print("\nCPU1 move:")
            game.display()
            state = game.update_state()
            if state == False:
                break
            if state == False:
                break
            human_turn = False
        if not human_turn:
            game.make_move(cpu2)
            print("\nCPU2 move:")
            game.display()
            state = game.update_state()
            if state == False:
                break
            human_turn = True

def test():
    game = TTT()
    game.board = [1, 0, 1,
                2, 0, 0,
                1, 2, 2]
    print(game.critical_move(2))
    print(game.board)
    return True

single_player()




