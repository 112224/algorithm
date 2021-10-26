input = __import__('sys').stdin.readline

# 맨 밑 자리 다 채우고
tc = int(input())
def isok(bit, i):
    return bit & (1<<i)

def check(r, bit):
    if r < 0: return True
    for j in range(m-1):
        if isok(bit, j) and isok(bit, j+1):
            return False
    for j in range(m):
        if isok(bit, j) and not able[r][j]:
            return False
    return True

for _ in range(tc):
    n, m = map(int, input().split())
    dp = [[0] * (1<<m) for _ in range(n)]
    able = [[True] * m for _ in range(n)]
    for i in range(n):
        ele = input().rstrip()
        for j in range(m):
            if ele[j] == 'x':
                able[i][j] = False

    for i in range(n):
        for bit in range(1<<m):
            if not check(i, bit): continue
            for pbit in range(1<<m):
                if not check(i - 1, pbit): continue
                cnt, flag = 0, True
                for j in range(m):
                    if isok(bit, j):
                        cnt += 1
                        if (j > 0 and isok(pbit, j-1)) or (j < m-1 and isok(pbit, j+1)):
                            flag = False
                            break
                if flag:
                    if i == 0: dp[i][bit] = max(dp[i][bit], cnt)
                    else: dp[i][bit] = max(dp[i][bit], dp[i - 1][pbit] + cnt)

    ans = 0
    for state in range(1<<m):
        if ans < dp[n-1][state]:
            ans = dp[n-1][state]
    print(ans)