# 하나는 비트연산, 하나는 나머지
# dp로 풀자!
# 참고 코드 https://m.blog.naver.com/rdd573/221360289763

import sys
input = sys.stdin.readline

# 입력
N, a, b = map(int, input().split())

bits = [False] * 31

must_bit = 0
for _ in range(N):
    i = int(input())
    must_bit |= (1 << i)
    bits[i] = True

if a > 10000:
    ans = 0
    for i in range(a, b, a):
        if i & must_bit == must_bit:
            ans += 1
    print(ans)
else:
    dp = [[-1] * a for _ in range(31)]
    m = [0] * 32
    M = [0] * 32

    for i in range(31):
        bit = (1 << i)
        m[i] = m[i-1] + bit * bits[i]
        M[i] = M[i-1] + bit

    def memo(idx, modul):
        if idx == -1:
            return 1 if modul == 0 else 0

        if dp[idx][modul] != -1:
            return dp[idx][modul]

        ret = memo(idx-1, (modul + (1<<idx))%a)
        if not bits[idx]:
            ret += memo(idx-1, modul)
        dp[idx][modul] = ret
        return dp[idx][modul]

    def go(idx, val):
        if val + m[idx] > b:
            return 0
        if val + M[idx] <= b:
            return memo(idx, val % a)

        ret = go(idx - 1, val + (1 << idx))
        if not bits[idx]:
            ret += go(idx-1, val)
        return ret
    ans = go(30, 0)
    print(go(15, 0))