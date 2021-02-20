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
地方,駅名,読み(ひらがな),独占価格,独占後収益額,収益率,URL
北海道,洞爺湖,とうやこ,738億2000万円,43億800万円,6%,https://game8.jp/momotetsu-teiban/360951
北海道,札幌,さっぽろ,598億3000万円,28億6400万円,5%,https://game8.jp/momotetsu-teiban/360961
︙
```

## property_info.csv
- 物件毎のデータ
```
地方,駅名,物件名,タイプ,価格,収益率,収益額
北海道,洞爺湖,おふくいも屋,食品,1000万円,80%,800万円
北海道,洞爺湖,火山博物館,観光,8億円,1%,800万円
︙
```
