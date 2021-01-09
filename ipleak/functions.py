from ipleak.app import console


def print_ipleak_data(name: str, data: dict) -> None:
    if 'country_name' in data and 'city_name' in data and data['country_name'] != None and data['city_name'] != None:
        console.print(
            f'{name}: {data["ip"]} - {data["country_name"]} {data["city_name"]}')
    elif 'country_name' in data and data['country_name'] != None:
        console.print(f'{name}: {data["ip"]} - {data["country_name"]}')
    else:
        console.print(f'{name}: {data["ip"]}')
    return True
