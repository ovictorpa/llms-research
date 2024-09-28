from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:

    if not numbers:
        return []
    
    result = []
    for n in numbers[:-1]:
        result.append(n)
        result.append(delimiter)
    
    result.append(numbers[-1])
    return result
