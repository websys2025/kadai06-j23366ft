import requests

APP_ID = "2c742695e566f3b6647ee0349db1fccaad5e254b"  
API_URL  = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"  
#endpoint

params = {
    "appId": APP_ID,  
    "statsDataId":"0003074210",  # 統計データID
    #学校基本調査 / 平成２３年度以降 高等教育機関《報告書掲載集計》 学校調査 高等専門学校
    "metaGetFlg":"Y",  # メタ情報を取得
    "cntGetFlg":"N",  # 件数情報は取得しない
    "explanationGetFlg":"Y",  # 説明文を取得
    "annotationGetFlg":"Y",  # 注釈情報を取得
    "sectionHeaderFlg":"1", 
    "replaceSpChars":"0",  
    "lang": "J"  # 言語は日本語
}

#使い方:己のIDでゲットリクエストを送り、statsDataIdに使いたい
#統計データIDを置く、その後パラメータを指定し、リクエストを送り、表示する。
response = requests.get(API_URL, params=params)#APIへGETリクエスト
data = response.json()
print(data)

