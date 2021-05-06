import sys
input = sys.stdin.readline

n = int(input())
dice = [list(map(int, input().split())) for _ in range(n)]
idx = [5,3,4,1,2,0]

def find(i):
    ret = 0
    if i == 6:
        return 0
    if i == 0 or i == 5:
        ret += max(dice[0][1:5])
    elif i == 1 or i == 3:
        ret += max(dice[0][0], dice[0][2], dice[0][4], dice[0][5])
    elif i == 2 or i == 4:
        ret += max(dice[0][0], dice[0][1], dice[0][3], dice[0][5])
    prev = dice[0][idx[i]]
    for j in range(n-1):
        j_idx = dice[j + 1].index(prev)
        if j_idx == 0 or j_idx == 5:
            ret += max(dice[j+1][1:5])
        elif j_idx == 1 or j_idx == 3:
            ret += max(dice[j+1][0], dice[j+1][2], dice[j+1][4], dice[j+1][5])
        elif j_idx == 2 or j_idx == 4:
            ret += max(dice[j+1][0], dice[j+1][1], dice[j+1][3], dice[j+1][5])
        prev = dice[j+1][idx[j_idx]]

    ret = max(ret, find(i+1))
    return ret

print(find(0))