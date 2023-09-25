import utils
from paquete.modulo_1 import modulo_1_fun
from paquetes_ejemplo.modulo_ejemplo_1 import funcion_3, funcion_4
from paquetes_ejemplo.modulo_ejemplo_2 import funcion_1, funcion_2



data = [
        {
            'Country': 'Colombia',
            'Population': 500
        },
        {
            'Country': 'Bolivia',
            'Population': 300
        }
    ]

def country_pop():
    keys, values = utils.get_poputation()
    print(keys, values)
    country = input('Put a Country -> ').capitalize()
    results = utils.population_by_country(data, country)
    return results

def run():
    print(modulo_1_fun())
    print(funcion_3())
    print(funcion_4())
    print(funcion_1())
    print(funcion_2())

if __name__ == '__main__':
    run()