def main():
    nodes_count, existing_lines_count = map(int, input().split())
    min_time_matrix = [
        [float('inf')] * nodes_count for _ in range(nodes_count)]
    for i in range(nodes_count):
        min_time_matrix[i][i] = 0

    for _ in range(existing_lines_count):
        node1, node2, travel_time = map(int, input().split())
        node1 -= 1
        node2 -= 1
        min_time_matrix[node1][node2] = travel_time
        min_time_matrix[node2][node1] = travel_time

    proposals_count = int(input())
    proposals = []
    for _ in range(proposals_count):
        node1, node2, time, cost = map(int, input().split())
        proposals.append((node1-1, node2-1, time, cost))

    requirements_count = int(input())
    requirements = []
    for _ in range(requirements_count):
        node1, node2, max_time = map(int, input().split())
        requirements.append((node1-1, node2-1, max_time))

    min_cost, max_cost = 0, 10**10 + 1
    feasible_cost = -1
    while min_cost <= max_cost:
        current_cost = (min_cost + max_cost) / 2

        floyd_matrix = [row[:] for row in min_time_matrix]
        for u, v, time, cost in proposals:
            if cost <= current_cost:
                floyd_matrix[u][v] = min(floyd_matrix[u][v], time)
                floyd_matrix[v][u] = min(floyd_matrix[v][u], time)
        for t in range(nodes_count):
            for i in range(nodes_count):
                for j in range(nodes_count):
                    if floyd_matrix[i][t] + floyd_matrix[t][j] < floyd_matrix[i][j]:
                        floyd_matrix[i][j] = floyd_matrix[i][t] + \
                            floyd_matrix[t][j]
        feasible = True
        for a, b, time in requirements:
            if floyd_matrix[a][b] > time:
                feasible = False
                break

        if feasible:
            max_cost = current_cost - 1
            feasible_cost = current_cost
        else:
            min_cost = current_cost + 1

    if feasible_cost == -1:
        print(feasible_cost)
    else:
        valid_ids = [
            i+1 for i, (_, _, _, cost) in enumerate(proposals) if cost <= feasible_cost]
        print(len(valid_ids))
        print(" ".join(map(str, valid_ids)))


if __name__ == "__main__":
    main()
