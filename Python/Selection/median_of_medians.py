def median_algorithm(nums, k):

    chunks = [nums[i:i+5]for i in range(0, len(nums), 5)]

    medians = [sorted(chunk)[len(chunk)//2]for chunk in chunks]
    pivot_value = sorted(medians)[len(medians)//2]

    # Partition Phase
    left_array = [n for n in nums if n < pivot_value]
    right_array = [m for m in nums if m > pivot_value]

    # selection phase
    pivot_index = len(left_array)

    if k < pivot_index:
        return median_algorithm(left_array, k)
    elif k > pivot_index:
        return median_algorithm(right_array, k-len(left_array)-1)
    else:
            return pivot_value


def select(nums, k):
    return median_algorithm(nums, k-1)


x = [1, -5, 0, 44, 10, 15, 20, 3, -1, 21, 22, 23, 24, 25, 26, 27, 28, 29]

print(select(x, 1))
print(select(x, 2))
print(select(x, 3))
print(select(x, 9))
print(select(x, 12))
print(select(x, len(x)))
