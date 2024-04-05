f_w, f_o = list(map(int, input().split(':')))
s_w, s_o = list(map(int, input().split(':')))
first_game_is_home = 2 - int(input())

all_w = f_w + s_w
all_o = f_o + s_o
our_home = our_visit = -1
their_home = their_visit = -1


if first_game_is_home:
    our_home = f_w
    their_visit = f_o

    our_visit = s_w
    their_home = s_o
else:
    our_home = s_w
    their_visit = s_o

    our_visit = f_w
    their_home = f_o


if all_w == all_o:
    # если счет равен, но у них больше голов в гостях
    if our_visit <= their_visit:
        print('1')
    # если счет равен, но у нас голов в гостях больше
    else:
        print('0')
# если у нас больше голов:
elif all_w > all_o:
    print('0')
# если у нас меньше голов
else:
    ans = all_o - all_w
    if first_game_is_home:  # ща в гостях
        # our_visit += tmp
        if our_visit + ans <= their_visit:
            ans += 1
        print(ans)
    else:  # ща дома
        # our_home += tmp
        if our_visit <= their_visit:
            ans += 1
        print(ans)
