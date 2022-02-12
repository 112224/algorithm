input = __import__('sys').stdin.readline


def is_possible(road, n, l):
    # 낮은 곳의 갯수가 l개 이상 연속, 높이 차이는 1
    height = road[0]
    width = 1
    for val in road[1:]:
        if val == height:
            width += 1
        elif val == height + 1 and width >= 0:
            if width >= l:
                height = val
                width = 1
            else:
                return False
        elif val == height - 1 and width >= 0:
            height = val
            width = -l + 1
        else:
            return False
    return True if width >= 0 else False


def solve():
    n, l = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    ret = 0
    for i in range(n):
        if is_possible(board[i][:], n, l):
            ret += 1
    board = list(map(list, zip(*board)))
    for i in range(n):
        if is_possible(board[i][:], n, l):
            ret += 1

    return ret


print(solve())
