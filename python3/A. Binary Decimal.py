import sys
input = sys.stdin.readline

ans = []

tc = int(input())

for _ in range(tc):
    num = list(input().strip())
    num = [int(x) for x in num]
    ans.append(max(num))
print('\n'.join(map(str,ans)))
