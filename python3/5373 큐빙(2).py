input = __import__('sys').stdin.readline
#         27 28 29
#         30 31 32
#         33 34 35
#         *****
# 36 37 38*0 1 2  *45 46 47
# 39 40 41*3 4 5  *48 49 50
# 42 43 44*6 7 8  *51 52 53
#         *****
#         18 19 20
#         21 22 23
#         24 25 26
#         *****
#         9 10 11
#         12 13 14
#         15 16 17
change_list = [
    [44, 41, 38, 33, 34, 35, 45, 48, 51, 20, 19, 18],
    [24, 25, 26, 53, 50, 47, 29, 28, 27, 36, 39, 42],
    [6, 7, 8, 51, 52, 53, 11, 10, 9, 42, 43, 44],
    [47, 46, 45, 2, 1, 0, 38, 37, 36, 15, 16, 17],
    [0, 3, 6, 18, 21, 24, 9, 12, 15, 27, 30, 33],
    [17, 14, 11, 26, 23, 20, 8, 5, 2, 35, 32, 29]
]
color = list('wyrogb')
direction = list('UDFBLR')
facing = dict()
for i, ele in enumerate(direction):
    facing[ele] = i


def rotate(cube, ans, face):
    # 옆 면 회전
    candi = change_list[face]
    tmp = [ans[ele] for ele in candi]
    for i in range(12):
        ans[candi[i]] = tmp[(i - 3) % 12]
    candi = cube[face][:]
    tmp = [[ans[ele] for ele in candi[i]] for i in range(3)]
    for i in range(3):
        for j in range(3):
            ans[candi[i][j]] = tmp[2 - j][i]


def print_ans(ans, cube):
    printing = [[color[ans[ele] // 9] for ele in ary] for ary in cube[0]]
    for ary in printing:
        print(''.join(ary))


def solve():
    tc = int(input())

    cube = [[[k * 9 + i * 3 + j for j in range(3)] for i in range(3)] for k in range(6)]
    for _ in range(tc):
        ans = [i for i in range(54)]
        k = int(input())
        cmd = input().split()
        for ele in cmd:
            face, clock = facing[ele[0]], ele[1]
            rotate(cube, ans, face)
            if clock == '-':
                rotate(cube, ans, face)
                rotate(cube, ans, face)
        print_ans(ans, cube)


solve()
