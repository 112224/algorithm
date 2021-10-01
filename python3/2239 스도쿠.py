input = __import__('sys').stdin.readline

board = [list(map(int, list(input().rstrip()))) for _ in range(9)]
row = [0] * 9
col = [0] * 9
block = [[0] * 3 for _ in range(3)]
for i in range(9):
    for j in range(9):
        val = board[i][j]
        if not val: continue
        row[i] |= (1<<val)
        col[j] |= (1<<val)
        block[i//3][j//3] |= (1<<val)

def recursive(idx, board, row, col, block):
    if idx == 81:
        return True
    i, j = divmod(idx, 9)
    if board[i][j]:
        return recursive(idx + 1, board, row, col, block)
    for val in range(1, 10):
        sh = (1<<val)
        if row[i] & sh == 0 and col[j] & sh == 0 and block[i//3][j//3] & sh == 0:
            row[i] |= sh
            col[j] |= sh
            block[i//3][j//3] |= sh
            board[i][j] = val
            if recursive(idx + 1, board, row, col, block):
                return True
            row[i] ^= sh
            col[j] ^= sh
            block[i // 3][j // 3] ^= sh
            board[i][j] = 0
    return False
recursive(0, board, row, col, block)
for ele in board:
    print(''.join(map(str, ele)))
