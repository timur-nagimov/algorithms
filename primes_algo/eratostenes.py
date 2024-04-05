def eratostenes(n):
    """
    Решето Эратосфена O(n*log(log(n)))
    """
    numbers = list(range(n+1))
    numbers[0] = numbers[1] = False
    for num in range(2, n+1):
        if numbers[num]:
            for i in range(num*num, n+1, num):
                numbers[i] = False

    return numbers
