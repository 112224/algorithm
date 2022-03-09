from itertools import permutations
from collections import deque

di = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dict_insert(cards, key, val):
    if key in cards:
        cards[key].append(val)
    else:
        cards[key] = [val]


def inrange(r, c):
    return 0 <= r < 4 and 0 <= c < 4


def ctrl_move(board, r, c, direction):
    dr, dc = di[direction]
    while inrange(r + dr, c + dc):
        r, c = r + dr, c + dc
        if board[r][c] != 0: break
    return r, c


def bfs(board, r1, c1, r2=-1, c2=-1):
    visit = [[-1] * 4 for _ in range(4)]
    visit[r1][c1] = 0

    q = deque([(r1, c1)])
    while q:
        cur_r, cur_c = q.popleft()

        for i in range(4):
            nr, nc = ctrl_move(board, cur_r, cur_c, i)

            if inrange(nr, nc) and visit[nr][nc] == -1:
                visit[nr][nc] = visit[cur_r][cur_c] + 1
                q.append((nr, nc))

            nr, nc = cur_r + di[i][0], cur_c + di[i][1]
            if inrange(nr, nc) and visit[nr][nc] == -1:
                visit[nr][nc] = visit[cur_r][cur_c] + 1
                q.append((nr, nc))
    if r2 != -1:
        return visit[r2][c2]
    return visit


def simulation(board, cards, r, c, keys, idx):
    if idx == -1: return 0

    key = keys[idx]
    r2, c2 = cards[key][0]
    r3, c3 = cards[key][1]

    visit = bfs(board, r, c)
    v1, v2 = visit[r2][c2], visit[r3][c3]
    v1 += bfs(board, r2, c2, r3, c3)
    v2 += bfs(board, r3, c3, r2, c2)

    board[r2][c2], board[r3][c3] = 0, 0
    v1 += simulation(board, cards, r3, c3, keys, idx - 1)
    v2 += simulation(board, cards, r2, c2, keys, idx - 1)
    board[r2][c2], board[r3][c3] = key, key

    return min(v1, v2) + 2


def solution(board, r, c):
    answer = 10 ** 9
    cards = dict()
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0: continue
            dict_insert(cards, board[i][j], (i, j))

    n = len(cards)
    for ary in permutations(cards.keys()):
        ret = simulation(board, cards, r, c, ary, n - 1)
        if ret < answer: answer = ret

    return answer


print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0))
