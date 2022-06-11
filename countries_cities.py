import json

from models.airport import Airport
from models.city import City
from models.country import Country


def get_airport_codes() -> dict:
    """
    Reads 'airport-codes.json' and returns the content as dict
    :return:
    """
    with open("files/airport-codes.json", mode="r") as file:
        airport_codes = json.load(file)
    return airport_codes


def get_countries_dict() -> dict:
    """
    Create an array of dictionaries where each dictionary represents a country. A country will have 'name' and
    'code' representing it.
    The files 'country_codes.txt' and 'countries.txt' are concatenated together in order to create the array.
    :return:
    """
    with open("files/country_codes.txt", mode="r") as file:
        country_codes = file.read().split("\n")
    with open("files/countries.txt", mode="r") as file:
        countries = file.read().split("\n")
    countries_dict = {code:name for code, name in zip(country_codes, countries)}
    return countries_dict


def get_iata_codes():
    """
    Creates an array of iata_codes
    :return:
    """
    iata_codes = []
    airport_codes = get_airport_codes()
    for item in airport_codes:
        if item['iata_code'] != None:
            iata_codes.append({
                'iataCode': item['iata_code'],
                'airport': item['name'],
                'countryCode': item['iso_country'],
                'city': item['municipality']
            })

    return iata_codes


def get_city_airports():
    airport_codes = get_airport_codes()
    cities_dict = {}
    index = 0
    for item in airport_codes:
        if item['iata_code'] is None:
            continue
        index += 1
        city = item['municipality']
        if city in cities_dict:
            cities_dict[city]['airports'].append({
                'iataCode': item['iata_code'],
                'airport': item['name'],
            })
        else:
            cities_dict[city] = {'city': city}
            cities_dict[city]['countryCode'] = item['iso_country']
            cities_dict[city]['airports'] = []
            cities_dict[city]['airports'].append({
                'iataCode': item['iata_code'],
                'airport': item['name'],
            })

    cities_array = []
    # convert to jsonArray
    for key, value in cities_dict.items():
        cities_array.append({
            'city': value['city'],
            'countryCode': value['countryCode'],
            'airports': value['airports']
        })
    return cities_array


country_codes = get_countries_dict()
iata_codes = get_iata_codes()
countries = {}
for item in iata_codes:
    if item['city'] is None:
        continue
    country_code = item['countryCode']
    if country_code not in countries:
        if country_code in country_codes:
            name = country_codes[country_code]
        else:
            name = ''
        countries[country_code] = Country(name, country_code)
    airport = Airport(item)
    hasCity = False
    for city in countries[country_code].cities:
        if city.name == item['city']:
            hasCity = True
            city.airports.append(airport)
            break
    if not hasCity:
        city = City(item['city'], country_code)
        city.airports.append(airport)
        countries[country_code].cities.append(city)

# convert countries from dict to json array
json_array = [value.toJSON() for key, value in countries.items()]
with open("output/countries_cities_airports.json", mode="w") as file:
    json.dump(json_array, file, indent=4)
