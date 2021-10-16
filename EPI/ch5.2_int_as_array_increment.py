"""
Question 5.2

Write an non-negative integer as an array, add a given integer to the array and calculate the addition like adding it to an integer. For example, if your input is [2, 3, 9], add 1, the array should be updated to [2, 4, 0].
"""
"""
Explanation:
Do the same way like we do the addition problem.
Start from the last digit
"""
from typing import List


def plus_one(array: List[int]) -> List[int]:

    # Start addition from the last index
    array[-1] += 1

    for i in reversed(range(len(array))):
        if array[i] == 10:
            array[i] = 0
            array[i - 1] += 1
            # If the first element of array is greater than 10, append 0 to the end of array
            if array[0] == 10:
                array[0] = 1
                array.append(0)
        else:
            break

    return array


print(plus_one([2, 3, 9]))
print(plus_one([9, 9, 9]))
print(plus_one([9, 9, 8]))




