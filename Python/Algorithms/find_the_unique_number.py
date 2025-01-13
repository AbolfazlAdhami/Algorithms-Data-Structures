"""There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

Link:https://www.codewars.com/kata/585d7d5adb20cf33cb000235/python

"""


def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b

# Mine


def find_uniq(arr):
    freq = {}
    for n in arr:
        if n in freq:
            freq[n] += 1
        else:
            freq[n] = 1
    return min(freq, key=freq.get)


print(find_uniq([1, 1, 1, 2, 1, 1]))
