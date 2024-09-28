from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:

    closest_pair = None
    min_distance = float('inf')
    
    for i, num1 in enumerate(numbers):
        for j, num2 in enumerate(numbers):
            if i != j:
                distance = abs(num1 - num2)
                if distance < min_distance:
                    min_distance = distance
                    closest_pair = tuple(sorted([num1, num2]))
    
    return closest_pair
