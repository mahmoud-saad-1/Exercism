def primes(limit):
    test1 = set()

    for i in range(2, limit + 1):
        test1.add(i)

    for i in range(2, limit):
        if i in test1:
            for n in range(i*2, limit + 1,i):
                test1.discard(n)
    return sorted(list(test1))
