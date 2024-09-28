from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_number = min(numbers)
    max_number = max(numbers)
    
    if min_number == max_number:
        return [0.0] * len(numbers)
    
    return [(x - min_number) / (max_number - min_number) for x in numbers]
