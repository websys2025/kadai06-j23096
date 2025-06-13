import requests
#国家公務員死因調査
APP_ID = "fddf8cd7b0768c8b6dbe5fb4054bddab42ab94ae"
API_URL  = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

params = {
    "appId": APP_ID,
    "statsDataId":"0003343391",

    "cdArea":"12101,12102,12103,12104,12105,12106",
    "cdCat01": "A1101",
    
    "metaGetFlg":"Y",
    "cntGetFlg":"N",
    "explanationGetFlg":"Y",
    "annotationGetFlg":"Y",
    "sectionHeaderFlg":"1",
    "replaceSpChars":"0",
    "lang": "J"  # 日本語を指定
    
}



#response = requests.get(API_URL, params=params)
response = requests.get(API_URL, params=params)
# Process the response
data = response.json()
print(data["GET_STATS_DATA"])

