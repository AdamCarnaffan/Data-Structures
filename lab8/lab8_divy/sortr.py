def sortr(array):
   n = len(array)
   if n <= 0:
      return True
   pos_neg = [[], []]
   for i in array:
      if i >= 0:
         pos_neg[0] += [i]
      else:
         pos_neg[1] += [abs(i)]
   helper_sortr(pos_neg[0], max(pos_neg[0]), 10)
   helper_sortr(pos_neg[1], max(pos_neg[1]), 10)
   n1 = len(pos_neg[1])
   for i in range(0, n1, 1):
      array[i] = pos_neg[1][n1 - 1 - i]*-1
   n0 = len(pos_neg[0])
   for i in range(0, n0, 1):
      array[n1 + i] = pos_neg[0][i]
   return True

def helper_sortr(array, largest_digit, tens):
   if largest_digit <= 0:
      return True
   buckets = []
   for i in range(0, 10, 1):
      buckets += [[]]
   for i in range(0, len(array), 1):
      value = array[i]
      while value >= tens:
         value -= tens
      buckets[value//(tens//10)] += [array[i]]
   counter = 0
   for i in range(0, len(buckets), 1):
      for j in range(0, len(buckets[i]), 1):
         array[counter] = buckets[i][j]
         counter += 1
   return helper_sortr(array, largest_digit//10, tens*10)

def main():
   array = [6, 10, 17, 19, 33, 34, 44, 65, 80, 94, -98, -89, -79, -57, -54, -53, -44, -29, -9, -2]
   print("Unsorted Array:", end = " ")
   print(array)
   print("length:", len(array))
   sortr(array)
   print("\nAfter Sort: ")
   print(array)
   return True

main()