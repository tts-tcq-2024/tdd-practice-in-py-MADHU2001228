def add_numbers_less_than_1000(arr):

    return sum(num for num in arr if num < 1000)

def is_digit(ch):

    return ch.isdigit()

def string_to_numbers(s):

    num_arr = []
    num = 0
    for ch in s:
        if is_digit(ch):
            num = num * 10 + int(ch)
        else:
            num_arr.append(num)
            num = 0
    num_arr.append(num)  
    return num_arr

def sum_string(s):
   
    num_arr = string_to_numbers(s)
    return add_numbers_less_than_1000(num_arr)

def contains_negative_numbers(s):

    for i, ch in enumerate(s):
        if ch == '-' and i + 1 < len(s) and is_digit(s[i + 1]):
            return True
    return False

def is_valid_string(s):

    return not contains_negative_numbers(s) or s == ""

def add(s):

    if is_valid_string(s):
        total = sum_string(s)
        return total if total > 0 else 0
    return -1
