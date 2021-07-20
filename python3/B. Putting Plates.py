import sys
input = sys.stdin.readline

tc = int(input())
di = [(-1,0),(0,-1),(-1,-1),(-1,1)]
for _ in range(tc):
    h, w = map(int, input().split())
    table = [[0] * w for i in range(h)]

    for i in range(h):
        for j in range(w):
            if i == 0 or i == h-1 or j == 0 or j == w-1:
                flag = False
                for dx, dy in di:
                    px, py = i+dx, j+dy
                    if 0 <= px < h and 0 <= py < w:
                        if table[px][py] == 1:
                            flag = True
                            break
                if not flag:
                    table[i][j] = 1

    for ele in table:
        print(''.join(map(str, ele)))
    print()
