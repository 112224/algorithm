import sys
input = sys.stdin.readline
import math


def init(tree, se, ed, node):
    if se == ed:
        tree[node] = 1
    else:
        m = (se+ed)//2
        init(tree, se, m, 2*node)
        init(tree, m+1, ed, 2*node + 1)
        tree[node] = tree[2*node] + tree[2*node+1]


# tree[node] 가 나타내는 것 [st, ed] 까지의 범위의 합
def update(tree, st, ed, node, idx):
    # 현재 segment tree 가 idx를 포함하는 범위가 아니라면
    if idx < st or idx > ed:
        return
    # 포함한다면,
    tree[node] -= 1

    # st == ed 인 상황이면 leaf 노드에 도착
    if st != ed:
        m = (st+ed)//2
        # 다음 포함 범위에 따라서 업데이트 부분 찾아가기
        if idx <= m:
            update(tree, st, m, 2*node, idx)
        else:
            update(tree, m+1, ed, 2*node +1, idx)


def query(tree, st, ed, node, order):
    if st == ed:
        return st
    m = (st+ed)//2
    # 왼쪽 범위에 order 가 포함된다면 ([st, ed]의 구간합이 order 이상이라면)
    if order <= tree[2*node]:
        return query(tree, st, m, 2*node, order)
    return query(tree, m+1, ed, 2*node+1, order - tree[2*node])


n, k = map(int, input().split())
h = math.ceil(math.log2(n))
tree = [0] * (1 << (h+1))
init(tree, 1, n, 1)

ret = []
idx = 1
for i in range(n):
    num = n - i
    idx += k-1

    if idx % num == 0:
        idx = num
    elif idx > num:
        idx %= num

    val = query(tree, 1, n, 1, idx)
    update(tree, 1, n, 1, val)
    ret.append(str(val))
print('<' + ', '.join(ret) + '>')

