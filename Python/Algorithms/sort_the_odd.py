"""You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

Examples
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

Link:https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python
"""


def sort_array(source_array):
    odd_numbers = sorted([num for num in source_array if num % 2 != 0])
    odd_index = 0
    res = []
    for num in source_array:
        if num % 2 != 0:
            res.append(odd_numbers[odd_index])
            odd_index += 1
        else:
            res.append(num)
    return res

# Smarter Solve
def sort_array(source_array):
    odd_numbers = sorted(
        [num for num in source_array if num % 2 != 0], reverse=True)
    return [num if num % 2 == 0 else odd_numbers.pop() for num in source_array]


print([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
print(sort_array([5, 8, 6, 3, 4]))
