input = __import__('sys').stdin.readline

tc = int(input())
change = [
    [36, 37, 38, 18, 19, 20, 45, 46, 47, 27, 28, 29],
    [42, 43, 44, 24, 25, 26, 51, 52, 53, 33, 34, 35],
    [6, 7, 8, 44, 41, 38, 11, 10, 9, 45, 48, 51],
    [2, 1, 0, 53, 50, 47, 15, 16, 17, 36, 39, 42],
    [0, 3, 6, 35, 32, 29, 9, 12, 15, 18, 21, 24],
    [8, 5, 2, 26, 23, 20, 17, 14, 11, 27, 30, 33]
]
col = list('wyrogb')
caid = list('UDFBLR')
idxs = dict()
for i, ele in enumerate(caid):
    idxs[ele] = i


def rotate(idx):
    ret = change[idx]
    tmp = [ans[ret[i]] for i in range(12)]
    for i in range(12):
        ans[ret[i]] = tmp[(i + 3) % 12]
    ret = cube[idx]
    temp = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            temp[j][2 - i] = ans[ret[i][j]]
    for i in range(3):
        for j in range(3):
            ans[ret[i][j]] = temp[i][j]


for _ in range(tc):
    cube = [[[i * 9 + 3 * j + k for k in range(3)] for j in range(3)] for i in range(6)]

    ans = [col[i // 9] for i in range(54)]
    n = int(input())
    ary = input().split()
    for cmd in ary:
        idx, clock = idxs[cmd[0]], cmd[1]
        rotate(idx)
        if clock == '-':
            rotate(idx)
            rotate(idx)
    print(cube)
    for ele in cube[0]:
        ele = [ans[x] for x in ele]
        print(''.join(ele))
