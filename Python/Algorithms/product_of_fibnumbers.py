def product_fib(num):
    a, b = 0, 1
    while a*b < num:
        a, b = b, a+b
    return [a, b, num == a*b]


"""
Description:

The Fibonacci numbers are the numbers in the following integer sequence (Fn): 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...

such that:
F(0)=1
F(1)=1
F(n)=F(n−1)+F(n−2)

Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying:
F(n)∗F(n+1)=prod

714 ---> (21, 34, true)
--> since F(8) = 21, F(9) = 34 and 714 = 21 * 34

800 --->  (34, 55, false)
--> since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55

Link : https://www.codewars.com/kata/5541f58a944b85ce6d00006a/python
"""
