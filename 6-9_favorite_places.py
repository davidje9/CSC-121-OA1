favorite_places = {
    'david': ['sorosis park','odds','kainos'],
    'meg': ['burnsville', 'rabbit rabbit'],
    'barry': ['bryce canyon'],
    }

for person in favorite_places.keys():
    print(f"\n{person.title()}'s favorite places include", end = " ")
    for place in favorite_places[person]:
            if favorite_places[person].index(place) == len(favorite_places[person]) - 1:
                print(place.title(), end = ".")
            else:
                print(place.title(), end = ", ")
