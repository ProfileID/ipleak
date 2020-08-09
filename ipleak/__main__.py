import requests
import json
import random
import string
import click


class IPLeak():
    def __init__(self):
        self.urlIPv4 = "https://ipv4.ipleak.net/json/"
        self.urlIPv6 = "https://ipv6.ipleak.net/json/"
        self.urlDNS = f"https://{self.get_random_string(40)}.ipleak.net/json/"

        self.getIP(self.urlIPv4, "IPv4")
        self.getIP(self.urlIPv6, "IPv6")
        self.getIP(self.urlDNS, "DNS")

    def get_random_string(self, length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        
        return result_str

    def getIP(self, url, title):
        try:
            request = requests.get(url)
            if request.status_code == 200:
                data = request.json()

                if title:
                    print()
                    print(f"--- {title} ---")

                print(f"{data['ip']}")

                if "country_name" in data and data["country_name"] is not None:
                    print(f"Country: {data['country_name']}")

                if "city_name" in data and data["city_name"] is not None:
                    print(f"City: {data['city_name']}")

        except Exception as e:
            print()
            if title:
                print(f"--- {title} ---")
            print("Not available")


@click.command()
def main():
    IPLeak()


if __name__ == "__main__":
    main()
