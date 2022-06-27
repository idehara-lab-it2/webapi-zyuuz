import requests
import json
from html import escape

# 検索語を入力
s = input('検索＞')

# 日本語表示(language)、検索対象範囲を日本(country)、検索を入力文字列(term) として webAPI を実行
# このとき、文字列は "html escape" する必要がある
response = requests.get('https://itunes.apple.com/search?country=JP&language=ja_jp&term='+escape(s))

# 結果の文字列を json 型に変換
data = response.json()

# とりあえず全部表示
print(json.dumps(data, indent=4, ensure_ascii=False).encode().decode())

# 件数の表示
print('検索結果：' + str(data['resultCount']) + ' 件')
