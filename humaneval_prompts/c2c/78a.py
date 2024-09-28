def hex_key(num):

    primes = ('2', '3', '5', '7', 'B', 'D')
    total = 0
    for digit in num:
        if digit in primes:
            total += 1
    return total
