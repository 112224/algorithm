input = __import__('sys').stdin.readline
di = [(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1] if i != 0 or j != 0]


def insert_tree(tree, k, v):
    if k in tree:
        tree[k] += v
    else:
        tree[k] = v


def simulation(board, nutrient, trees, n):
    ret = 0
    for i in range(n):
        for j in range(n):
            if not trees[i][j]: continue
            breed = board[i][j]
            next_tree = dict()
            dead = 0
            for key in sorted(trees[i][j].keys()):
                val = trees[i][j][key]
                can_alive = val if breed >= val * key else breed // key
                if not can_alive:
                    dead += val *(key // 2)
                    continue
                ret += can_alive
                breed -= key * can_alive
                insert_tree(next_tree, key + 1, can_alive)
                dead += (val - can_alive) * (key // 2)

            board[i][j] = breed + dead
            trees[i][j] = next_tree

    # fall
    for i in range(n):
        for j in range(n):
            if not trees[i][j]: continue
            cnt = 0
            for key in sorted(trees[i][j].keys()):
                if key % 5 != 0: continue
                val = trees[i][j][key]
                cnt += val

            if cnt == 0: continue
            for dx, dy in di:
                nx, ny = i + dx, j + dy
                if 0 <= nx < n and 0 <= ny < n:
                    ret += cnt
                    insert_tree(trees[nx][ny], 1, cnt)

    # winter
    for i in range(n):
        for j in range(n):
            board[j][i] += nutrient[j][i]
    return ret


def solve():
    n, m, k = map(int, input().split())
    board = [[5] * n for _ in range(n)]
    nutrient = [list(map(int, input().split())) for _ in range(n)]
    trees = [[dict() for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        r, c, age = map(int, input().split())
        insert_tree(trees[r - 1][c - 1], age, 1)

    ret = m
    for _ in range(k):
        ret = simulation(board, nutrient, trees, n)
        if ret == 0:
            break
    return ret


print(solve())
