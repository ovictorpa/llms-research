def modp(n: int, p: int):

    ret = 1
    for _ in range(n):
        ret = (2 * ret) % p
    return ret
