input = __import__('sys').stdin.readline

visit = [[False] * 110 for _ in range(110)]

# x는 열 y 는 행 visit[y][x]
def make_curve(ary):
    cx, cy = ary[-1]
    ret = []
    for x, y in ary[-2::-1]:
        x, y = x - cx, y - cy
        ret.append((-y + cx, x + cy))
    return ret

def rotate(x, y, cx, cy, angle):
    if angle == 1:
        x, y = y, -x
    elif angle == 2:
        x, y = -x, -y
    elif angle == 3:
        x, y = -y, x
    visit[x+cx][y+cy] = True

curve = [[(0,0), (1, 0)]]
for i in range(1, 11):
    curve.append(curve[i-1] + make_curve(curve[i-1]))

n = int(input())
for _ in range(n):
    cx,cy,d,g = map(int,input().split())
    for x, y in curve[g]:
        rotate(x, y, cx, cy, d)
ans = 0

for i in range(100):
    for j in range(100):
        if visit[i][j] == visit[i][j+1] == visit[i+1][j] == visit[i+1][j+1] == True:
            ans += 1
print(ans)