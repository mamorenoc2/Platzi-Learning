# def my_print(text):
#   print(text)

# my_print('hola')

# def suma(a, b):
#   print(a+b)

# suma(10,11)

def message_creator(text):
   mensaje = ""
   if(text == 'computadora'):
      mensaje = "Con mi computadora puedo programar usando Python"
   elif(text == 'celular'):
      mensaje = "En mi celular puedo aprender usando la app de Platzi"
   elif(text == 'cable'):
      mensaje = "¡Hay un cable en mi bota!"
   else:
       mensaje = "Artículo no encontrado"

   # Escribe tu solución 👇
   return mensaje

text = 'computadora'
response = message_creator(text)
print(response)