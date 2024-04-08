def eratostenes(n):
    """
    Решето Эратосфена O(n)
    """
    lp = [0]*(n+1)
    primes = []
    for i in range(2, n+1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)

        for prime in primes:
            x = prime*i
            if x > n or prime > lp[i]:
                break
            lp[x] = prime

    return primes, lp


print(eratostenes(15))
