def rotate(arr):
    return [list(row) for row in list(zip(*arr))[::-1]]


def search_new_rectangle(m, n, cells, input_number):
    # cells меняются в исходном списке
    left_row = None
    header = None

    right_row = None
    # находим верхнюю границу
    for i in range(m):
        for j in range(n):
            if cells[i][j] == "#":
                cells[i][j] = input_number
                if left_row is None:
                    header = i  # строка где начинается
                    left_row = j  # столбец где начинается
            else:
                if left_row is not None:
                    right_row = j
                    break
        if left_row is not None:
            if right_row is None:
                right_row = n
            break
    if left_row is not None:
        if right_row is None:
            right_row = n

    footer = None
    whole_cells = True
    # Надо заполнить прямоугольник по найденным краям

    # с чем будем сравнивать
    # rec_slice = cells[header][left_row:right_row+1]
    if left_row is None:
        return None, None, None, None
    for i in range(header+1, m):
        for j in range(left_row, right_row):
            if cells[i][j] != '#':
                footer = i
                whole_cells = False
                break
        if whole_cells:
            for j in range(left_row, right_row):
                cells[i][j] = input_number
        else:
            break
    if whole_cells and footer is None:
        footer = m

    # footer, right_row - не включительно
    # все остальное включительно
    return left_row, right_row, header, footer


cells = []
m, n = map(int, input().split())
for i in range(m):
    row_input = input()
    cells.append([char for char in row_input])
rotated_cells = rotate(cells)
# right_row, footer - не включительно
left_1, right_1, header_1, footer_1 = search_new_rectangle(m, n, cells, '1')
left_2, right_2, header_2, footer_2 = search_new_rectangle(m, n, cells, '2')

left_3, right_3, header_3, footer_3 = search_new_rectangle(m, n, cells, '3')

rotated = False

if left_3 is not None:
    left_1, right_1, header_1, footer_1 = search_new_rectangle(
        n, m, rotated_cells, '1')
    left_2, right_2, header_2, footer_2 = search_new_rectangle(
        n, m, rotated_cells, '2')

    left_3, right_3, header_3, footer_3 = search_new_rectangle(
        n, m, rotated_cells, '3')

    if left_3 is None:
        rotated = True


# print(left_1, right_1, header_1, footer_1)
# print(left_2, right_2, header_2, footer_2)
# print(left_3, right_3, header_3, footer_3)
answer_exist = False
if rotated:
    cells = rotated_cells
    n, m = m, n


if left_3 is not None or left_1 is None:
    print('NO')
elif left_2 is not None:
    print('YES')
    answer_exist = True
    for i in range(m):
        for j in range(n):
            if cells[i][j] == '1':
                cells[i][j] = 'a'
            elif cells[i][j] == '2':
                cells[i][j] = 'b'
            else:
                pass
else:  # когда нашли только один прямоугольник
    rows_diff = footer_1 - header_1 - 1
    cols_diff = right_1 - left_1 - 1
    if rows_diff > 0 and cols_diff > 0:
        print('YES')
        answer_exist = True
        b_count = right_1 - left_1

        for i in range(m):
            for j in range(n):
                if cells[i][j] == '1':
                    if b_count > 0:
                        cells[i][j] = 'b'
                        b_count -= 1
                    else:
                        cells[i][j] = 'a'
                else:
                    pass
    else:
        if rows_diff <= 0 and cols_diff <= 0:
            print('NO')
        else:
            print('YES')
            answer_exist = True
            cells[header_1][left_1] = 'b'
            for i in range(m):
                for j in range(n):
                    if cells[i][j] == '1':
                        cells[i][j] = 'a'
                    else:
                        cells[i][j] = cells[i][j]

if answer_exist:
    if rotated:
        cells = rotate(rotate(rotate(cells)))
        m, n = n, m
    for i in range(m):
        for j in range(n):
            print(cells[i][j], end='')
        print()
