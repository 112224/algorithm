input = __import__('sys').stdin.readline

dp = [0]* 1000000
dp[2] = 2
dp[3] = 0
dp[4] = dp[2]