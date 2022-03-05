def time2int(time):
    time = time.split(':')
    return int(time[0]) * 60 + int(time[1])


def calculator(fees, use_time):
    x1, y1, x2, y2 = fees
    ret = y1
    use_time -= x1
    if use_time > 0:
        ahr, rem = divmod(use_time, x2)
        add_fee = y2 * ahr if rem == 0 else y2 * (ahr + 1)
        ret += add_fee
    return ret


def get_used_time(records):
    last = time2int('23:59')
    time_table = dict()
    ret = dict()
    for ele in records:
        time, car_num, tp = ele.split()
        time = time2int(time)
        car_num = int(car_num)
        if tp == 'IN':
            time_table[car_num] = time
        else:
            used_time = time - time_table[car_num]
            time_table[car_num] = -1
            if car_num in ret:
                ret[car_num] += used_time
            else:
                ret[car_num] = used_time
    for key in time_table:
        if time_table[key] == -1: continue
        used_time = last - time_table[key]
        if key in ret:
            ret[key] += used_time
        else:
            ret[key] = used_time
    return ret


def solution(fees, records):
    times = get_used_time(records)

    return [calculator(fees, times[key]) for key in sorted(times.keys())]

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))