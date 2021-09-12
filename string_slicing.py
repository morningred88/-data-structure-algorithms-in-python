def sliceString(s):
    # Specify the start index and the end index, separated by a colon, to return a part of the string. The end index is not included
    # llo, get the characters from position 2 to position 5 (not included)
    s = s[2:5]


# Slice from the start
    # hello world, whole string
    s = s[:]
    # hello, get the characters from the start to position 5 (not included)
    s = s[:5]

# Negative Indexing, the last character is -1
    # hello worl, does not include the last character
    s = s[:-1]
    # hello wor, does not include the last 2 characters
    s = s[:-2]

# Slice to the end
    # llo world, from position 2 all the way to the end
    s = s[2:]

# slice in steps
    s = s[::-1]  # dlrow olleh, move backwards in 1 step - reverse string
    s = s[::-2]  # drwolh, move backwords in 2 steps
    s = s[::+2]  # hlowrd, move forwards in 2 steps
    return s


if __name__ == '__main__':
    print(sliceString('hello world'))
