import random
countries = ['col', 'mex', 'bol', 'pe']

#Diccionarios con condicionales#
population_dict = {country: random.randint(1,100) for country in countries}

population_less_30 = {country: population for (country, population) in population_dict.items() if population < 30}

print(population_dict)
print(population_less_30)

#Diccionario que pone en mayúscula todas las vocales de una frase
texto = 'Hola!, Soy manuela'
vocales_mayusculas = { c: c.upper() for c in texto if c in 'aeiou'}
cantidad_vocales = { c: texto.count(c) for c in texto if c in 'aeiou'}
print(cantidad_vocales)

