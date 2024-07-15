def parse_input(input):
    if input.startswith('//'):
        delimiter = input[2]
        return input[4:], delimiter
    return input, ','
 
def split_and_convert(input, delimiter):
    return [int(num) for num in input.replace('\n', delimiter).split(delimiter)]
 
def filter_numbers(numbers):
    return [num for num in numbers if num <= 1000]
 
def add(input):
    if not input:
        return 0
    parsed_input, delimiter = parse_input(input)
    numbers = split_and_convert(parsed_input, delimiter)
    filter_numbers = filter_numbers(numbers)
    return sum(filtered_numbers)
