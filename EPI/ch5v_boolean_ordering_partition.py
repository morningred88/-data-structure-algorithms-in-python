"""
Variation problem 4:
Given an array A of n objects with Boolean-valued key, reorder the array so that all objects false appear first.
The relative ordering of key true should not be change.
Use O(1) additional space and O(N) time.
"""

from typing import List


def rearrange_boolean_forward(A:List[bool]) -> List:

    # Initialize the placement position (index) of the 2 subarrays
    false, true = 0, 0
    for i in range(len(A)):
        if A[i]:
            true += 1
        else:
            A[true], A[false] = A[false], A[true]
            false, true = false + 1, true + 1

    return A


def rearrange_boolean_forward_test(A:List[int]) -> List:

    # Initialize the placement position (index) of the 2 subarrays
    false, true = 0, 0
    for i in range(len(A)):
        if A[i] != 0:
            true += 1
        else:
            A[true], A[false] = A[false], A[true]
            false, true = false + 1, true + 1

    return A


def rearrange_boolean_backward(A:List[bool]) -> List:

    # Initialize the placement position (index) of the 2 subarrays
    false, true = len(A) - 1, len(A) - 1
    for i in reversed(range(0, len(A))):
        if not A[i]:
            false -= 1
        else:
            A[true], A[false] = A[false], A[true]
            false, true = false - 1, true - 1

    return A


# This method is used for testing the method rearrange_boolean_backward(A)
def rearrange_boolean_backward_test(A:List[int]) -> List:

    # Initialize the placement position (index) of the 2 subarrays
    false, true = len(A)-1, len(A)-1
    for i in reversed(range(0, len(A))):
        if A[i] == 0:
            false -= 1
        else:
            A[true], A[false] = A[false], A[true]
            false, true = false - 1, true - 1

    return A


array = [False, True, True, False]
print(rearrange_boolean_forward(array))
array_test =[0, 1, 2, 0]
print(rearrange_boolean_forward_test(array_test))

# array = [False, True, True, False]
# print(rearrange_boolean_backward(array))
# array_test =[0, 1, 2, 0]
# print(rearrange_boolean_backward_test(array_test))

