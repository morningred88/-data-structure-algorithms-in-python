"""
Variation question:
Assuming the keys take one of three values, recorder the array so that the keys with the same value appear together. The order of the subarrays are not important. Use O(1) space and O(n) time.

"""
def three_key_partition (array, first_value, second_value, third_value):
    first_key, second_key, third_key = 0, 0, len(array)
    first, second, third = first_value, second_value, third_value
    while second_key < third_key:
        if array[second_key] == first:
            array[first_key], array[second_key] = array[second_key], array[first_key]
            first_key, second_key = first_key +1, second_key +1
        elif array[second_key] == second:
            second_key += 1
        else:
            third_key -= 1
            array[second_key], array[third_key] = array[third_key], array[second_key]
    return array

print(three_key_partition([2, 1, 1, 2, 3, 1, 2, 3, 2, 1, 2, 2, 3, 1, 3], 3, 1, 2))
