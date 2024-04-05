def rock_moves(board, row, col):

    # Движение влево
    for i in range(col - 1, -1, -1):
        if board[row][i] in ('*', -1):
            board[row][i] = -1
        else:
            break

    # Движение вправо
    for i in range(col + 1, 8):
        if board[row][i] in ('*', -1):
            board[row][i] = -1
        else:
            break

    # Движение вверх
    for i in range(row - 1, -1, -1):
        if board[i][col] in ('*', -1):
            board[i][col] = -1
        else:
            break

    # Движение вниз
    for i in range(row + 1, 8):
        if board[i][col] in ('*', -1):
            board[i][col] = -1
        else:
            break

    return board


def bishop_moves(board, row, col):

    # влево-вверх
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] in ('*', -1):
            board[i][j] = -1
        else:
            break
        i -= 1
        j -= 1

    # вверх-вправо
    i, j = row - 1, col + 1
    while i >= 0 and j < 8:
        if board[i][j] in ('*', -1):
            board[i][j] = -1
        else:
            break
        i -= 1
        j += 1

    # вниз-влево
    i, j = row + 1, col - 1
    while i < 8 and j >= 0:
        if board[i][j] in ('*', -1):
            board[i][j] = -1
        else:
            break
        i += 1
        j -= 1

    # вниз-вправо
    i, j = row + 1, col + 1
    while i < 8 and j < 8:
        if board[i][j] in ('*', -1):
            board[i][j] = -1
        else:
            break
        i += 1
        j += 1

    return board


board = []
for _ in range(8):
    board.append(list(input()))


for i in range(8):
    for j in range(8):
        if board[i][j] == 'B':
            board = bishop_moves(board, i, j)
        elif board[i][j] == 'R':
            board = rock_moves(board, i, j)


# подсчет суммы
summa = 0
for i in range(8):
    for j in range(8):
        if board[i][j] == '*':
            summa += 1

# результат
print(summa)
