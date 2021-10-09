"""
Question:
Write a program that takes an integer array (A) and an index i into A,  rearrange the elements such that all elements less than A[i] appear first,  at the beginning, followed by elements equal to A[i], then elements greater than A[i].
Requirement: The array arrange should not take any extra space from the memory, so O(1)

For example:
A =[5, 6, 2, 7, 8, 3, 6, 2, 4, 5], A[i]= 5, output [2, 3, 4, 5, 5, 6, 7, 8, 6] is a valid output
A =[5, 6, 2, 7, 8, 3, 6, 2, 4, 5], A[i]= 7, output [2, 3, 4, 5, 5, 6, 6, 7, 8] is a valid output
"""
"""
Explanation:
Think about the partition step in quicksort. A[i] as the pivot.

Since space complexity is O(1), it must be some swap step happened in order to achieve the rearrangement. 

Bruteforce:
First pass - move all the element less than A[i] to the first partition: Consider one element after another, starting from first element A[0]. Loop through and  find the first element first element A[j] less than A[i]. The move to the second element, find the next element A[j] less than A[i]. It tooks 2 for loops to find all the elements less than A[i].
Second pass- move all the element greater than A[i] to the last partition: We use the same method as for moving all the element less than A[i]. But this time starting from the last element of the array A[len(A)-1). It also tooks 2 for loops to find all the elements greater than A[i].
Time Complexity O(N^2), space complexity O(1)

Optimized Solution:
We will reorder the element into less than, equal to and greater than the pivot with single pass. We do this by maintaining four subarrays: bottom (element less than pivot), middle (element equals to pivot) unclassified, top (element greater than pivot). Initially, all elements are unclassified. We iterate through elements in unclassified, move elements into one of bottom, middle or top groups.
Time Complexity O(N), space complexity O(1)
"""

from typing import List

#Time Complexity O(N), space complexity O(1)
def dutch_flag_partition(A:List[int], pivot_index: int) -> None:
    pivot = A[pivot_index]
    smaller, equal, larger = 0, 0, len(A)-1
    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller +1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else:
            A[larger], A[equal] = A[equal], A[larger]
            larger -= 1
    return A


array = [1, 7, 3, 8, 2, 5, 1, 5, 1, 5, 2]
print(dutch_flag_partition(array, 5))
