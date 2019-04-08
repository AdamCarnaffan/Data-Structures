import numpy

def ex1():  # play with matrices
   matrix = numpy.zeros(shape=(10, 10))
   for i in range(matrix.shape[0]):
      for j in range(matrix.shape[1]):
         matrix[i][j] = i*(matrix.shape[0] - 1) + i + j
   col_5 = matrix[:, 4]  # get column 5
   row_5 = matrix[4]
   return True

def ex2():  # row-reduce matrix
   matrix = numpy.zeros(shape=(2, 2))
   for i in range(matrix.shape[0]):
      for j in range(matrix.shape[1]):
         matrix[i][j] = i*(matrix.shape[0] - 1) + i + j
   print(ex2_rred(matrix))
   return True

def ex2_rred(matrix):  # forward step of row-reduction
   if matrix.shape == (0, 0):
      return True
   max_extrema_i = 0
   for i in range(1, len(matrix[:, 0]), 1):
      if matrix[i][0] > matrix[max_extrema_i][0]:
         max_extrema_i = i
   matrix[0], matrix[max_extrema_i] = matrix[max_extrema_i].copy(), matrix[0].copy()
   divider = matrix[0][0]
   if divider == 0:
      return True
   matrix[0] = matrix[0]/divider
   for i in range(1, len(matrix[:, 0]), 1):
      matrix[i] += -1 * matrix[i][0] * matrix[0]
   ex2_rred((matrix[1:, 1:]))
   return matrix


def ex3():  # repersenting an array of 2-D vectors
   nx = ny = 3
   m1 = numpy.zeros(shape=(nx, nx, 2))
   # or simply create two arrays, one for x and one for y
   print(m1)
   return True

def ex4():  # on paper
   return True

def ex5():  # evolve - generate next state
   # generate an empty-template-variable for the next_state matrix
   # go through the matrix applying the difference equation to generate 
   # set previous matrix to equal new state matrix and return for further evolutions
   return True




def excercise_tester():  # essentially a main function
   #ex1()
   #ex2()
   #ex3()
   #ex4()
   #ex5()
   return True


excercise_tester()