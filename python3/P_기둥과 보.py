def solution(n, build_frame):
    answer = []
    board = [[False] * (n+1) for _ in range(n+1)]

    def pilar(x, y):
        if y == 0 or board[x][y]:
            return True
        return False

    def pannel(x, y):
        f1 = x + 1 < n and board[x + 1][y]
        if board[x][y] or f1:
            return True
        return False

    for x, y, a, b in build_frame:
        if a == 0:
            if b == 1 and pilar(x, y):
                board[x][y] = True
                if y + 1 < n: board[x][y + 1] = True
                answer.append([x, y, a])
        else:
            if b == 1 and pannel(x, y):
                board[x][y] = True
                if x + 1 < n: board[x + 1][y] = True
                answer.append([x, y, a])

    return answer

n = 5
frames = [[[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]],
          [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]]

for ele in frames:
    print(solution(n, ele))

