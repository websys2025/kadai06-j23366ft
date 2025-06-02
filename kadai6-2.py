# kadai6-2.py

# エンドポイント: https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json
# 機能: 指定地域（東京都）の天気、降水確率、気温を取得
# 使い方: requestsライブラリでGETリクエストを送信し、JSONで表示

import requests

url = "https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json"
data = requests.get(url).json()

print("=== 東京都の天気予報 ===")

d0 = data[0]
ts = d0["timeSeries"][0]
td = ts["timeDefines"]
ar = ts["areas"][0]
name = ar["area"]["name"]
w0 = ar["weathers"][0]
w1 = ar["weathers"][1]
w2 = ar["weathers"][2]

print("【" + name + "】")
print(td[0] + " の天気: " + w0)
print(td[1] + " の天気: " + w1)
print(td[2] + " の天気: " + w2)
