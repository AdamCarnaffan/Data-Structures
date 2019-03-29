from random import randint

def sortr(array):
   n = len(array)
   if n <= 0:
      return True
   largest_digit = max(array)
   tens = 10
   while largest_digit > 0:
      buckets = []
      for i in range(0, 10, 1):
         buckets += [[]]
      for i in range(0, n, 1):
         value = array[i]
         while value >= tens:
            value -= tens
         buckets[value//(tens//10)] += [array[i]]
      counter = 0
      for i in range(0, len(buckets), 1):
         for j in range(0, len(buckets[i]), 1):
            array[counter] = buckets[i][j]
            counter += 1
      largest_digit = largest_digit//10
      tens *= 10
   return True


def main():
   array = [randint(0, 1000) for i in range(100)]
   print("Unsorted Array:", end = " ")
   print(array)
   print("length:", len(array))
   sortr(array)
   print("\nAfter Sort: ")
   print(array)
   return True

main()