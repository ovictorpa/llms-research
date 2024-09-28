def largest_divisor(n: int) -> int:

    for i in reversed(range(1, n)):  
        if n % i == 0:
            return i
    return 1 
