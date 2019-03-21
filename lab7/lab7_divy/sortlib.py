def selection_sort(u):  # O(n) average swap-complexity
   if type(u) != list:  # ensure input is a list
      return False
   for i in range(0, len(u), 1):  # starting from index i
      minimum = i  # the starting index could hold the lowest value
      swap_need = False  # to avoid swapping the index i with itself
      for j in range(i + 1, len(u), 1):  # check the indices ahead of i for a lower value
         if u[j] < u[minimum]:  # if an index is lower than the previous minimum
            minimum = j  # update minimum to new minimum index
            swap_need = True  # swap is necessary, starting index i is not the lowest value
      if swap_need:  # swap the starting i position with the minimum 
         helper_swap_indices(u, i, minimum)
   return True

def heapify(u):
   n = len(u)
   for i in range(n - 1, 0, -1):  # build the heap from the bottom up, exclude 0 to avoid conditional
      parent = (i - 1)//2  # parent of index i
      helper_heap_shift_down(u, parent, n)  # shift down the parent as much as possible
   helper_heap_shift_down(u, 0, n)  # shift 0 manually to avoid conditional in the for-loop
   return True
   
def reheapify(u, end):  # end is in terms of logical-length (counting from 1)
   helper_swap_indices(u, 0, end - 1)  # move the biggest value to the end of the current range of the list
   helper_heap_shift_down(u, 0, end - 1)  # shift down the new 0 index value to correct position
   return True

def heap_sort(u):  # O(n*logn) average time-complexity
   if type(u) != list:  # ensure input is a list
      return False
   heapify(u)  # put list 'u' into a heap
   n = len(u)
   while n > 1:  # stop once the priority queue (PQ) is of length 1 or less
      reheapify(u, n)
      n -= 1  # decrement the size of the PQ
   return True

def merge_sort(u):  # O(n*logn) average time-complexity
   if type(u) != list:  # ensure input is a list
      return False
   helper_merge_sort(u, 0, len(u))  # helper to allow for recursive functionality
   return True

def quick_sort(u, initial, final): # O(n*logn) average time-complexity, final is inclusive
   if type(u) != list or initial >= final:  # ensure input is a list
      return False
   pIndex = partition(u, initial, final)  # partition at the given index
   quick_sort(u, initial, pIndex)  # sort left half of pivot (inclusive)
   quick_sort(u, pIndex + 1, final)  # sort right half of pivot

def partition(u, initial, final):
   pivot = u[(final - initial)//2 + initial]  # arbritray method of picking a pivot
   i, j = initial - 1, final + 1  # initialize indices
   while True:
      i += 1  # forces incrementation to prevent stalling on an index
      while u[i] < pivot:  # skip correctly placed indices
         i += 1
      j -= 1  # forces incrementation to prevent stalling on an index
      while u[j] > pivot:  # skip correctly placed indices
         j -= 1
      if i >= j:  # if i and j converge, return the position where j ended up (i could work too)
         break
      helper_swap_indices(u, i, j)  # swap the incorrectly located indices
   return j

# helper functions
def helper_merge_sort(u, start, end):  # from start to end (end is non-inclusive)
   middle = (end - start)//2 + start
   if middle == start:  # list is of size 1
      return False
   helper_merge_sort(u, start, middle)  # right list
   helper_merge_sort(u, middle, end)  # left list
   helper_merge_sort_combine_lists(u, start, middle, end)
   return True

def helper_merge_sort_combine_lists(u, start, middle, end):
   sL = []  # sorted_List
   left_i, right_i = start, middle
   while left_i != middle and right_i != end:
      if u[left_i] < u[right_i]:  # left list index data is less than right list index data
         sL += [u[left_i]]
         left_i += 1
      elif u[right_i] <= u[left_i]:  # the right index data is less than or equal to the left
         sL += [u[right_i]]
         right_i += 1
   if left_i == middle:  # determine which side was not fully sorted in sL
      side = right_i
      stop = end
   else:
      side = left_i
      stop = middle
   for left_overs in range(side, stop, 1):  # add the unsorted side into sL
      sL += [u[left_overs]]
   for i in range(start, end, 1):
      u[i] = sL[i - start]
   return True

def helper_heap_shift_down(u, index, end):
   while True:
      swap = index  # a break condition
      left_child = helper_heap_child(index, 1)  # left child of the index node
      if left_child >= end:  # break if left child is out of range
         break
      elif u[left_child] > u[swap]:  # check if the left child is greater than the parent
         swap = left_child
      if left_child + 1 < end and u[left_child + 1] > u[swap]:  # check if the right child exists
         swap = left_child + 1  # swap with the right child if it is the greater option
      if swap == index:  # break condition (children are both lower)
         break
      else:  # swap with the greater child_index and repeat
         helper_swap_indices(u, index, swap)
         index = swap
   return True
   
def helper_heap_child(index, lr):  # lr is 1 or 2
   return 2*index + lr

def helper_swap_indices(u, index_a, index_b):  # swap u[index_a] and u[index_b]
   swap = u[index_a]
   u[index_a] = u[index_b]
   u[index_b] = swap
   return True

def main():
   v1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
   v2 = [100, 1, 1000, 9, 8, 7, 2, 2000, 10]
   v3 = [100, 10, 1000, 9, 8, 7, 2, 6, 5, 2, 3, 1]

   print("SELECTION_SORT:")
   for i in [v1, v2, v3]:
      x = list(i)
      selection_sort(x)
      print(x)
   
   print("\nMERGE_SORT:")
   for i in [v1, v2, v3]:
      x = list(i)
      merge_sort(x)
      print(x)

   print("\nHEAP_SORT:")
   for i in [v1, v2, v3]:
      x = list(i)
      heap_sort(x)
      print(x)
   
   print("\nQUICK_SORT:")
   for i in [v1, v2, v3]:
      x = list(i)
      quick_sort(x, 0, len(x) - 1)
      print(x)
   return True

main()
