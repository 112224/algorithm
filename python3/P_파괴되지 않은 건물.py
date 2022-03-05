def solution(board, skill):
    answer = 0
    n, m = len(board), len(board[0])
    game = [[0] * (m + 2) for _ in range(n + 2)]

    # 0,0 -> 1, 1
    # n-1, m-1 -> n, m

    for type, r1, c1, r2, c2, degree in skill:
        if type == 1: degree *= -1
        r1, c1, r2, c2 = r1 + 1, c1 + 1, r2 + 1, c2 + 1
        game[r1][c1] += degree
        game[r1][c2+1] += -degree
        game[r2+1][c1] += -degree
        game[r2+1][c2+1] += degree

    for i in range(n+2):
        for j in range(1, m+2):
            game[i][j] += game[i][j-1]

    for j in range(m+2):
        for i in range(1, n+2):
            game[i][j] += game[i-1][j]

    for i in range(n):
        for j in range(m):
            if board[i][j] + game[i+1][j+1] > 0:
                answer += 1


    return answer


print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
               [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))
