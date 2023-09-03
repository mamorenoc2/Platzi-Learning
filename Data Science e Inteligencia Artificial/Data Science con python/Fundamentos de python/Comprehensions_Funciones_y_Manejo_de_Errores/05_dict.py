import random
#diccionarios de numeros pares
dict = {}
for i in range(1,10):
  dict[i] = i*2

#list comprehesions in dictionaries
dict_comprehesion = {i: i * 2 for i in range(1, 10) }
print(dict)
#print(dict_comprehesion)

countries = ['col', 'mex', 'bol', 'pe']
population = {}

for country in countries:
  population[country] = random.randint(1,100)

#print(population)

population_v1 = {country: random.randint(1,100) for country in countries}
#print(population_v1)

names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]

new_dict = {name:age for (name, age) in zip(names, ages)}
#print(new_dict)






fruits = ['mango', 'espinaca','coco']
liquid = ['jugo de ','batido de ','leche de ']

batido = {liquid:fruits for (liquid, fruits) in zip(liquid,fruits)}
print(batido)