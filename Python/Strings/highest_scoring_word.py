"""Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

For example, the score of abad is 8 (1 + 2 + 1 + 4).

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.

Link: https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/python
"""


def high(x):
    words = x.split()

    def word_score(word):
        return sum(ord(char) - ord('a') + 1 for char in word)
    highest_word = max(words, key=word_score)
    return highest_word


def high(x):
    return max(x.split(), key=lambda word: sum(ord(char)-ord('a') + 1 for char in word))


print(high("man i need a taxi up to ubud"))  # output: taxi
print(high("what time are we climbing up the volcano"))   # output: volcano
print(high("aaa b"))  # output: aaa
