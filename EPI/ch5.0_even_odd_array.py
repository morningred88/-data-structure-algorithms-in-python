"""
Question: Your input is integers, how can you recorder the input so that even entries appears first
"""
"""
Explanation: 
When working with arrays, we should take advantage of the fact that we can work efficiently on both ends
- Set the even index as the start point of the array
- Set odd index as the last index of the array
- Both index will meet in the middle
- If the value of the even index is an even number, move even index 1 step forward
- If the value of the even index is an odd number, swap it with the value from current odd index, then move odd index 1 step backward
"""

def even_sort(array) -> None:

    # Set the index of even value as 0, set index of odd value as the last index of array
    next_even, next_odd = 0, len(array) - 1

    while next_even < next_odd:
        if array[next_even] % 2 == 1:
            array[next_even], array[next_odd] = array[next_odd], array[next_even]
            next_odd -=1
        else:
            next_even += 1

    return array

print(even_sort ([1,2,3,4]))