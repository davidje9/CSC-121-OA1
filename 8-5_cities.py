def describe_city(city, country="mexico"):
    """state city and its country in a single sentence"""
    print(f"{city.title()} is in {country.title()}.")

describe_city("the dalles", "the united states of america")
describe_city("oaxaca")
describe_city(country = "japan", city = "osaka")
