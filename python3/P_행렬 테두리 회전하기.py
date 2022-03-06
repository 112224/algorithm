def rotate(board, x1, y1, x2, y2):
    candi = []
    for j in range(y1, y2 + 1): candi.append((x1, j))
    for i in range(x1 + 1, x2 + 1): candi.append((i, y2))
    for j in range(y2 - 1, y1 - 1, -1): candi.append((x2, j))
    for i in range(x2 - 1, x1, -1): candi.append((i, y1))

    tmp = [board[x][y] for x, y in candi]
    for i, point in enumerate(candi):
        x, y = point
        board[x][y] = tmp[i - 1]

    return min(tmp)


def solution(rows, columns, queries):
    answer = []
    board = [[(i - 1) * columns + j for j in range(1, columns + 1)] for i in range(1, rows + 1)]

    for x1, y1, x2, y2 in queries:
        answer.append(rotate(board, x1-1, y1-1, x2-1, y2-1))
    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
