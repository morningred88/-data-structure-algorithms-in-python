"""
When working with arrays, we should take advantage of the fact that we can work efficiently on both ends
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