import requests
import json
import random
import string
import click

def ipleak():
    requestv4 = requests.get("https://ipv4.ipleak.net/json/")

    if requestv4.status_code == 200:
        datav4 = requestv4.json()
        print(f"IPv4: {datav4['ip']}")

    try:
        requestv6 = requests.get("https://ipv6.ipleak.net/json/")
        datav6 = requestv6.json()
        print(f"IPv6: {datav6['ip']}")
    except Exception as e:
        pass

    if datav4:
        print(f"{datav4['country_name']} - {datav4['city_name']}")

    requestdns = requests.get(
        f"https://{get_random_string(40)}.ipleak.net/json/")
    if requestdns.status_code == 200:
        datadns = requestdns.json()
        print(
            f"DNS: {datadns['ip']} - {datadns['country_name']} - {datadns['city_name']}")

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

@click.command()
def main():
    ipleak()

if __name__ == "__main__":
    main()