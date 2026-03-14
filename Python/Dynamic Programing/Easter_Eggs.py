def height(n, m):
    if n == 0 or m == 0 or m == n:
        return 0
    k = min(m, n)
    result = 0
    current = 1
    for i in range(1, k+1):
        current = current*(m-i+1)//i
        result += current
    return result


# def height(n, m):
#     if n <= 0 or m <= 0:
#         return 0
#     k = min(n, m)
#     result = 0
#     c = 1
#     for i in range(1, k+1):
#         c = c * (m - i + 1) // i
#         result += c
#     return result
print(height(2, 14))  # Output: 105
print(height(7, 20))  # Output: 137979

"""One man (lets call him Eulampy) has a collection of some almost identical Fabergé eggs. One day his friend Tempter said to him:

 Do you see that skyscraper? And can you tell me a maximal floor that if you drop your egg from will not crack it?
 No, - said Eulampy.
 But if you give me N eggs, - says Tempter - I'l tell you an answer.
 Deal - said Eulampy. But I have one requirement before we start this: if I will see more than M falls of egg, my heart will be crushed instead of egg. So you have only M trys to throw eggs. Would you tell me an exact floor with this limitation?
*Link:https://www.codewars.com/kata/54cb771c9b30e8b5250011d4/python
"""
