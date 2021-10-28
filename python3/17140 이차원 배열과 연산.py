input = __import__('sys').stdin.readline
from collections import defaultdict as dt
from operator import itemgetter

r, c, k = map(int, input().split())
r, c = r - 1, c - 1
board = [list(map(int, input().split())) for _ in range(3)]

for ele in board:
    print(ele)
print()
for ele in list(map(list, zip(*board))):
    print(ele)
print()
for ele in list(zip(*board)):
    print(ele)

def sort_():
    # 각 행에 대해 정렬
    M = -1
    L = len(board)
    for i in range(L):
        cnt = dt(int)
        for ele in board[i]:
            if ele == 0: continue
            cnt[ele] += 1
        tmp = [[k, v] for k, v in cnt.items()]
        tmp.sort(key=itemgetter(1, 0))
        tmp = [x for ele in tmp for x in ele]
        board[i] = tmp[:100]
        if M < len(board[i]):
            M = len(board[i])

    for i in range(L):
        if len(board[i]) < M:
            board[i].extend([0] * (M - len(board[i])))


ans = -1
for idx in range(101):
    if r < len(board) and c < len(board[0]) and board[r][c] == k:
        ans = idx
        break
    if len(board) >= len(board[0]):
        sort_()
    else:
        board = list(map(list, zip(*board)))
        sort_()
        board = list(map(list, zip(*board)))

print(ans)
