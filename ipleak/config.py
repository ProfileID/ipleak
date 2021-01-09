import random
import string


class Settings(object):
    url_ipv4 = "https://ipv4.ipleak.net/json/"
    url_ipv6 = "https://ipv6.ipleak.net/json/"
    url_dns = f"https://{''.join(random.choice(string.ascii_lowercase) for i in range(40))}.ipleak.net/json/"


settings = Settings()
