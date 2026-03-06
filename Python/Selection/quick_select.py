import random


class QuickSelect:
    def __init__(self, nums):
        self.nums = nums
        self.first_index = 0
        self.last_index = len(nums)-1

    def run(self, k):
        return self.select(self.first_index, self.last_index, k)

    def partition(self, first_index, last_index):
        pivot_index = random.randint(first_index, last_index)

        self.swap(pivot_index, last_index)

        for i in range(first_index, last_index):
            if self.nums[i] > self.nums[last_index]:
                self.swap(i, first_index)
                first_index += 1

        return first_index

    def swap(self, i, j):
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

    def select(self, first_index, last_index, k):

        pivot_index = self.partition(first_index, last_index)

        if pivot_index < k:
            return self.select(pivot_index+1, last_index, k)
        elif pivot_index > k:
            return self.select(first_index, pivot_index-1, k)

        return self.nums[pivot_index]


x = [2, 0, 5, -4, 100, 44, 3]
select = QuickSelect(x)
print(select.run(1))
 
