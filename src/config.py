from random import choice
from pathlib import Path
from fake_useragent import UserAgent


class Settings:

    def __init__(self):
        self.fake_headers = UserAgent()

    headers = {
        "User-Agent": '',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
    }

    url_api_WB = "https://catalog.wb.ru/catalog/bl_shirts/catalog?TestGroup=no_test&TestID=no_test&appType=1&cat=8126&curr=rub&dest=-1257786&sort=popular&spp=27"
    url_api_WB_first = 'https://catalog.wb.ru/catalog/bl_shirts/catalog?TestGroup=no_test&TestID=no_test&appType=1&cat=8126&curr=rub&dest=-1257786'
    url_api_WB_second = '&sort=popular&spp=27'

    prox = [
        {"http": "socks5://217.29.63.40:12356"},
        {"http": "http://217.29.63.40:12355"},
        ]

    def get_path(self):
        abs_path: Path = Path(__file__).resolve().parent.parent
        return abs_path

    def get_headers(self):
        self.headers["User-Agent"] = self.fake_headers.random
        return self.headers

    def get_prox(self):
        return choice(self.prox)


settings = Settings()
