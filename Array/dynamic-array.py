"""
Don't need to specify how large an array is beforehand
A list instance often has greater capacity than current length
If elements keep getting appended, eventually this extra space runs out

(a) create a new array B 
(b) store elements of A in B 
(c) reassign refence A to the new array B

A commonl used rule is for the new array to have twice the capacity of the existing array that has been filled. 
"""
import sys


def getArraySize(n):
    # Set a empty array
    data = []
    for i in range(n):
        # Number of elements
        a = len(data)

        # Actual size in memory in Bytes
        b = sys.getsizeof(data)

        # Version 3.6+: Use a formatted string literal, f-string for short
        print(f'Length: {a}; Size in bytes: {b}')
        # string.format(), variation in older python version
        #print('Length: {}; Size in bytes: {}'.format(a, b))

        # increase length by one, append the particular integer into the list
        data.append(n)


if __name__ == '__main__':
    getArraySize(10)

"""
Results:
Length: 0
Size in bytes: 56
Length: 1
Size in bytes: 88
Length: 2
Size in bytes: 88
Length: 3
Size in bytes: 88
Length: 4
Size in bytes: 88
Length: 5
Size in bytes: 120
Length: 6
Size in bytes: 120
Length: 7
Size in bytes: 120
Length: 8
Size in bytes: 120
Length: 9
Size in bytes: 184
"""
