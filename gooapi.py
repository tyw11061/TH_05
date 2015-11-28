import json
import urllib.request
import sys

if(len(sys.argv) >= 2):
	sentence = sys.argv[1]
else:
	sentence = input("> ")



# APIで送信するデータを格納する変数
apidata = {
"app_id":"5492f152c45a3270ea40990b66b8d3dd658312f356c09d6866363876e3fe2186",
"request_id":"test",
"sentence":sentence,
"class_filter":"ART|ORG|PSN|LOC|DAT|TIM"
}

# url_api:APIのリクエストURLとAPIKEYを接続し、APIのクエリURLを生成
url_api = "https://labs.goo.ne.jp/api/entity"
# apidata_encode:apiに使用するデータapidataをJSON規格で表記し、エンコードしたバイナリデータ
apidata_encoded = json.dumps(apidata).encode("utf-8")
# request_api:url_apiにapidata_encodedをPOST方式で送信するリクエスト
request_api = urllib.request.Request(url_api, apidata_encoded)
# 送信するHTMLのヘッダに、JSON規格のデータであることを明示
request_api.add_header('Content-Type', 'application/json')
# response_api:APIにリクエストを送信し、返って来たバイナリデータ
response_api = urllib.request.urlopen(request_api).read()
# response_apiをデコードする。辞書の形をした文字列となるため、eval関数(入力文字列をそのまま命令文として処理する関数)を通して辞書に変換する
response_api = eval(response_api.decode("utf-8"))

print(response_api["ne_list"])
