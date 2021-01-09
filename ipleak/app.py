import typer
from rich.console import Console

app = typer.Typer()  # nopep8
console = Console()  # nopep8

from ipleak.exceptions import NoIPFound
from ipleak.config import settings
from ipleak.functions.http import get_url
from ipleak.functions.ipleak import ipleak_string


@app.command()
def ipv4():
    with console.status('[bold green]Getting IPv4...') as status:
        data = get_url(settings.url_ipv4)
        if data is not {}:
            try:
                console.print(ipleak_string("IPv4", data))
            except NoIPFound as e:
                console.print(f'IPv4: not available.', style='bold red')


@app.command()
def ipv6():
    with console.status('[bold green]Getting IPv6...') as status:
        data = get_url(settings.url_ipv6)
        if data is not {}:
            try:
                console.print(ipleak_string("IPv6", data))
            except NoIPFound as e:
                console.print(f'IPv6: not available.', style='bold red')


@app.command()
def dns():
    with console.status('[bold green]Getting DNS...') as status:
        data = get_url(settings.url_dns)
        if data is not {}:
            try:
                console.print(ipleak_string("DNS", data))
            except NoIPFound as e:
                console.print(f'DNS: not available.', style='bold red')


@app.command()
def all():
    ipv4()
    ipv6()
    dns()
