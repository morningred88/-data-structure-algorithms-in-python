"""
Question 5 Duplicate in an array

We want to find duplicates in one-dimensional array of intergers in O(n) running time where the integer values are smaller than the length of the array!

For example: if we have a list [1,2,3,1,5] then the algorithm can detect that there are a duplicate with value 1

Note: the array cannot contain items smaller than 0 and items with value greater than the size of the list. This is how we can achieve o(n) linear complexity!

"""


def findDuplicate(nums):

    # We can achieve O(N) linear running time where N=len(nums)
    for num in nums:
        if nums[abs(num)] >= 0:
            nums[abs(num)] = -nums[abs(num)]
        else:
            print(f'Repition found: {abs(num)}')


if __name__ == '__main__':

    # This method cannot handle value < 0 !!!
    # the maximum item is smaller than the size of the list
    n = [1, 2, 3, 1, 2, 4, 3, 5, 6, 7, 6]
    findDuplicate(n)
