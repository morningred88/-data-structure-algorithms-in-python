from typing import List

def five_keys_partition(A:List[int], first: int, second: int, third: int, forth: int, fifth: int)-> List:

    first_key, second_key, third_key, forth_key, fifth_key = 0, 0, 0, 0, len(A)

    while (forth_key < fifth_key):
        if A[forth_key] == first:
            A[first_key], A[forth_key] = A[forth_key], A[first_key]
            A[forth_key], A[second_key] = A[second_key], A[forth_key]
            A[forth_key], A[third_key] = A[third_key], A[forth_key]
            first_key, second_key, third_key, forth_key= first_key +1, second_key +1, third_key +1, forth_key+1
        elif A[forth_key] == second:
            A[second_key], A[forth_key] = A[forth_key], A[second_key]
            A[forth_key], A[third_key] = A[third_key], A[forth_key]
            second_key, third_key, forth_key = second_key + 1, third_key + 1, forth_key+1
        elif A[forth_key] == third:
            A[forth_key], A[third_key] = A[third_key], A[forth_key]
            third_key, forth_key = third_key + 1, forth_key+1
        elif A[forth_key] == forth:
            forth_key +=1
        else:
            fifth_key -=1
            A[forth_key], A[fifth_key] =A[fifth_key], A[forth_key]

    return A

print(five_keys_partition([2, 1, 1, 2, 4, 3,5, 1, 2, 5, 1, 2, 4, 2, 3], 1, 2, 3, 4, 5))

