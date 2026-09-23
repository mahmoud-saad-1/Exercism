def sum_of_multiples(limit, multiples):
    score = set()

    for i in range(0, len(multiples)):
        if multiples[i] == 0:
            continue
        for n in range(multiples[i],limit,multiples[i]):
            score.add(n)

    return sum(score)
