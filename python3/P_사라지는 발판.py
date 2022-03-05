di = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def finished(board, n, m, loc):
    x, y = loc
    for dx, dy in di:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
            return False
    return True


def move(board, n, m, aloc, bloc):
    x, y = aloc
    if finished(board, n, m, aloc): return False, 0
    if aloc == bloc: return True, 1

    flag = False
    min_turn, max_turn = 10 ** 9, 0
    for dx, dy in di:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
            board[x][y] = 0
            ret, turn = move(board, n, m, bloc, [nx, ny])
            board[x][y] = 1

            if not ret:
                flag = True
                min_turn = min(min_turn, turn)
            elif not flag:
                max_turn = max(max_turn, turn)

    ret = min_turn if flag else max_turn
    return flag, ret + 1


def solution(board, aloc, bloc):
    whos, answer = move(board, len(board), len(board[0]), aloc, bloc)
    return answer


print(solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [1, 0], [1, 2]))
