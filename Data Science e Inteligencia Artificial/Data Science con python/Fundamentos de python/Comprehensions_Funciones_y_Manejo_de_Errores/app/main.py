import utils
from paquete.modulo_1 import modulo_1_fun




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

if __name__ == '__main__':
    run()