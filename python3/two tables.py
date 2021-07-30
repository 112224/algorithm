import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    W, H = map(int,input().split())
    x1,y1,x2,y2 =map(int,input().split())
    w, h = map(int,input().split())
    f1, f2 = False, False
    if x2-x1 + w > W:
        f1 = True
    if y2-y1 + h > H:
        f2 = True
    if f1 and f2:
        print(-1)
    else:
        mx = max(x1, W-x2)
        my = max(y1, H-y2)
        if mx >= w or my >= h:
            print(0)
        else:
            if f1:
                print(h-my)
            elif f2:
                print(w-mx)
            else:
                print(min(h-my, w-mx))
