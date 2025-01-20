def exp_sum(n):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[0][i] = 1
    for num in range(1, n + 1):
        for max_part in range(1, n + 1):
            if num >= max_part:
                dp[num][max_part] = dp[num - max_part][max_part] + \
                    dp[num][max_part - 1]
            else:
                dp[num][max_part] = dp[num][max_part - 1]

    return dp[n][n]


exp_sum(1)  # 1
exp_sum(2)  # 2  -> 1+1 , 2
exp_sum(3)  # 3 -> 1+1+1, 1+2, 3
exp_sum(4)  # 5 -> 1+1+1+1, 1+1+2, 1+3, 2+2, 4
exp_sum(5)  # 7 -> 1+1+1+1+1, 1+1+1+2, 1+1+3, 1+2+2, 1+4, 5, 2+3

exp_sum(10)  # 42
exp_sum(50)  # 204226
exp_sum(80)  # 15796476
exp_sum(100)  # 190569292

"""
How many ways can you make the sum of a number?

From wikipedia: https://en.wikipedia.org/wiki/Partition_(number_theory)

In number theory and combinatorics, a partition of a positive integer n, also called an integer partition, is a way of writing n as a sum of positive integers. Two sums that differ only in the order of their summands are considered the same partition. If order matters, the sum becomes a composition. For example, 4 can be partitioned in five distinct ways:
4
3 + 1
2 + 2
2 + 1 + 1
1 + 1 + 1 + 1

 P(n,k)=P(n−k,k)+P(n,k−1)

"""
