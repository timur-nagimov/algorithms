x = int(input())  # кол-во наших солдат
y = int(input())  # кол-во хп врага
p = int(input())  # сколько спавнится солдат

# x1, y1, p1 = x, y, p

enemy_soldiers = 0  # сколько солдат у врага
step = 0
all_steps = []


def only_enemy_destroyer(x_curr, x, enemy_soldiers):
    step = 0
    if enemy_soldiers == 0:
        # завершения хода (кр.случ)
        return 1
    while True:
        '''print('STEP внутри dest:', step)'''
        if x_curr is None:
            x_curr = x
        if x <= 0:
            '''print('помер здесь')'''
            return float('inf')
        if enemy_soldiers <= 0:
            '''print('вернул значение')'''
            return step
        enemy_soldiers -= x_curr
        x -= enemy_soldiers

        x_curr = None
        step += 1


def solution_finder(x, y, p):
    all_steps = []
    step = 0
    enemy_soldiers = 0

    # иначе всю атаку в enemy
    while True:
        if step == 2 and x == enemy_soldiers:
            all_steps.append(float('inf'))
            return all_steps

        if x <= 0:
            all_steps.append(float('inf'))
            return all_steps

        # если победили
        if y <= 0 and enemy_soldiers <= 0:
            all_steps.append(step)
            return all_steps

        # если может снести трон
        if y - x <= 0:
            '''print('сделан заход на step:', step)'''
            # x_curr, x, enemy_soldiers
            all_steps.append(
                step + only_enemy_destroyer(x-y, x, enemy_soldiers)
            )

        current_attack = x
        # бьем солдат врага
        if current_attack >= enemy_soldiers:
            current_attack -= enemy_soldiers
            enemy_soldiers = 0
        else:
            enemy_soldiers -= current_attack
            current_attack = 0

        # если осталась атака - идем бить трон
        y -= current_attack

        # теперь солдаты врага бьют нас :(
        x -= enemy_soldiers

        # и спавним новых солдат врага если трон жив
        if y > 0:
            enemy_soldiers += p

        step += 1


'''        print('НА КОНЕЦ STEP №', step)
        print(x, y, p)
        print('---')
'''

# print(solution_finder(10,  11, 15))
# print(solution_finder(1, 2, 1))
# print(solution_finder(1, 1, 1))
# print(solution_finder(250, 500, 218))
# print(solution_finder(499, 500, 499))
sol_list = solution_finder(x, y, p)

min_sol = min(sol_list)
if min_sol == float('inf'):
    print(-1)
else:
    print(min_sol)
