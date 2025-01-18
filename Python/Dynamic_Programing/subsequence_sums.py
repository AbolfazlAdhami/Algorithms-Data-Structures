def subsequence_sums(arr, s):
    prefix_sum = 0
    prefix_count = {0: 1}
    count = 0

    for num in arr:
        prefix_sum += num
        if prefix_sum - s in prefix_count:
            count += prefix_count[prefix_sum - s]
        if prefix_sum in prefix_count:
            prefix_count[prefix_sum] += 1
        else:
            prefix_count[prefix_sum] = 1
    print(prefix_count, prefix_sum)
    return count


print(subsequence_sums([1, 2, 3, -3, -2, -1], 0))  # Output: 3
print(subsequence_sums([1, 5, -2, 4, 0, -7, -3, 6], 4))  # Output: 4

"""
Given a sequence of integers named arr, find the number of continuous subsequences (sublist or subarray) in arr that sum up to s. A continuous subsequence can be defined as a sequence inbetween a start index and stop index (inclusive) of the sequence. For instance, [2, 3, 4] is a continuous subsequence of [1, 2, 3, 4, 5] , but [3, 5] and [4, 1] are not.

PERFORMANCE REQUIREMENTS

The length of arr is ≤ 10,000. The contents of arr can range from -10000 to 10000.

** Link:https://www.codewars.com/kata/60df63c6ce1e7b0023d4af5c/python

"""
