from click.termui import style
import requests
import random
import string
import json
import click
import typer
from rich.console import Console

app = typer.Typer()
console = Console()

url_ipv4 = "https://ipv4.ipleak.net/json/"
url_ipv6 = "https://ipv6.ipleak.net/json/"
url_dns = f"https://{''.join(random.choice(string.ascii_lowercase) for i in range(40))}.ipleak.net/json/"


def get_ipleak_url(version: str, url: str) -> dict:
    try:
        request = request = requests.get(url)
        if request.status_code == 200:
            data = request.json()
            return data

    except Exception as e:
        console.print(f'{version}: not available.', style='bold red')
        return {}


def print_ipleak_data(name: str, data: dict) -> None:
    if 'country_name' in data and 'city_name' in data and data['country_name'] != None and data['city_name'] != None:
        console.print(
            f'{name}: {data["ip"]} - {data["country_name"]} {data["city_name"]}')
    elif 'country_name' in data and data['country_name'] != None:
        console.print(f'{name}: {data["ip"]} - {data["country_name"]}')
    else:
        console.print(f'{name}: {data["ip"]}')


@app.command()
def ipv4():
    with console.status('[bold green]Getting IPv4...') as status:
        data = get_ipleak_url("IPv4", url_ipv4)
        if data is not {}:
            print_ipleak_data("IPv4", data)


@app.command()
def ipv6():
    with console.status('[bold green]Getting IPv6...') as status:
        data = get_ipleak_url("IPv6", url_ipv6)
        if data is not {}:
            print_ipleak_data("IPv6", data)


@app.command()
def dns():
    with console.status('[bold green]Getting DNS...') as status:
        data = get_ipleak_url("DNS", url_dns)
        if data is not {}:
            print_ipleak_data("DNS", data)


@app.command()
def all():
    ipv4()
    ipv6()
    dns()


def main():
    app()


if __name__ == "__main__":
    main()
