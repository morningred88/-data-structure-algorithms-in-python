"""
Question 1: Reversing an array in-place

We want to reverse a T[] array in O(n) linear time complexity and we want the algorithm to be in-place as well, so no additional memory can be used!
For example: input is [1,2,3,4,5] then the output is [5,4,3,2,1]
"""


def reverseArray(nums):
    # index pointing to the first item
    start_index = 0
    # index pointing to the last item
    end_index = len(nums)-1
    while end_index > start_index:
        # keep swapping the items
        nums[start_index], nums[end_index] = nums[end_index], nums[start_index]
        start_index += 1
        end_index -= 1


if __name__ == '__main__':
    n = [1, 2, 3, 4]
    reverseArray(n)
    print(n)
