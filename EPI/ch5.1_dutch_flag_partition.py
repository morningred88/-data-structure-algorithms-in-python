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

"""