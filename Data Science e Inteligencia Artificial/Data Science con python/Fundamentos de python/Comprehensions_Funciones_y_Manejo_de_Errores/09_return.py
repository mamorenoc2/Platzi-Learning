def find_volume(length, width, depth):
  return length * width * depth

resultado = find_volume(10, 20, 3)
print(resultado)

#Misma función pero con valores predeterminados
def find_volume_2(length=1, width=1, depth=1):
  return length * width * depth

#No hay necesidad de enviar parámetros
resultado = find_volume_2()
print(resultado)


#Misma función pero usando valores predeterminados y enviando valores por argumento
def find_volume_3(length=1, width=1, depth=1):
  return length * width * depth

#Se envía el parametro que se quiera modificar por defecto
resultado = find_volume_2(width=10)
print(resultado)