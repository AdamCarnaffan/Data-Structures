def DisplayBoard(board):
   display = ""
   for i in range(7, -1, -1):
      for j in range(8 * i, 8 * i + 8, 1): 
         piece = board[j]
         if piece == 0:
            if (j//8) % 2 == 0:
               if j % 2 == 0:
                  display += "_"
               else:
                  display += "#"
            else:
               if j % 2 == 0:
                  display += "#"
               else:
                  display += "_"
         elif piece <= 15:
            if piece == 10:
               display += "P"
            elif piece == 11:
               display += "N"
            elif piece == 12:
               display += "B"
            elif piece == 13:
               display += "R"
            elif piece == 14:
               display += "Q"
            else:
               display += "K"
         elif piece <= 25:
            if piece == 20:
               display += "p"
            elif piece == 21:
               display += "n"
            elif piece == 22:
               display += "b"
            elif piece == 23:
               display += "r"
            elif piece == 24:
               display += "q"
            else:
               display += "k"
         if j == i*8 + 7:
            display += "\n"
         else:
            display += " "
   print(display)
   return True

def printBoard(board):
   accum="---- BLACK SIDE ----\n"
   max=63
   for j in range(0,8,1):
      for i in range(max-j*8,max-j*8-8,-1):
         accum=accum+'{0: <5}'.format(board[i])
      accum=accum+"\n"
   accum=accum+"---- WHITE SIDE ----"
   print(accum)
   return True

def indexBoard():
   accum="---- BLACK SIDE ----\n"
   max=63
   for j in range(0,8,1):
      for i in range(max-j*8,max-j*8-8,-1):
         accum=accum+'{0: <5}'.format(i)
      accum=accum+"\n"
   accum=accum+"---- WHITE SIDE ----"
   print(accum)
   return True
      
