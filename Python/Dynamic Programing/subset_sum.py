class SubsetSumProblem:
    def __init__(self, nums, m) -> None:
        self.nums = nums
        self.m = m
        self.S = [[False for _ in range(m+1)] for _ in range(len(nums)+1)]

    def solve(self):

        for i in range(len(self.nums)+1):
            self.S[i][0] = True

        for i in range(1, len(self.nums) + 1):
            for j in range(1, self.m+1):
                if j < self.nums[i-1]:
                    self.S[i][j] = self.S[i-1][j]
                else:
                    if self.S[i-1][j]:
                        self.S[i][j] = self.S[i-1][j]
                    else:
                        self.S[i][j] = self.S[i-1][j-self.nums[i-1]]

    def show_result(self):
        print("The problem is feasible: %s" % self.S[len(self.nums)][self.m])

        if not self.S[len(self.nums)][self.m]:
            return

        col_index = self.m
        row_index = len(self.nums)

        while col_index > 0 or row_index > 0:
            if self.S[row_index][col_index] == self.S[row_index-1][col_index]:
                row_index -= 1
            else:
                print('We take him : %d' % self.nums[row_index - 1])
                col_index = col_index - self.nums[row_index-1]
                row_index -= 1


if __name__ == '__main__':
    M = 15
    n = [9,4,1,3,5,6,14]

    problem = SubsetSumProblem(n, M)
    problem.solve()
    problem.show_result()
