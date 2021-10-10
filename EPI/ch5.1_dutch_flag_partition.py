"""
Question:
Write a program that takes an integer array (A) and an index i into A,  rearrange the elements such that all elements less than A[i] appear first,  at the beginning, followed by elements equal to A[i], then elements greater than A[i].
Requirement: The array arrange should not take any extra space from the memory, so O(1)

Example 1:
A =[5, 6, 2, 7, 8, 3, 6, 2, 4, 5], A[0]= 5, output [2, 3, 4, 5, 5, 6, 7, 8, 6] is a valid output, [3, 2, 4, 5, 5, 6, 7, 8, 6] is also a valid output.
A =[5, 6, 2, 7, 8, 3, 6, 2, 4, 5], A[3]= 7, output [2, 3, 4, 5, 5, 6, 6, 7, 8] is a valid output
"""
"""
Explanation:
Think about the partition step in quicksort. A[i] as the pivot.

There are 4 apporaches to solve the problem

First approach:
Build 3 arrays, one less than the pivot, one equal to pivot and one array greater than pivot. Then we will write the 3 arrays back to array A. O(N) space and 0(N) time.

Second approach:
We can do this in place and keep the space constant. We don't want to create space that scales with out input. Improve the space complexity from O(N) to O(1). 
Since space complexity is O(1), it must be some swap step happened in order to achieve the rearrangement. 

We do this using 2 passes. First pass to find all the elements less than pivot. Second pass to find all the elements greater than pivot. 

First pass - move all the element less than A[i] to the first partition: Consider one element after another, starting from first element A[0]. Loop through and  find the first element first element A[j] less than A[i]. The move to the second element, find the next element A[j] less than A[i]. It tooks 2 for loops to find all the elements less than A[i].
Second pass- move all the element greater than A[i] to the last partition: We use the same method as for moving all the element less than A[i]. But this time starting from the last element of the array A[len(A)-1). It also tooks 2 for loops to find all the elements greater than A[i].
Time Complexity O(N^2), space complexity O(1)

Third approach: improve the time complexity from the second approach 
We still do this using 2 passes. But we will remember the placement indecies to repartition when we are going forward and backward. For example, first pass to find all the elements less than pivot. But we remember where place the smallest item. Second pass to find all the elements greater than pivot, but remember the larger placement pointer. Keep moving the smaller and larger placement pointer. 
Time Complexity O(N), space complexity O(1)

Forth approach: Optimized approach to 3. approach using single pass
We will reorder the element into less than, equal to and greater than the pivot with single pass. We do this by maintaining four subarrays: bottom (element less than pivot), middle (element equals to pivot) unclassified, top (element greater than pivot). Initially, all elements are unclassified. We iterate through elements in unclassified, move elements into one of bottom, middle or top groups.
Time Complexity O(N), space complexity O(1)

Reference:
The Dutch National Flag Problem (The Quicksort "Band-Aid")
Back To Back SWE
https://www.youtube.com/watch?v=ER4ivZosqCg

"""

from typing import List


# Time Complexity O(n), space complexity O(1)
def dutch_flag_partition(A:List[int], pivot_index: int) -> List:
    pivot = A[pivot_index]
    smaller, equal, larger = 0, 0, len(A)
    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            A[larger], A[equal] = A[equal], A[larger]
    return A

array = [1, 2, 3, 1, 2, 3]
print(dutch_flag_partition(array, 1))

