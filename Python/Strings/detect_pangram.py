# The quick brown fox jumps over the lazy dog
"""A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

Link: https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python
    """


def is_pangram(st):
    sentens = set(st.lower())
    count = 0
    for char in sentens:
        if char.isalpha():
            count += 1
    return count == 26


print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("This isn't a pangram!"))
print(is_pangram("abcdefghijklm opqrstuvwxyz"))
print(is_pangram("ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ"))
