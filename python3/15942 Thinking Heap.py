input = __import__('sys').stdin.readline
from collections import deque
n = int(input())
k, p = map(int, input().split())
# 배열의 p번째 수 k
ans = [-1] * (n+1)
visit = [False] * (n+10)

visit[k] = True
ans[p] = k
def get_up(idx, k):
    cnt = k - 1
    while idx > 1:
        idx >>= 1
        if cnt <= 0:
            return False
        visit[cnt] = True
        ans[idx] = cnt
        cnt -= 1
    return True

def get_path(idx):
    return [2*idx, 2*idx + 1]
def get_down(idx, k):
    cnt = k + 1
    q = deque()
    q.append(idx)

    while q:
        val = q.popleft()
        for ele in get_path(val):
            if 0 < ele <= n:
                if cnt > n:
                    return False
                visit[cnt] = True
                ans[ele] = cnt
                cnt += 1
                q.append(ele)
    return True


if not get_up(p, k) or not get_down(p, k):
    print(-1)
else:
    cnt = 1
    while visit[cnt]:
        cnt += 1
    for i in range(1, n+1):
        if ans[i] == -1:
            ans[i] = cnt
            visit[cnt] = True
            while visit[cnt]:
                cnt += 1
    for ele in ans[1:]:
        print(ele)