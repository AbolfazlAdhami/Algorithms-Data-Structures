def binary_search(container, item, left, right):
    if left > right:
        return -1
    middle_index = (left+right)//2

    if container[middle_index] == item:
        return middle_index

    elif container[middle_index] > item:
        print('Checking left side of list...')
        return  binary_search(container, item, left, middle_index-1)
    elif container[middle_index] < item:
        print('Checking right side of list...')
        return  binary_search(container, item, middle_index-1, right)


nums = [1,2,3,4,5,6,7,8,9,10]
print(binary_search(nums, 2, 0, len(nums)-1))
print(binary_search(nums, 8, 0, len(nums)-1))
