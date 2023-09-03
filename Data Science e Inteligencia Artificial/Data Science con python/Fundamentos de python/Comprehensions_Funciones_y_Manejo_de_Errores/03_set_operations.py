set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

#Para unir todos elementos
set_c = set_a.union(set_b)
print(set_c)
#Tambien con caracteres lógicos se pueden unir elementos
set_c_modificado = set_a | set_b
print(set_c_modificado)

#Para interseptar 2 conjuntos
#Es cuando se escogen los elementos en común de los conjuntos
set_d = set_a.intersection(set_b)
print(set_d)

#Tambien con caracteres lógicos se pueden interceptar los elementos
set_d_modificado = set_a & set_b
print(set_d_modificado)

#Para ver la diferencia de conjuntos
#Dejar los elementos del primer conjunto y removiendo los del segundo, incluyendo los valores en común

set_e = set_a.difference(set_b)
print(set_e)

#Tambien con caracteres lógicos se pueden saber la diferencia entre conjuntos

set_e_modificado = set_a - set_b
print(set_e_modificado)


#Para saber la diferencia simétrica entre conjuntos
# Es hacer la misma función que la unión con la diferencia de que se sacan los elementos iguales
set_f = set_a.symmetric_difference(set_b)
print(set_f)

set_f_modificado = set_a ^ set_b
print(set_f_modificado)
