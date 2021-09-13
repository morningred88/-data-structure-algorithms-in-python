"""
Question 4: Anagram checking

Construct an algorith to check whether two words (or phrases) are anagrams or not
"An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once"
"""


def isAnagram(str1, str2):
    # If the length of the strings differs - they are not anagrams
    if len(str1) != len(str2):
        return False
    # Sort the characters of the strings and then compare the characters with the same index
    # This is the bottleneck because it O(nlogn)
    str1 = sorted(str1)
    str2 = sorted(str2)

    # after that we have to check the charactors with the same indexes
    # O(n) running time
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    return True
    # Overall running time is O(nlogn) + O(n) = O(nlogn)


if __name__ == '__main__':
    print(isAnagram('fluster', 'restful'))
    print(isAnagram('follow', 'pillow'))
