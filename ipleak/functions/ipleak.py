from ipleak.exceptions import NoIPFound


def ipleak_string(name: str, data: dict) -> str:
    if 'ip' in data:
        msg = ""
        msg += f'{name}: {data["ip"]}'
        if 'country_name' in data and data['country_name'] != None:
            msg += f' - {data["country_name"]}'
        if 'city_name' in data and data['city_name'] != None:
            msg += f' - {data["city_name"]}'
        return msg
    else:
        raise NoIPFound
