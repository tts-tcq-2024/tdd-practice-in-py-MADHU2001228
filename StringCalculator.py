def add(num):
  if  num == "0" or num == "":
    return 0
  a = num.split(',')
  
  sum = sum( int(result) for result in a)
  return sum
