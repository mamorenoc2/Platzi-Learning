def increment(x):
  return x+1
  
increment_en_lambda = lambda x: x + 1

def high_order_funtion(x, func):
  return x + func(x)

high_oder_funtion_en_lambda = lambda x, funtionc: x + funtionc(x)

result = high_order_funtion(2, increment)
# (2 + (2 + 1)) -> 5

result_2 = high_oder_funtion_en_lambda(3, increment)
# (3 + (3 + 1 )) -> 7

print(result)
print(result_2)