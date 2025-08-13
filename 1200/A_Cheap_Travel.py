def cheap_travel():
    cost = 0
    nmab = list(map(int, input().split()))
    n, m, a, b = nmab[0], nmab[1], nmab[2], nmab[3]
    # n = no. of rides, m = m rides per $b, $a = price for one ride
    if b < a * m:
        cost += (n // m) * b
        cost += min((n % m) * a, b)
    else:
        cost = n * a
    print(cost)

cheap_travel()
