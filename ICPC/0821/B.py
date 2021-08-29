dic_week = {
    "Sun": [0],
    "Mon": [1],
    "Tue": [2],
    "Wed": [3],
    "Thu": [4],
    "Fri": [5],
    "Sat": [6],
    "All": [0, 1, 2, 3, 4, 5, 6]
}

dic_day = {
    "Day": range(60*6, 60*18),
    "Night": range(60*18, 60*30),
    "All": range(0, 60*24)
}

one_week = 7 * 24 * 60

def calc_time_in_week(weekday, time):
    time_in_week = [0] * one_week
    for week in dic_week[weekday]:
        for time_in_day in dic_day[time]:
            at = ((24*60*week) + time_in_day) % one_week
            time_in_week[at] = 1
    return time_in_week

def calc_dup(s, t, m, start, time_in_week):
    dup = 0
    for num_game in range(m):
        start_i = (start + (t * num_game)) % one_week
        end_i = (start + (t * num_game) + s + 1) % one_week
        if time_in_week[start_i] and time_in_week[end_i]:
            dup += 1
    return dup

def func(s, n, t, weekday, time, p, m):
    time_in_week = calc_time_in_week(weekday, time)
    dup = 0
    for start in range(one_week):
        dup = max(dup, calc_dup(s, t, m, start, time_in_week))
    return 1 - ((1 - (1 / p)) ** (n * dup))

ans = []
while True:
    s, n, t, weekday, time, p, m = input().split()
    if weekday == "None":
        for e in ans:
            print("{:.10f}".format(e))
        exit()
    else:
        result = func(int(s), int(n), int(t), weekday, time, int(p), int(m))
        ans.append(result)