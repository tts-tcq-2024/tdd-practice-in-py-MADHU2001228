def add(num):
  if  num == "0" or num == "":
    return 0
  a = num.split(',')
  
  Addition = sum( int(result) for result in a)
  return Addition
