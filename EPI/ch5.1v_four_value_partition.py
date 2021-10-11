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


def four_keys_partition(A:List[int], first_key: int, second_key: int, third_key: int, fourth_key:int)-> List:

    first, second, third, fourth = 0, 0, 0, len(A)

    while third < fourth:
        if A[third] == first_key:
            A[first], A[third] = A[third], A[first]
            A[third], A[second] = A[second], A[third]
            first, second, third = first + 1, second + 1, third + 1
        elif A[third] == second_key:
            A[second], A[third] = A[third], A[second]
            second, third = second + 1, third + 1
        elif A[third] == third_key:
            third += 1
        else:
            fourth -= 1
            A[fourth], A[third] =A[third], A[fourth]
    return A


array = [2, 1, 1, 2, 4, 3, 1, 2, 3, 1, 2, 4, 2, 3]
print(four_keys_partition(array, 1, 2, 3, 4))

