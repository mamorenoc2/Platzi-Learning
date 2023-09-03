items = [
  {
    'product': 'camisa',
    'price': 100, 
  },
  {
    'product': 'pantalones',
    'price': 300
  },
  {
    'product': 'zapatos',
    'price': 200
  }
]

prices = list(map(lambda item: item['price'], items))
products = list(map(lambda item: item['product'], items))
#print(prices)
#print(products)

def add_taxes(item):
  item['taxes'] = item['price'] * .19
  return item
  

new_items = list(map(add_taxes, items))
print(new_items)
