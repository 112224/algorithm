from collections import deque
input = __import__('sys').stdin.readline

di = [(0, 1), (1, 0), (0, -1), (-1, 0)]
tc = int(input())

def bfs(has_key, need_key, visit, board, n, m, q):
    ret = 0
    while q:
        x, y = q.popleft()
        for dx, dy in di:
            nx, ny = x + dx, y + dy
            if 0<=nx<n and 0<=ny<m and not visit[nx][ny]:
                val = board[nx][ny]
                if val == '*': continue
                if 'A' <= val <= 'Z':
                    if not has_key[ord(val) - ord('A')]:
                        need_key[ord(val) - ord('A')].append((nx, ny))
                        continue
                elif 'a'<=val<='z':
                    # key 획득
                    key = ord(val) - ord('a')
                    has_key[key] = 1
                    while need_key[key]:
                        q.append((need_key[key].pop()))
                elif val == '$':
                    ret += 1
                visit[nx][ny] = True
                q.append((nx, ny))
    return ret



for _ in range(tc):
    n, m = map(int, input().split())
    visit = [[False] * (m+2) for _ in range(n+2)]
    board = [['.']*(m+2)] +  [['.']+list(input().rstrip()) + ['.'] for _ in range(n)] + [['.']*(m+2)]
    has_key = [0] * 26
    need_key = [[] for _ in range(26)]
    ini_key = input().rstrip()
    if ini_key != '0':
        for ch in ini_key:
            val = ord(ch) - ord('a')
            has_key[val] += 1
    q = deque()
    q.append((0, 0))
    ans = bfs(has_key, need_key, visit, board, n + 2, m + 2, q)
    print(ans)