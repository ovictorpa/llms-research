def total_match(lst1, lst2):

    l1 = sum(len(st) for st in lst1)
    l2 = sum(len(st) for st in lst2)
    
    if l1 <= l2:
        return lst1
    else:
        return lst2
