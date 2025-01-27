"""A happy number is one where if you repeatedly square its digits and add them together, you eventually end up at 1.

For example:

7 -> 49 -> 97 -> 130 -> 10 -> 1 so 7 is a happy number.

42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 so 42 is not a happy number.

This can also be done with powers other than 2.

Complete the function that receives 2 arguments: the starting number and the exponent. It should return an array of numbers containing whatever loop it encounters, or [1] if it doesn't encounter any. This array should only include the numbers in the loop, not any that lead into the loop, and should repeat the first number as the last number e.g.:

[42, 20, 4, 16, 37, 58, 89, 145, 42]
The first number in the array should be where the loop is first encountered.

All function inputs will be positive integers, with the exponent being between 2 and 4.

Link: https://www.codewars.com/kata/578597a122542a7d24000018/python
"""


def is_happy(n, k):
    def get_next(n):
        total = 0
        while n > 0:
            digit = n % 10
            total += digit ** k
            n //= 10
        return total

    visited = {}
    sequence = []

    while n != 1:
        if n in visited:
            start_index = visited[n]
            return sequence[start_index:] + [n]
        visited[n] = len(sequence)
        sequence.append(n)
        n = get_next(n)

    return [1]


print(is_happy(42, 2))  # Output: [42, 20, 4, 16, 37, 58, 89, 145, 42]
print(is_happy(7, 2))   # Output: [1]


def is_happy_2(n):
    def get_next(number):
        return sum(int(digit) ** 2 for digit in str(number))

    seen = set()  # To track numbers we've already seen (to detect cycles)

    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)

    return n == 1


is_happy_2(91)
