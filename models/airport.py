import json

class Airport:
    def __init__(self, airport):
        self.name = airport['airport']
        self.iata_code = airport['iataCode']
        self.city = airport['city']
        self.country_code = airport['countryCode']

    def __str__(self):
        return f"{self.name}, {self.iata_code}"

    def toJSON(self):
        return {
            'name': self.name,
            'iata_code': self.iata_code,
            'city': self.city,
            'country_code': self.country_code,
        }
