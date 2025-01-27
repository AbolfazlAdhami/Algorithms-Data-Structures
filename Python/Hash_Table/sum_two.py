def two_sum(nums, target):
    num_map = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in num_map:
            return [num_map[diff], i]
        num_map[num] = i
    return num_map


print(two_sum([3, 2, 4], 6))
print(two_sum([2, 7, 11, 15], 9))
