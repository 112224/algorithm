input = __import__('sys').stdin.readline

n, m = map(int, input().split())
text = dict()
for _ in range(n):
    site, pw = input().split()
    text[site] = pw
for _ in range(m):
    site = input().rstrip()
    print(text[site])
