import requests

APP_ID = "2c742695e566f3b6647ee0349db1fccaad5e254b"  
API_URL  = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"  


params = {
    "appId": APP_ID,  
    "statsDataId":"0003074210",  # 統計データID
    "metaGetFlg":"Y",  # メタ情報を取得
    "cntGetFlg":"N",  # 件数情報は取得しない
    "explanationGetFlg":"Y",  # 説明文を取得
    "annotationGetFlg":"Y",  # 注釈情報を取得
    "sectionHeaderFlg":"1", 
    "replaceSpChars":"0",  
    "lang": "J"  # 言語は日本語
}


response = requests.get(API_URL, params=params)
data = response.json()
print(data)

