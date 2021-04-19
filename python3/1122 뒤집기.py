from collections import deque
import sys
input = sys.stdin.readline


a, b, k = map(int, input().split())

if a%2 == 1 and k % 2 == 0:
    print(-1)
elif a==0:
    print(0)
elif k == 0 or a+b<k:
    print(-1)
else:
    a_count, b_count = 0, 0
    ans = -1

    for i in range(100001):
        if i%2 == 1:
            # 0으로 되어있는 a개의 bit는 2k + 1 회 뒤집어줘야 함.
            a_count = i*a
        else:
            # 1로 되어있는 b개의 bit는 2k 회 뒤집어줘야 함
            b_count = i*b
        # total_count로 만들어진 상태는 a, b 모두 1인 상태
        total_count = a_count + b_count
        ret = i * k
        # k 개씩 i회 뒤집은 값의 범위는 a 이상이어야 하고,
        # a, b를 각각 뒤집어 준 횟수 이하여야 함.
        if a <= ret <= total_count:
            if (total_count - ret) % 2 ==0:
                ans = i
                break
    print(ans)