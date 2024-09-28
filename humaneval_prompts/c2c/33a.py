from typing import List

def sort_third(l: List[int]) -> List[int]:

    l = list(l)
    l[::3] = sorted(l[::3])
    return l
