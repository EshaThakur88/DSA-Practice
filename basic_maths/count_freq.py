"""Problem Statement: Given an array, we have found the number of occurrences of each element in the array.

Examples
Example 1:
Input: arr[] = {10,5,10,15,10,5};
Output: 10  3
	            5  2
                15  1
Explanation: 10 occurs 3 times in the array
	      5 occurs 2 times in the array
              15 occurs 1 time in the array

Example2: 
Input: arr[] = {2,2,3,4,4,2};
Output: 2  3
	           3  1
               4  2
Explanation: 2 occurs 3 times in the array
	     3 occurs 1 time in the array
             4 occurs 2 time in the array
            """

from collections import defaultdict

def count_frequency(arr):

  freq_map=defaultdict(int)
  for i in arr:
    freq_map[i]+=1

  return freq_map

def main():
  arr=[2,2,3,4,4,2]
  ans=count_frequency(arr)
  for key, value in ans.items():
    print(f"{key}: {value}")

if __name__=="__main__":
  main()


"""
WITH NORMAL DICT:
def count_frequency(arr):
    freq_map = {}

    for i in arr:
        if i in freq_map:
            freq_map[i] += 1
        else:
            freq_map[i] = 1

    return freq_map


WITH NORMAL DICT BUT MORE CLEANER WITH .get() METHOD:
def count_frequency(arr):
    freq_map = {}

    for i in arr:
        freq_map[i] = freq_map.get(i, 0) + 1

    return freq_map

"""