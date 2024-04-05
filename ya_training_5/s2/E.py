def main():
    n = int(input())

    all_stats = []
    plus_stats = []
    minus_stats = []

    for i in range(n):
        x, y = map(int, input().split())
        all_stats.append([x, y, i+1])
        if x - y >= 0:
            plus_stats.append([x, y, i+1])
        else:
            minus_stats.append([x, y, i+1])

    # plus_stats = sorted(plus_stats, key=lambda x: -(x[0]-x[1]))
    # minus_stats = sorted(minus_stats, key=lambda x: -x[0])
    # надо убирать из all_stats 1 элемент, если он неотрицательный
    # сумма всех пол.ягод без этой ягоды
    # если максимальна сумма - этот элемент экватор
    max_sum = 0
    ekvator_idx = 0

    summ_plus = 0
    for plus in plus_stats:
        summ_plus += plus[0]
        summ_plus -= plus[1]

    for berry_idx in range(len(all_stats)):
        berry = all_stats[berry_idx]
        removed_berry = False
        # summ_plus = 0

        # избавиться от этой бяки
        """for plus in plus_stats:
            summ_plus += plus[0]
            summ_plus -= plus[1]"""

        # если ягода в списке положит.ягод
        # удалим её из суммы
        if berry[0] - berry[1] >= 0:
            summ_plus -= berry[0]
            summ_plus += berry[1]
            removed_berry = True

        # если
        # смотрим, если сумма макс. - обновляем
        if max_sum < summ_plus + berry[0]:
            max_sum = summ_plus + berry[0]
            ekvator_idx = berry_idx

        # если удаляли ягоду - вернем
        if removed_berry:
            summ_plus += berry[0]
            summ_plus -= berry[1]

    # теперь надо вывести:
    # положительные без экватора
    # экватор
    # отрицательные
    # ну и считать сумму

    current_high = 0
    max_ans = 0
    ans_idx = []
    # Удалим из оттуда откуда надо
    if all_stats[ekvator_idx] in plus_stats:
        plus_stats.remove(all_stats[ekvator_idx])
    elif all_stats[ekvator_idx] in minus_stats:
        minus_stats.remove(all_stats[ekvator_idx])

    # выводим положительные
    for plus in plus_stats:
        current_high += plus[0]  # плюс день
        if max_ans < current_high:
            max_ans = current_high
        current_high -= plus[1]  # минус ночь
        if max_ans < current_high:
            max_ans = current_high
        ans_idx.append(plus[2])  # добавляем индекс

    # обработаем экватор
    ekvator = all_stats[ekvator_idx]
    current_high += ekvator[0]
    if max_ans < current_high:
        max_ans = current_high
    current_high -= ekvator[1]
    if max_ans < current_high:
        max_ans = current_high
    ans_idx.append(ekvator[2])

    # обработка минусов
    for minus in minus_stats:
        current_high += minus[0]  # плюс день
        if max_ans < current_high:
            max_ans = current_high
        current_high -= minus[1]  # минус ночь
        if max_ans < current_high:
            max_ans = current_high
        ans_idx.append(minus[2])  # добавляем индекс

    print(max_ans)
    print(' '.join(map(str, ans_idx)))


if __name__ == '__main__':
    main()
