"""
The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.
https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/python

"""



def max_sequence(arr):
    if not arr:
        return 0
    max_sum=0
    current_sum=0
    for n in arr:
        current_sum=max(0,current_sum+n)
        max_sum=max(max_sum,current_sum)
    return max_sum


print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])) # Shoule be 6
print(max_sequence([13,14,15,1])) # Shoule be 43
print(max_sequence([])) # Shoule be 0