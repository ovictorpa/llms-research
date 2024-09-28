def move_one_ball(arr):

    if len(arr) == 0:
        return True
    
    sorted_array = sorted(arr)
    
    min_value = min(arr)
    min_index = arr.index(min_value)
    
    rotated_array = arr[min_index:] + arr[:min_index]
    
    return rotated_array == sorted_array
