input = __import__('sys').stdin.readline

n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(n):
    val, flat = board[i][0], 1
    flag = True
    for j in range(1, n):
        nval = board[i][j]
        if abs(val - nval) > 1:
            flag = False
            break
        if val == nval:
            flat += 1
        else:
            if not flag:
                break
            if val < nval:
                if flat < l:
                    flag = False
                    break
                else:
                    val, flat = nval, 1
            else:
                flag = False
                val, flat = nval, 1
        if not flag:
            if flat == l:
                flat = 0
                flag = True
    if flag:ans += 1
for j in range(n):
    val, flat = board[0][j], 1
    flag = True
    for i in range(1, n):
        nval = board[i][j]
        if abs(val - nval) > 1:
            flag = False
            break
        if val == nval:
            flat += 1
        else:
            if not flag:
                break
            if val < nval:
                if flat < l:
                    flag = False
                    break
                else:
                    val, flat = nval, 1
            else:
                flag = False
                val, flat = nval, 1
        if not flag:
            if flat == l:
                flat = 0
                flag = True
    if flag:ans += 1
print(ans)