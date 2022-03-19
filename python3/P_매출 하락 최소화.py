def dp(sales, adj, memo, idx, att, prev):
    if memo[idx][att] != -1: return memo[idx][att]
    ret = 0
    flag = False
    gap = -1
    for ele in adj[idx]:
        if ele == prev: continue
        cka = dp(sales, adj, memo, ele, 1, idx)
        qnf = dp(sales, adj, memo, ele, 0, idx)
        ret += min(cka, qnf)

        if cka<qnf: flag = True
        else:
            if gap == -1 or gap > cka - qnf:
                gap = cka - qnf
    if att == 1: ret += sales[idx]
    elif not flag: ret += gap

    memo[idx][att] = ret
    return memo[idx][att]


def solution(sales, links):
    n = len(sales)
    adj = [[] for _ in range(n)]
    memo = [[-1, -1] for _ in range(n)]
    for a, b in links:
        adj[a - 1].append(b - 1)

    for i in range(n):
        if not adj[i]:
            memo[i][1] = sales[i]
            memo[i][0] = 0


    return min(dp(sales, adj, memo, 0, 0, -1), dp(sales, adj, memo, 0, 1, -1))


print(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17],
               [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]))
