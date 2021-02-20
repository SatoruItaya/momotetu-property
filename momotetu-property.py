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
    monopoly_info_header = ["地方", "駅名", "読み(ひらがな)", "独占価格", "独占後収益額", "収益率"]
    monopoly_info_list.append(monopoly_info_header)

    property_info_list = []
    property_info_header = ["地方", "駅名", "物件名", "タイプ", "価格", "収益率", "収益額"]
    property_info_list.append(property_info_header)

    for region in region_table:

        property_station_list = region.find_all("tr")[1:]

        for property_station in property_station_list:

            station_page_anchor = property_station.find("a")
            station_soup = get_bs(station_page_anchor.get("href"))

            basic_info_table = station_soup.find_all("table", class_="a-table a-table a-table")[0]

            monopoly_info_record = []
            # 地方
            monopoly_info_record.insert(0, basic_info_table.find_all("td")[3].text)
            # 駅名
            monopoly_info_record.insert(1, property_station.find_all("td")[0].text)
            # 読み(ひらがな)
            monopoly_info_record.insert(2, basic_info_table.find_all("td")[4].text)
            # 独占価格
            monopoly_info_record.insert(3, basic_info_table.find_all("td")[1].text)
            # 独占後収益額
            monopoly_info_record.insert(4, basic_info_table.find_all("td")[2].text)
            # TODO 収益率
            monopoly_info_record.insert(5, property_station.find_all("td")[3].text)

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
                property_info_record.insert(4, property_info.find_all("td")[2].text)
                # 収益率
                property_info_record.insert(5, property_info.find_all("td")[3].text)
                # 収益額
                property_info_record.insert(6, property_info.find_all("td")[4].text)

                property_info_list.append(property_info_record)

            break

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


if __name__ == "__main__":
    gen_propery_csv()
