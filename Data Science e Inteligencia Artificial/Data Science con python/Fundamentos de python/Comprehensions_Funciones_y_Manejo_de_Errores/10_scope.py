price = 10 #Global

def increment():
  #Si no se define la variable price, esta tendrá un UnboudLocalError
  #variable local
  price = 20
  price += 10
  print(price)

print(price)
increment()
  