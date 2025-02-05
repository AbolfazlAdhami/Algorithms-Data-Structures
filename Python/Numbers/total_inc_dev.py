from math import comb


def total_inc_dec(x):
    if x == 0:
        return 1
    total = 10
    for k in range(2, x+1):
        inc = comb(k + 8, 8)

        dec = comb(k + 9, 9) - 1
        total += inc + dec - 9
    return total


print(total_inc_dec(1)) # Output:10
print(total_inc_dec(2)) # Output:100
print(total_inc_dec(3)) # Output:475
print(total_inc_dec(4)) # Output:1675


"""
Let's define increasing numbers as the numbers whose digits, read from left to right, are never less than the previous ones: 234559 is an example of increasing number.

Conversely, decreasing numbers have all the digits read from left to right so that no digits is bigger than the previous one: 97732 is an example of decreasing number.

You do not need to be the next Gauss to figure that all numbers with 1 or 2 digits are either increasing or decreasing: 00, 01, 02, ..., 98, 99 are all belonging to one of this categories (if not both, like 22 or 55): 101 is indeed the first number which does NOT fall into either of the categories. Same goes for all the numbers up to 109, while 110 is again a decreasing number.

Now your task is rather easy to declare (a bit less to perform): you have to build a function to return the total occurrences of all the increasing or decreasing numbers below 10 raised to the xth power (x will always be >= 0).    
    
    
*Link:https://www.codewars.com/kata/55b195a69a6cc409ba000053/python
"""
