def how_many_times(string: str, substring: str) -> int:

    times = 0
    substring_length = len(substring)
    
    for i in range(len(string) - substring_length + 1):
        if string[i:i + substring_length] == substring:
            times += 1
    
    return times
