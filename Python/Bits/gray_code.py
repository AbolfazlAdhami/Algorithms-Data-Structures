def bin2gray(bits):
    gray = [bits[0]]
    for i in range(1, len(bits)):
        gray.append(bits[i] ^ bits[i-1])
    return gray


def gray2bin(bits):
    binary = [bits[0]]
    for i in range(1, len(bits)):
        binary.append(binary[i-1] ^ bits[i])
    return binary


print(bin2gray([1, 0, 1]))  # Output: [1, 1, 1]
print(gray2bin([1, 1, 1]))  # Output: [1, 0, 1]


"""
Gray code is a form of binary encoding where transitions between consecutive numbers differ by only one bit. This is a useful encoding for reducing hardware data hazards with values that change rapidly and/or connect to slower hardware as inputs. It is also useful for generating inputs for Karnaugh maps.

Here is an exemple of what the code look like:

0:    0000
1:    0001
2:    0011
3:    0010
4:    0110
5:    0111
6:    0101
7:    0100
8:    1100
The goal of this kata is to build two function bin2gray and gray2bin wich will convert natural binary to Gray Code and vice-versa. We will use the "binary reflected Gray code". The input and output will be arrays of 0 and 1, MSB at index 0.

There are "simple" formula to implement these functions. It is a very interesting exercise to find them by yourself. Otherwise you can look here: http://mathworld.wolfram.com/GrayCode.html for formula and more informations.

All input will be correct binary arrays.

Link: https://www.codewars.com/kata/5416ce834c2460b4d300042d/python
"""
