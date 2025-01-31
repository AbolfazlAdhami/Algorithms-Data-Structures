from bisect import bisect_left


def smaller(arr):
    result = []
    sorted_list = []

    for num in reversed(arr):
        index = bisect_left(sorted_list, num)
        result.append(index)
        sorted_list.insert(index, num)

    return result[::-1]


# print(smaller([5, 4, 3, 2, 1]))  # Output [0,1,2,3,4]
# print(smaller([1, 2, 3]))  # Output [0,0,0]

"""
Write a function that given, an array arr, returns an array containing at each index i the amount of numbers that are smaller than arr[i] to the right.

For example:

* Input [5, 4, 3, 2, 1] => Output [4, 3, 2, 1, 0]
* Input [1, 2, 0] => Output [1, 1, 0]
    
Link:https://www.codewars.com/kata/56a1c074f87bc2201200002e/python
    """


def count_smaller(arr):
    if not arr:
        return []
    sorted_arr = sorted(set(arr))
    rank_map = {num: i + 1 for i, num in enumerate(sorted_arr)}

    def update(bit, index, value):
        while index < len(bit):
            bit[index] += value
            index += index & -index

    def query(bit, index):
        sum_ = 0
        while index > 0:
            sum_ += bit[index]
            index -= index & -index
        return sum_
    bit = [0] * (len(sorted_arr) + 1)
    result = []

    for num in reversed(arr):
        rank = rank_map[num]
        result.append(query(bit, rank - 1))
        update(bit, rank, 1)

    return result[::-1]


print(count_smaller([5, 4, 7, 9, 2, 4, 1, 4, 5, 6]))


"""
        
        
* Link: https://www.codewars.com/kata/56a1c63f3bc6827e13000006/train/python
"""
