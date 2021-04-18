from bs4 import BeautifulSoup
import requests
import csv


def gen_propery_csv():

    home_url = "https://game8.jp/momotetsu-teiban/359686"

    soup = get_bs(home_url)

    region_table = soup.find_all("table", class_="a-table a-table a-table")

    property_station_list = []

    # Definition of Lists for CSV
    monopoly_info_list = []
    monopoly_info_header = ["地方", "駅名", "読み(ひらがな)", "独占価格(百万)", "独占後収益額(百万)", "収益率(%)", "URL"]
    monopoly_info_list.append(monopoly_info_header)

    property_info_list = []
    property_info_header = ["地方", "駅名", "物件名", "タイプ", "価格(百万)", "収益率(%)", "収益額(百万)"]
    property_info_list.append(property_info_header)

    for region in region_table:

        property_station_list = region.find_all("tr")[1:]

        for property_station in property_station_list:

            station_page_anchor = property_station.find("a")
            station_page_link = station_page_anchor.get("href")
            station_soup = get_bs(station_page_link)

            basic_info_table = station_soup.find_all("table", class_="a-table a-table a-table")[0]

            monopoly_info_record = []
            # 地方
            monopoly_info_record.insert(0, basic_info_table.find_all("td")[3].text)
            # 駅名
            monopoly_info_record.insert(1, property_station.find_all("td")[0].text)
            # 読み(ひらがな)
            monopoly_info_record.insert(2, basic_info_table.find_all("td")[4].text)
            # 独占価格
            monopoly_info_record.insert(3, transform_to_million_units(basic_info_table.find_all("td")[1].text))
            # 独占後収益額
            monopoly_info_record.insert(4, transform_to_million_units(basic_info_table.find_all("td")[2].text))
            # 収益率
            monopoly_info_record.insert(5, property_station.find_all("td")[3].text.replace("%", ""))
            # URL
            monopoly_info_record.insert(6, station_page_link)
            # TODO event

            monopoly_info_list.append(monopoly_info_record)

            property_info_table = station_soup.find_all("table", class_="a-table a-table a-table")[1]
            property_num = len(property_info_table.find_all("tr")) - 1

            for i in range(property_num):

                property_info = property_info_table.find_all("tr")[i + 1]

                property_info_record = []
                # 地方
                property_info_record.insert(0, basic_info_table.find_all("td")[3].text)
                # 駅名
                property_info_record.insert(1, property_station.find_all("td")[0].text)
                # 物件名
                property_info_record.insert(2, property_info.find_all("td")[0].text)
                # タイプ
                property_info_record.insert(3, property_info.find_all("td")[1].text)
                # 価格
                property_info_record.insert(4, transform_to_million_units(property_info.find_all("td")[2].text))
                # 収益率
                property_info_record.insert(5, property_info.find_all("td")[3].text.replace("%", "").replace("％", ""))
                # 収益額
                property_info_record.insert(6, transform_to_million_units(property_info.find_all("td")[4].text))

                property_info_list.append(property_info_record)

    # CSV処理
    with open('monopoly_info.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(monopoly_info_list)

    with open('property_info.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(property_info_list)


def get_bs(url):

    res = requests.get(url)
    return BeautifulSoup(res.text, "html.parser")


def transform_to_million_units(kanji_price_yen):

    # truncate "円"
    kanji_price = kanji_price_yen.replace("円", "")

    million_units = 0

    trillion_place = kanji_price.find("兆")

    # contain "兆"
    if trillion_place > -1:
        trillion = kanji_price[:trillion_place]
        million_units += int(trillion) * 1000000

    billion_place = kanji_price.find("億")

    # contain "億"
    if billion_place > -1:
        billion = kanji_price[trillion_place + 1:billion_place]
        million_units += int(billion) * 100

    ten_thousand_place = kanji_price.find("万")

    # contain "万"
    if ten_thousand_place > -1:
        ten_thousand = kanji_price[billion_place + 1:ten_thousand_place]
        million_units += int(ten_thousand) / 100

    return "%g" % million_units


if __name__ == "__main__":
    gen_propery_csv()
