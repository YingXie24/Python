def get_formatted_city(city, country, population=None):
    """Return a single string of containing City, Country."""
    if population:
        full_city = f"{city}, {country} - population {population}"
    else:
        full_city = f"{city}, {country} - population unknown"
    return full_city.title()
