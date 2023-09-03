def incrementar(x):
  return x + 1

incrementar_2 = lambda x : x + 1

resultado = incrementar(10)
resultado_2 = incrementar_2(10)

print(resultado)
print(resultado_2)

full_name = lambda name, last_name : f'El nombre completo es {name.title()} {last_name.title()}'
texto = full_name('manuela','moreno cordoba')
print(texto)
