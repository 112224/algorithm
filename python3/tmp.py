from collections import defaultdict


def time2int(time):
    h, m = time.split(':')
    return int(h)*60 + int(m)

def calculator(fees, use_time):
    a, b, c, d = fees
    ret = b
    use_time -= a
    if use_time > 0:
        add_use, k = divmod(use_time, c)
        if k != 0: add_use += 1
        ret += add_use * d
    return ret


def solution(fees, records):
    used_time = defaultdict(int)
    in_and_out = dict()
    out_time = time2int('23:59')

    for record in records:
        time, car_num, parking_type = record.split()
        time = time2int(time)
        if parking_type == 'IN':
            in_and_out[car_num] = [time, out_time]
        else:
            in_and_out[car_num][1] = time
            used_time[car_num] += in_and_out[car_num][1] - in_and_out[car_num][0]

    for key in in_and_out:
        if in_and_out[key][1] == out_time:
            used_time[key] += in_and_out[key][1] - in_and_out[key][0]

    return [calculator(fees, used_time[x]) for x in sorted(used_time.keys())]

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))