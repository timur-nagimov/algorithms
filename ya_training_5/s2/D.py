n = int(input())

chess_board = []

for i in range(8+2):
    chess_board.append([0]*(8+2))

coords_x = []
coords_y = []

for i in range(n):
    x, y = map(int, input().split())
    coords_x.append(x)
    coords_y.append(y)

    chess_board[x][y] = 1

# массив сдвигов
shift_x = [-1, 1, 0, 0]
shift_y = [0, 0, -1, 1]

answer = 0
for i in range(len(coords_x)):
    point_x = coords_x[i]
    point_y = coords_y[i]

    for j in range(len(shift_x)):
        move_x = point_x + shift_x[j]
        move_y = point_y + shift_y[j]

        if chess_board[move_x][move_y] == 0:
            answer += 1


print(answer)
