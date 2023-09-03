def sum_with_range(min_, max_):
  suma = 0
  for x in range(min_,max_):
    suma += x
  return suma

def rest_with_range(n_min, n_max):
  rest = 0
  for x in range(n_min, n_max):
    rest -= x
  return rest

resultado = sum_with_range(1, 100)
print(resultado)