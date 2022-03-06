def solution(lottos, win_nums):
    win_nums = set(win_nums)
    cnt, z_cnt = 0, 0
    for ele in lottos:
        if ele == 0:
            z_cnt += 1
        elif ele in win_nums:
            cnt += 1

    hi, lo = 7 - (cnt + z_cnt), 7 - cnt
    if hi > 6: hi = 6
    if lo > 6: lo = 6

    return [hi, lo]