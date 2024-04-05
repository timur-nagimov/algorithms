heights = [2, 7, 6, 9, 7, 5, 7, 3, 5]


left = []
right = []

# left edge
left.append(-1)
stack = [(0, heights[0]), ]
for i in range(len(heights)):
    while len(stack) != 0 and heights[i] < stack[-1][1]:
        stack.pop()
    left.append()

# ..
