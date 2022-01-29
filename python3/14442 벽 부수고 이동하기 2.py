#https://www.acmicpc.net/problem/14442
#벽 부수고 이동하기 2


input = __import__('sys').stdin.readline
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n,m,k = map(int, input().split())
board = [list(map(int, list(input().rstrip()))) for _ in range(n)]


# early return 을 위해 함수로 분리. 함수로 분리하는 것이 작성에 더 편한 경우 많으니 습관들일 것.
def bfs(n, m, k):
    if n == 1 and m == 1:
        return 1
    # 부순 것의 갯수를 저장
    visit = [[-1] * m for _ in range(n)]
    visit[0][0] = 0
    q = deque()
    q.append((0, 0, 1))

    while q:
        x, y, cnt = q.popleft()
        nc = cnt + 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if nx == n-1 and ny == m-1:
                    return nc
                broken_count = visit[x][y] + board[nx][ny]
                # 방문 가능한 경우 => 더 적게 부수고 방문

                if broken_count <= k and (visit[nx][ny] == -1 or broken_count < visit[nx][ny]):
                    visit[nx][ny] = broken_count
                    q.append((nx, ny, nc))
    return -1

print(bfs(n, m, k))