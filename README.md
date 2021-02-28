# momotetu-property
- [桃太郎電鉄 〜昭和 平成 令和も定番!〜](https://www.konami.com/games/momotetsu/teiban/)に登場する物件データのCSVファイルを作成する君
- [Game8の攻略ガイド](https://game8.jp/momotetsu-teiban/359686)からスクレイピングでデータを取得

# Requirements
- Python 3.7+

# Setup
```
$ pip install -r requirements.txt
```

# How to use
```
$ python momotetu_property.py
```

# Outputs
## monopoly_info.csv
- 物件駅毎のデータ
```
地方,駅名,読み(ひらがな),独占価格(百万),独占後収益額(百万),収益率(%),URL
北海道,洞爺湖,とうやこ,73820,4308,6,https://game8.jp/momotetsu-teiban/360951
北海道,札幌,さっぽろ,59830,2864,5,https://game8.jp/momotetsu-teiban/360961
︙
```

## property_info.csv
- 物件毎のデータ
```
地方,駅名,物件名,タイプ,価格(百万),収益率(%),収益額(百万)
北海道,洞爺湖,おふくいも屋,食品,10,80,8
北海道,洞爺湖,火山博物館,観光,800,1,8
︙
```
