from collections import deque


def main():
    total_elements, window_length = map(int, input().split())
    elements = list(map(int, input().split()))

    sliding_window_sum = 0
    min_queue = deque()
    usage_count = [0] * total_elements

    for index in range(total_elements):
        current_value = elements[index]

        while (min_queue and
               min_queue[0][1] <= index - window_length):
            min_queue.popleft()
        while (
                min_queue and
                min_queue[-1][0] >= current_value):
            min_queue.pop()

        min_queue.append((current_value, index))
        sliding_window_sum += min_queue[0][0]
        usage_count[min_queue[0][1]] += 1

    print(sliding_window_sum)
    print(" ".join(map(str, usage_count)))


if __name__ == "__main__":
    main()
