# class word_split:

#     def split(self, phrase, list_of_words):

def word_split(phrase, list_of_words, output=[]):

    # If you default output=[], it would be overwritten for every recursion!
    if len(phrase) == 0:
        # print(output)
        return output

    # For every word in list
    for i in range(0, len(phrase)+1):
        prefix = phrase[:i]
        subfix = phrase[i:]

        if prefix in list_of_words:
            output.append(phrase[:i])
            return word_split(subfix, list_of_words, output)


# word_split('themanran',['clown','ran','man'])
# word_split('themanran', ['the', 'ran', 'man'])

# List of strings to represent a dictionary
dict = [
    "self", "th", "is", "famous", "Word",
    "break", "b", "r", "e", "a", "k", "br",
    "bre", "brea", "ak", "problem"
]

# input string
str = "Wordbreakproblem"

print(word_split(str, dict))
