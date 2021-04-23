import sys
from functools import cmp_to_key
input = sys.stdin.readline

k, n = map(int, input().split())
ans = []

for _ in range(k):
    ch = int(input())
    ans.append(ch)

tmp = max(ans)
for _ in range(n-k):
    ans.append(tmp)


def compare(a, b):
    return int(str(b)+str(a)) - int(str(a)+str(b))


ans = sorted(ans, key= cmp_to_key(compare))
print(''.join(map(str,ans)))