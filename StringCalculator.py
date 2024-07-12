def add(num: str) -> int:
    if num.startswith('//'):
        delimiter, num = custom_delimiter(num)
    else:
        delimiter = ','
    num_Input = split(num, delimiter)
    return sum_num(num_Input) 
 
def custom_delimiter(num: str) -> tuple:
    delimiter, num = num[2:].split('\n', 1)
    return delimiter, num
  
def split(num: str, delimiter: str) -> list:
    return num.replace('\n', delimiter).split(delimiter) 
 
def sum_num(num_Input: list) -> int:
    def valid(num):
        return num.isdigit() and int(num) <= 1000
    return sum(int(num) for num in num_Input if valid(num))
