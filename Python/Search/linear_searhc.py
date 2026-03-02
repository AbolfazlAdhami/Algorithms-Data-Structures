def linear_search(container, item):
    for index in range(len(container)):
        if container[index] == item:
            return index
    return -1


nums = [10, 4, 2, 0, 22, 30, 99]

print(linear_search(nums,22))
print(linear_search(nums,23))
