from dotenv import load_dotenv
import os
import requests
import time

load_dotenv()
api_key = os.getenv("YAHOO_API_KEY")

url = "https://map.yahooapis.jp/weather/V1/place?coordinates=139.732293,35.663613&output=json&appid=" + api_key

def access_api(url: str, retries: int = 3, delay: int = 300):
    """
    指定したURLにアクセスしてレスポンスを表示する関数
    - 200 OKならレスポンスをprint
    - エラーや例外ならリトライ（最大retries回）
    - リトライ間隔はdelay秒（デフォルト300秒 = 5分）
    """
    for attempt in range(1, retries +1):
        try:
            r = requests.get(url)
            if r.status_code == 200:
                print(r.text)
                return # 成功のため終了
            else:
                print(f"エラーです (status={r.status_code})")
                time.sleep(delay)
        except requests.RequestException as e:
            print(f"通信エラー: {e}")
            time.sleep(delay)

access_api(url) # URLアクセス用の関数呼び出し