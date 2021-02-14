from bs4 import BeautifulSoup
import requests


def gen_propery_csv():

    home_url = "https://game8.jp/momotetsu-teiban/359686"
    region_list = ["北海道", "東北", "関東", "中部", "近畿", "中国", "四国", "九州沖縄"]

    soup = get_bs(home_url)

    property_info = soup.find_all("table", class_="a-table a-table a-table")
    print(property_info)


def get_bs(url):

    res = requests.get(url)
    return BeautifulSoup(res.text, "html.parser")


if __name__ == "__main__":
    print(gen_propery_csv())
