A simple python script that converts the data from https://datahub.io/core/airport-codes into the following JSON structure:
```json
[
    {
        "name": "country_name",
        "code": "country_code",
        "cities": [
            {
                "name": "city_name",
                "country_code": "country_code",
                "airports": [
                    {
                        "name": "airport_name",
                        "iata_code": "iata_code",
                        "city": "city_name",
                        "country_code": "country_code"
                    }
                ]
            }
        ]
    }
]
```

The original data, `files/airport-iatas.json` has some records where the `iata_code` is `null`. These records are discarded and are **not** added 
to the list, so that the final output has no `null` records.

The output of the script is in `output/countries_cities_airports.json`
