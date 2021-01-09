from click.termui import style
import requests
import random
import string
import json
import click
from requests.sessions import HTTPAdapter
from ipleak.config import settings

from ipleak.app import app, console
from ipleak.functions import *


def get_ipleak_url(version: str, url: str) -> dict:
    try:
        session = requests.Session()
        session.mount('https://', HTTPAdapter(max_retries=5))
        request = session.get(url)
        if request.status_code == 200:
            data = request.json()
            if 'ip' in data:
                return data
            else:
                console.print(f'{version}: not available.', style='bold red')
                return None
        else:
            console.print(f'{version}: not available.', style='bold red')
            return None

    except Exception as e:
        console.print(f'{version}: not available.', style='bold red')
        return None


@app.command()
def ipv4():
    with console.status('[bold green]Getting IPv4...') as status:
        data = get_ipleak_url("IPv4", settings.url_ipv4)
        if data is not None:
            print_ipleak_data("IPv4", data)


@app.command()
def ipv6():
    with console.status('[bold green]Getting IPv6...') as status:
        data = get_ipleak_url("IPv6", settings.url_ipv6)
        if data is not None:
            print_ipleak_data("IPv6", data)


@app.command()
def dns():
    with console.status('[bold green]Getting DNS...') as status:
        data = get_ipleak_url("DNS", settings.url_dns)
        if data is not None:
            print_ipleak_data("DNS", data)


@app.command()
def all():
    ipv4()
    ipv6()
    dns()
