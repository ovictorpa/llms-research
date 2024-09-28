def closest_integer(value):

    from math import floor, ceil

    num = float(value)
    
    if num % 1 == 0.5 or num % 1 == -0.5:
        if num > 0:
            return ceil(num)
        else:
            return floor(num)
    
    return round(num)
