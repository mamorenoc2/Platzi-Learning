#Importa funciones del sistemaa operativo
import sys
#print(sys.path)

#Importa expresiones regulares 
import re
text = 'Mi numero de telefono es 123 456 789, el código'
result = re.findall('[0-9]+', text)
#print(result)


import time
timestamp = time.time()
#print(timestamp)
local = time.localtime()
result_local_time = time.asctime(local)
#print(result_local_time)


import collections

numbers = [1,1,2,1,2,1,2,4,5,6,3,3,3,21]
counter = collections.Counter(numbers)
print(counter)