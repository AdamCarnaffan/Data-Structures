import random

class TicTacToe:

   def __init__(self):
     self.gen_baord()
     self.playing = 1
     self.movesMade = 0
     self.useAI = False

   def gen_baord(self):
     self.board = [0,0,0,0,0,0,0,0,0]
     return True
   
   def display(self):
     position = 0
     divisorLine = "---|---|---"
     for line in range(1,6,1):
       if line % 2 == 1:
         lineStr = ""
         for pos in range(position,position + 3,1):
            if self.board[pos] == 1:
              lineStr = lineStr + " X "
            elif self.board[pos] == 2:
              lineStr = lineStr + " O "
            else: # print position if is not taken
              lineStr = lineStr + " " + str(pos) + " "
            if pos < position + 2: # check if not last val
              lineStr = lineStr + "|"
         position = position + 3
         print(lineStr)
       else:
         print(divisorLine)
     return True # ran successfully to finish

   def toggle_ai(self):
     self.useAI = False if self.useAI else True
     return True

   def duplicate(self):
     dup = TicTacToe()
     dup.board = list(self.board)
     dup.playing = self.playing
     dup.movesMade = self.movesMade
     dup.useAI = self.useAI
     return dup

   def generate_move(self):
     moves = self.get_open_moves()
     if len(moves) == 1:
       return moves[0]
     results = []
     for v in moves:
       results = results + [self.simulate_move(v, False)]
     ind = 0
     for v in moves:
       res = self.simulate_move(v, True)
       if res == self.playing:
         results[ind] = res
       ind = ind + 1
     ind = 0
     nonLoss = []
     enemy = 2 if self.playing == 1 else 1
     for r in results:
       if r == self.playing:
         return moves[ind]
       elif r == enemy:
         nonLoss = nonLoss + [moves[ind]]
       ind = ind + 1
     if len(nonLoss) > 0:
       return nonLoss[0]
     return moves[random.randint(0, len(moves)-1)]

   def simulate_move(self, pos, playAsSelf):
     new = self.duplicate()
     if not playAsSelf:
       new.change_turn()
     new.toggle_ai()
     r = new.process_turn(pos)[1]
     return r

   def get_open_moves(self):
     avail = []
     pos = 0
     for v in self.board:
       if v == 0:
         avail = avail + [pos]
       pos = pos + 1
     return avail


   def change_turn(self):
     self.playing = 2 if self.playing == 1 else 1
     return True

   def validate_pos(self, pos):
     if pos < 0 or pos > 8:
       return False
     return True

   def process_turn(self, pos):
     if self.make_move(pos):
       self.movesMade = self.movesMade + 1
       win = self.check_win(pos)
       self.change_turn()
       if self.useAI and self.playing == 2 and win == 0 and self.movesMade <= 8:
         move = self.generate_move()
         print("TRYING " + str(move))
         win = self.process_turn(move)[1]
       if win == 0 and self.movesMade > 8:
         win = -1
       return [True, win]
     return [False, 0]

   def make_move(self, pos):
     if self.validate_pos(pos):
       if self.check_move(pos):
         self.board[pos] = self.playing
         return True
     return False

   def check_move(self, pos):
     if self.board[pos] == 0:
       return True
     return False

   def check_win(self, pos):
     x = pos % 3
     y = int((pos - x)/3)
     # Check vertical
     if self.board[0+x] == self.board[3+x] == self.board[6+x]:
       return self.playing
     # Check Horizontal
     if self.board[y*3] == self.board[y*3+1] == self.board[y*3+2]:
       return self.playing
     # Check Diagonal (if exists)
     if (x == y) or (x % 2 == 0 and y % 2 == 0):
       third = 0
       if x == y == 0:
         third = 8
       elif x == 2:
         third = 6
       elif y == 2:
         third = 2
       if self.board[4] == self.board[y*3+x] == self.board[third]:
         return self.playing
     return 0

def main():
   game = TicTacToe()
   game.toggle_ai()
   game.display()
   while True:
     move = input()
     res = game.process_turn(int(move))
     try:
       pass
     except:
       print("ERR: The position input was invalid")
       continue
     if not res[0]:
       print("ERR: The move could not be performed")
     game.display()
     if res[1] > 0:
       print("Player " + str(res[1]) + " has won!")
       break
     elif res[1] == -1:
       print("DRAW!")
       break
   return True

main()