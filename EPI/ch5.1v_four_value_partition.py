"""
Variation question 2
Given an array A of n objects with keys that takes one of four values, reorder the arrays so that all objects that have the same key appear together. Use O(1) space and O(n) time
"""
"""
For partition problem:
1. First initiate the placement index for each partition, all partitions starts from the beginning of the array except the last partition. It means the index for the first (n-1) partition moves forwards, but the n partition moves backwards.
2. Use the (n-1) partition value as equal value of quicksort (pivot value). It drive the index move forward, use its value to compare with pivot.  
3. If the first partiton move one step forward, all other partitions to (n-1) need also move forward. 
For example in the four_keys_partion example below:
 If A(partition_1) +=1, then A(partition_2) +=1, A(partition_3) +=1
 If A(partition_2) +=1, then A(partition_3) +=1
4. Number of swaps
partiton 1 moves one step forward, both partition 1 and 2 need to swap with partion 3
partition 2 moves one step forward, partition 2 needs to swap with partion 3
5. For the last partition, the index of it moves backward. In order to loop through all the elements of the array, the index is initiated as len(A), whcih is out of the array. If when a element with value > pivot, then we move the index one step backwards, then do the swap. 
"""

from typing import List

def four_keys_partition(A:List[int], first: int, second: int, third: int, forth: int)-> List:

    first_key, second_key, third_key, forth_key = 0, 0, 0, len(A)

    while (third_key < forth_key):
        if A[third_key] == first:
            A[first_key], A[third_key] = A[third_key], A[first_key]
            A[third_key], A[second_key] = A[second_key], A[third_key]
            first_key, second_key, third_key = first_key +1, second_key +1, third_key +1

        elif A[third_key] == second:
            A[second_key], A[third_key] = A[third_key], A[second_key]
            second_key, third_key = second_key + 1, third_key + 1
        elif A[third_key] == third:
            third_key +=1
        else:
            forth_key -=1
            A[forth_key], A[third_key] =A[third_key], A[forth_key]

    return A

print(four_keys_partition([2, 1, 1, 2, 4, 3, 1, 2, 3, 1, 2, 4, 2, 3], 1, 2, 3, 4))
