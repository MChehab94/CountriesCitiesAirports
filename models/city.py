from models.airport import Airport
import json


class City:

    def __init__(self, name: str, country_code: str):
        self.name = name
        self.country_code = country_code
        self.airports = []

    def add_airport(self, airport: Airport):
        self.airports.append(airport)

    def __str__(self):
        return f"{self.name}, {self.airports}"

    def toJSON(self):
        return {
            'name': self.name,
            'country_code': self.country_code,
            'airports': [airport.toJSON() for airport in self.airports]
        }
