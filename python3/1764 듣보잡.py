input = __import__('sys').stdin.readline

n,m = map(int, input().split())
cant_listen = set()
cant_hear = set()
for i in range(n):
    val = input().rstrip()
    cant_listen.add(val)
for i in range(m):
    val = input().rstrip()
    cant_hear.add(val)

ans = cant_listen & cant_hear
ans = list(ans)
ans.sort()
print(len(ans))
for ele in ans:
    print(ele)