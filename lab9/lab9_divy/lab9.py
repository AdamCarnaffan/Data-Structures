def quick_sort(u, initial, final):
   if final - initial <= 0:  # partitioned list has cardinality of 1, by definition sorted
      return True
   pivot_index = partition(u, initial, final)  # sort & obtain the index to split u
   quick_sort(u, initial, pivot_index - 1)  # recursivly repeat for each half of u still unsorted about p_index
   quick_sort(u, pivot_index + 1, final)
   return True

def partition(u, initial, final):
   pivot_value = u[final]
   lowest = i = initial
   while i != final:
      while u[lowest] <= pivot_value and lowest < final:
         lowest += 1
      i = lowest
      while u[i] > pivot_value and i < final:
         i += 1
      swap = u[lowest]
      u[lowest] = u[i]
      u[i] = swap
   return lowest

def hanoi(n, start, middle, final):
   if n <= 0:
      return True
   hanoi(n - 1, start, final, middle)  # move to midde
   final.append(start.pop())  # append to final
   hanoi(n - 1, middle, start, final)  # move from middle to final
   print(start, middle, final)
   return True

def helper_test_quick_sort():  # testing function for quicksort - technically not a helper function
   print("\nQUICK SORT")
   v1 = [10,9,8,7,6,5,4,3,2,1,0]  # test cases
   v2 = [100,1,1000,9,8,7,2,2000,10]
   v3 = [100,10,1000,9,8,7,2,6,5,2,3,1]
   expect = ["[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]",  # hand-sorted answers
   "[1, 2, 7, 8, 9, 10, 100, 1000, 2000]", 
   "[1, 2, 2, 3, 5, 6, 7, 8, 9, 10, 100, 1000]"]
   test_lists = [v1, v2, v3]
   for i in range(0, len(test_lists), 1):  # test the 3 test cases w/ fancy output
      test = list(test_lists[i])
      print("Input:", test)
      quick_sort(test, 0, len(test) - 1)
      print("Answer:", expect[i])
      print("Output:", test, "\n")
   return True

def helper_test_hanoi():  # testing function for hanoi - technically not a helper function
   print("\nBefore HANOI:")
   start_tower = [i for i in range(5)]  # generate a start tower
   middle_tower = []
   final_tower = []
   print("Starting Tower:", start_tower)  # middle and final should be empty
   print("Middle Tower:", middle_tower)
   print("Final Tower:", final_tower)
   hanoi(len(start_tower), start_tower, middle_tower, final_tower)  # hanoi from start to final
   print("\nAfter HANOI:")  # start and middle should be empty
   print("Starting Tower:", start_tower)
   print("Middle Tower:", middle_tower)
   print("Final Tower:", final_tower)
   return True

def main():
   helper_test_quick_sort()
   helper_test_hanoi()
   return True


main()