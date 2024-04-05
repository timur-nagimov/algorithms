l, x1, v1, x2, v2 = list(map(int, input().split()))


def main():
    # если совпали координаты
    if x1 == x2 or l - x2 == x1 or l - x1 == x2:
        return 0
    # если коорд. не совпали, но скорость = 0
    if v1 == 0 and v2 == 0:
        return None
    # скорость одного бегуна = 0
    if v1 == 0 or v2 == 0:
        waiting_x = x1 if v1 == 0 else x2
        # waiting_v = v1 if v1 == 0 else v2
        running_x = x1 if v1 != 0 else x2
        running_v = v1 if v1 != 0 else v2

        t1 = (waiting_x-running_x)/running_v
        t2 = (l-x1-x2)/running_v

        t1 = float('inf') if t1 < 0 else t1
        t2 = float('inf') if t2 < 0 else t2
        return min([t1, t2])
    # на будущее запомним наибольший x
    big_x = x1 if x1 > x2 else x2
    big_x_v = v1 if x1 > x2 else v2
    sml_x = x1 if x1 <= x2 else x2
    sml_x_v = v1 if x1 <= x2 else v2

    # если бегут в одном направлении
    if (big_x_v > 0 and sml_x_v > 0) or (big_x_v < 0 and sml_x_v < 0):
        t1 = float('inf')
        t3 = float('inf')  # против часовой
        if big_x_v != sml_x_v:
            t1 = (x1 - x2)/(v2-v1)
        t2 = (2*l - x1 - x2) / (v2+v1)  # только для движений по часовой
        if v1 < 0:
            t2 = (x1+x2)/abs(v1+v2)
        else:
            t3 = (l-x1-x2)/(abs(v1)+abs(v2))
        t1 = float('inf') if t1 < 0 else t1
        t2 = float('inf') if t2 < 0 else t2
        t3 = float('inf') if t3 < 0 else t3

        return min([t1, t2, t3])

    # тут остались только случаи когда движутся в разных направлениях
    t1 = float('inf')
    if v2-v1 != 0:
        t1 = (x1-x2)/(v2-v1)
    # и
    if big_x_v < 0:
        t2 = (l+big_x-sml_x)/(abs(v2)+abs(v1))
    else:
        t2 = (l+sml_x-big_x)/(abs(v2)+abs(v1))
    t3 = float('inf')  # (2*l-x1-x2)/(abs(v1)+abs(v2))
    t1 = float('inf') if t1 < 0 else t1
    t2 = float('inf') if t2 < 0 else t2
    # t3 = float('inf') if t3 < 0 else t3
    return min([t1, t2, t3])


result = main()

if result is not None:
    print('YES')
    print(f'{result:.10f}')
else:
    print('NO')
