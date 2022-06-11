from models.city import City


class Country:
    def __init__(self, name, country_code):
        self.name = name
        self.country_code = country_code
        self.cities = []

    def add_city(self, city: City):
        self.cities.append(city)

    def __str__(self):
        return f"{self.name}, {self.country_code, self.cities}"

    def toJSON(self):
        return {
            'name': self.name,
            'code': self.country_code,
            'cities': [city.toJSON() for city in self.cities if len(city.airports) > 0]
        }
