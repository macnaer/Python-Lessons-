import requests

URL = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"


def request(URL):
    responce = requests.get(URL)
    return responce.json()


currency = request(URL)

for item in currency:
    print(item["ccy"], " ", item["base_ccy"],
          " ", item["buy"], " ", item["sale"])
