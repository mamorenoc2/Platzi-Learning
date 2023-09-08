import functools

numbers = [1, 2, 3, 4]

def acumulador(counter, item):
    print(counter)
    print(item)
    return counter + item

result = functools.reduce(lambda counter, item: counter + item, numbers)

print(result)