def build_car(make, model, **car_info):
    """Store information about a car in a dictionary."""
    car_info['make'] = make
    car_info['model'] = model
    return car_info

car = build_car('subaru', 'outback', color='blue', tow_package=True)

print(car)
