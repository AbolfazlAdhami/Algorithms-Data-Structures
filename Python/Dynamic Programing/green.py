# def green(n: int) -> int:
#     if n == 1:
#         return 1

#     greens = [1]
#     length = 1

#     while len(greens) < n:
#         modulus = 10 ** length

#         # Check candidates in current digit length
#         for candidate in range(10 ** (length - 1), modulus):
#             if (candidate ** 2) % modulus == candidate:
#                 greens.append(candidate)
#                 if len(greens) == n:
#                     return greens[-1]

#         length += 1

#     return greens[n - 1]



def green(n: int) -> int:
    greens = [1]

    for digits in range(1, 20):  # Enough for n <= 5000
        mod = 10 ** digits

        # Find all solutions to x^2 ≡ x (mod 10^digits)
        # Solutions come from extending previous solutions
        if digits == 1:
            candidates = [0, 1, 5, 6]
        else:
            prev_mod = 10 ** (digits - 1)
            candidates = []

            for prev in greens:
                if prev >= prev_mod:
                    continue

                for add in range(10):
                    candidate = prev + add * prev_mod
                    if candidate > 0 and (candidate ** 2) % mod == candidate:
                        candidates.append(candidate)

        for c in sorted(set(candidates)):
            if c > 0 and c not in greens:
                greens.append(c)

        greens.sort()

        if len(greens) >= n:
            return greens[n - 1]

    return greens[n - 1]



print(green(4))
print(green(12))
print(green(13))
print(green(100))


"""
This is a very simply formulated task. Let's call an integer number N 'green' if N² ends with all of the digits of N. Some examples:

5 is green, because 5² = 25 and 25 ends with 5.

11 is not green, because 11² = 121 and 121 does not end with 11.

376 is green, because 376² = 141376 and 141376 ends with 376.

Your task is to write a function green that returns the nth green number, starting with 1 - green (1) == 1

Input range
n <= 5000

"""
