import asyncio
import aiohttp
import pandas as pd
from src.config import settings
from aiohttp_retry import RetryClient, ExponentialRetry


class ParserWB:

    def __init__(self):
        self.head = settings.get_headers()
        self.path = settings.get_path()

    products = []

    def get_links_pages(self):

        links = []
        first_page = settings.url_api_WB

        try:

            for num_page in range(1, 50):
                if num_page < 2:
                    links.append(first_page)
                else:
                    link = settings.url_api_WB_first + f"&page={num_page}" + settings.url_api_WB_second
                    links.append(link)

            return links

        except Exception as ex:
            print(f"Error has been occured: {ex}")

    async def get_product(self, session, link, head):

        retry_options = ExponentialRetry(attempts=5)
        retry_client = RetryClient(raise_for_status=False, retry_options=retry_options, client_session=session, start_timeout=0.5)

        async with retry_client.get(url=link, headers=head) as response:

            try:

                json_products = await response.json()

                for product in json_products['data']['products']:

                    self.products.append({
                        "id": product["id"],
                        "brand": product["brand"],
                        "name": product["name"],
                        "price": product["priceU"] // 100,
                        "price_promo": product["salePriceU"] // 100
                        })

            except Exception as ex:
                print(f"Error has been occured: {ex}")

    async def get_products(self, links: list[str]) -> None:

        async with aiohttp.ClientSession(headers=self.head) as session:
                tasks = []
                for link in links:
                    task = asyncio.create_task(self.get_product(session=session, link=link, head=self.head))
                    tasks.append(task)
                await asyncio.gather(*tasks)

    def write_csv(self, file_name: str, data: list[dict]) -> None:
        pd.DataFrame(data).to_csv(f"{self.path}/data/{file_name}.csv", index=False)


if __name__ == "__main__":
    pars = ParserWB()
    links = pars.get_links_pages()
    asyncio.run(pars.get_products(links=links))
    pars.write_csv(file_name="products2", data=pars.products)
