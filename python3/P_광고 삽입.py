def time2int(ti):
    ti = ti.split(':')
    return 3600 * int(ti[0]) + 60 * int(ti[1]) + int(ti[2])


def int2time(val):
    h, m = divmod(val, 3600)
    m, s = divmod(m, 60)
    h = str(h) if h > 9 else '0' + str(h)
    m = str(m) if m > 9 else '0' + str(m)
    s = str(s) if s > 9 else '0' + str(s)

    return f'{h}:{m}:{s}'


def solution(play_time, adv_time, logs):
    answer = 0
    play_time, adv_time = time2int(play_time), time2int(adv_time)
    viewer = [0] * (play_time + 1)

    for time in logs:
        st, ed = time.split('-')
        st, ed = time2int(st), time2int(ed)
        viewer[st] += 1
        viewer[ed] -= 1

    for i in range(1, play_time + 1):
        viewer[i] += viewer[i - 1]
    for i in range(1, play_time + 1):
        viewer[i] += viewer[i - 1]

    ret = viewer[adv_time]
    for i in range(play_time - adv_time + 1):
        cur = viewer[i + adv_time] - viewer[i]
        if ret < cur:
            ret = cur
            answer = i + 1

    return int2time(answer)


print(solution("99:59:59", "25:00:00",
               ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
