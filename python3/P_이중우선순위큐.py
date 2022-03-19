import heapq

def solution(operations):
    mih, mah = [], []
    icnt, dcnt = 0, 0
    for ele in operations:
        cmd, val = ele.split()
        val = int(val)

        if cmd == 'I':
            icnt += 1
            heapq.heappush(mih, val)
            heapq.heappush(mah, -val)
        else:
            dcnt += 1
            if val == 1:
                if mah:
                    heapq.heappop(mah)
            else:
                if mih:
                    heapq.heappop(mih)
    if dcnt >= icnt:
        return [0, 0]
    return [-mah[0], mih[0]]

print(solution(["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]))