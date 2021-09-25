input = __import__('sys').stdin.readline
from collections import deque

a, b = map(int, input().split())

def solution(a, b):
    if a > b:
        return -1
    q = deque()
    q.append((a, 0))
    while q:
        cur, cnt = q.popleft()
        if cur == b:
            return cnt + 1
        for x in [2 * cur, 10*cur + 1]:
            if x <= b:
                q.append((x, cnt + 1))
    return -1

print(solution(a, b))