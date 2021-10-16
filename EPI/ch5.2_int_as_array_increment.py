"""
Question 5.2

Write an non-negative integer as an array, add a given integer to the array and calculate the additional like adding it to an integer. For example, if your input is [2, 3, 9], add 1, the array should be updated to [2, 4, 0].
"""
from typing import List


def plus_one(array: List[int]) -> List[int]:

    array[-1] += 1

    for i in reversed(range(len(array))):
        if array[i] == 10:
            array[i] = 0
            array[i - 1] += 1
            if array[0] == 10:
                array[0] = 1
                array.append(0)
        else:
            break

    return array


print(plus_one([2, 3, 9]))
print(plus_one([9, 9, 9]))
print(plus_one([9, 9, 8]))




