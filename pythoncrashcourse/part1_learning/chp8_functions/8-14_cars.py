def cars(manufacturer, model, **car_info):
    """Store information about a car in a dictionary."""

    car_info["manufacturer"] = manufacturer
    car_info["model"] = model
    return car_info

car_dict = cars("subaru","outback",color = "blue", tow_package = True)


print(car_dict)