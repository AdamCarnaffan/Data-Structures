#for genrandommove function
import random

#####
########## TIC TAC TOE GAME ########## LAB 1 ##########
#####

def genBoard():
   unoccupiedboard = [0,0,0,0,0,0,0,0,0]
   return unoccupiedboard

def printBoard(T):
#Error Check
   if not type(T) == list:
      return False

   if not len(T) == 9:
      return False

   for val in T:
      if not val == 0 and not val == 1 and  not val == 2:
         return False

   board = list(T)
   T2 = list(T)
#Check List Values
   for cnt in range(0,len(T2),1):
      if T2[cnt] == 0:
         board[cnt] = str(cnt)

      elif T2[cnt] == 1:
         board[cnt] = "X"

      elif T2[cnt] == 2:
         board[cnt] = "O"
#Print Board
   print(" " + board[0] + " | " + board[1] + " | " + board[2])
   print("---|---|---")
   print(" " + board[3] + " | " + board[4] + " | " + board[5])
   print("---|---|---")
   print(" " + board[6] + " | " + board[7] + " | " + board[8])

   return True

def analyzeBoard(T):
#Errors
   if not type(T) == list:
      return -1

   if not len(T) == 9:
      return -1

   for val in T:
      if not val == 0 and not val == 1 and not val == 2:
         return -1
   #Too many x's or o'x than there should be in the game (checker).   
   #NEED TO COMMENT IT OUT BECAUSE THIS ERROR CHECK DOESNT NOT MESH WELL WITH LAB 2
   #exstotal = 0
   #ohstotal = 0
   #for picks in T: 
      #if picks == 1:
         #exstotal = exstotal + 1
      #elif picks == 2:
         #ohstotal = ohstotal + 1
   #remain = exstotal - ohstotal
   #if (remain < 0) or (remain > 1):
      #print("error check - too many x or o 'S")
      #return -1

#WINS

   xwin = False
   owin = False

   #Columns
   for cval in range(0,3,1):
      ctotal = 0
      czero = False
      for column in range(cval,9,3):
         if T[column] == 0:
            czero = True
            break
         else:
            ctotal = ctotal + T[column]
      if not czero:
         if ctotal == 3:
            xwin = True
            return 1
         elif ctotal == 6:
            owin = True
            return 2
 #Rows
   for rval in range(0,9,3):
      rtotal = 0
      rzero = False
      for row in range(rval,(rval + 3),1):
         if T[row] == 0:
            rzero = True
            break
         else:
            rtotal = rtotal + T[row]
      if not rzero:
         if rtotal == 3:
            xwin = True
            return 1
         elif rtotal == 6:
            owin = True
            return 2
   #Diagonals
   if (T[0] == 1) and (T[4] == 1) and (T[8] == 1):
      xwin = True
      return 1

   if (T[0] == 2) and (T[4] == 2) and (T[8] == 2):
      owin = True
      return 2

   if (T[6] == 1) and (T[4] == 1) and (T[2] == 1):
      xwin = True
      return 1

   if (T[6] == 2) and (T[4] == 2) and (T[2] == 2):
      owin = True
      return 2

   if (xwin == True) and (owin == True):
      return -1

   #Board in play
   for zero in T:
      if zero == 0:
         return 0
   #Draw
   return 3
def errorcheck(T,player):
   if len(T) != 9:
      return True

   if type(T) != list:
      return True

   if not (player == 1) and not (player == 2):
      return True

   for val in T:
      if (val != 0) and (val!= 1) and (val != 2):
         return True


def genNonLoser(T,player):
#ERROR Check
   if errorcheck(T,player) == True:
      return -1

#Analyzing Board for Non-Lose
   copyT = list(T)

   index = 0
   for val in copyT:
      if val == 0:
   #Playerx -- 1
         if player == 1:
            copyT[index] = 2
            if analyzeBoard(copyT) == 2:
               copyT[index] = 1
               return index
            else:
               copyT[index] = 0
   #Playero -- 2
         elif player == 2:
            copyT[index] = 1
            if analyzeBoard(copyT) == 1:
               copyT[index] = 2
               return index
            else:
               copyT[index] = 0
      index += 1

   return -1

def genWinningMove(T,player):
#ERROR CHECKER
   if errorcheck(T,player) == True:
      return -1

#ANALYZE BOARD FOR PLAYER MOVE AND IF IT EQUAL WINNING MOVE
   copyT = list(T)

   index = 0
   for val in copyT:
      if val == 0:
   #Playerx -- 1
         if player == 1:
            copyT[index] = 1
            if analyzeBoard(copyT) == 1:
               return index
            else:
               copyT[index] = 0
   #Playero -- 2
         elif player == 2:
            copyT[index] = 2
            if analyzeBoard(copyT) == 2:
               return index
            else:
               copyT[index] = 0
      index += 1

   return -1


def genRandomMove(T,player):
   copyT = list(T)

#ERROR CHECKER
   if errorcheck(T,player) == True:
      return -1

   indexchecker = 0
   count = 0
   while indexchecker <=8:
      if copyT[indexchecker] !=0:
         indexchecker += 1
      elif copyT[indexchecker] == 0:
         indexchecker += 1
         count += 1

   if count == 0:
      return -1

#EMPTY SPOT PICKER - LOOPS THROUGH RANDOM INTEGERS BETWEEN 0 AND 8 UNTIL ONE OF THEM FINALLY DOESNT EQUAL 0; the previous lines of code ensure tthat copyT does have a 0 in it, else count == 0 and -1 is returned
   loop = 10
   while loop > 2:
      index = random.randint(0,8)
      if copyT[index] == 0:
         return index

   return -1


def genOpenMove(T,player):
#ERROR CHECKER
   if errorcheck(T,player) == True:
      return -1

#GENERATE A MOVE 
   copyT = list(T)

   index = 0
   for val in copyT:
      if val == 0:
         return index
      index += 1

   return -1