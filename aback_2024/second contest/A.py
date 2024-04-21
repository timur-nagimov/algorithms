def check_victory_conditions(x_pos, y_pos, game_board):

    # гор, верт, диаг, обр.диаг
    directions = [
        (0, 1),
        (1, 0),
        (1, 1),
        (-1, 1)
    ]
    line_results = []

    for _ in directions:
        line_results.append([])

    for offset in range(-4, 5):
        for index, (delta_x, delta_y) in enumerate(directions):
            next_x, next_y = x_pos + delta_x * offset, y_pos + delta_y * offset
            if (
                (next_x, next_y) in game_board and game_board[(
                    next_x, next_y)] == game_board[(x_pos, y_pos)]
            ):
                line_results[index].append(1)
            else:
                line_results[index].append(0)

    for line in line_results:
        consecutive_ones = 0
        for number in line:
            if number == 1:
                consecutive_ones += 1
                if consecutive_ones >= 5:
                    return True
            else:
                consecutive_ones = 0
    return False


def main():
    num_moves = int(input())
    moves_list = []
    board_positions = {}
    game_result = "Draw"

    for _ in range(num_moves):
        x_coordinate, y_coordinate = map(int, input().split())
        moves_list.append((x_coordinate, y_coordinate))

    for move_index, (x, y) in enumerate(moves_list):
        board_positions[(x, y)] = move_index % 2

        if check_victory_conditions(x, y, board_positions):
            if move_index == num_moves - 1:
                game_result = "First" if move_index % 2 == 0 else "Second"
            else:
                game_result = "Inattention"
                break

    print(game_result)


if __name__ == "__main__":
    main()
