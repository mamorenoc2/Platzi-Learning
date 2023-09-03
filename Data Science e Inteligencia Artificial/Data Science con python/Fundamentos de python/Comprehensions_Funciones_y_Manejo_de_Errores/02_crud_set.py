set_countries = {'col', 'mex', 'bol'}
size = len(set_countries)
print('col' in set_countries)

# add(): Añade un elemento al conjunto.
print('add () function')
set_countries.add('pe')
print(set_countries)
print('\n')

# update(): Añade cualquier tipo de objeto iterable como: listas, tuplas
print('update () function')
set_countries.update({'ar', 'ecua', 'pe'})
print(set_countries)
print('\n')

# remove(): Elimina un elemento especifico y si este no existe lanza el error “keyError”
print('remove () function')
set_countries.remove('col')
print(set_countries)
print('\n')

#pop(): Nos devuelve un elemento aleatorio y lo elimina y si el conjunto está vacío lanza el error “key error”.
print('pop () function')
print(set_countries.pop())
print(set_countries)
print('\n')

#discard(): Elimina un elemento y si ya existe no lanza ningún error
print('discard () function')
set_countries.discard('arg')
print(set_countries)

set_countries.add('arg')
print('\n')


#eliminar todos los elementos
print('clear () function ')
set_countries.clear()
print(set_countries)
print('\n')
