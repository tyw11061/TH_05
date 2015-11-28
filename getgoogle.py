# 参考：http://bluele.hatenablog.com/entry/2013/08/24/001128
from urllib.parse import urlencode
from urllib.request import build_opener, urlopen, HTTPCookieProcessor
from http.cookiejar import CookieJar
import sys

def search_image(url):
	params = {
		'image_url': url,
		'hl': 'ja',
		}
	query = BASE_SEARCH_URL % urlencode(params)
	f = Opener.open(query)
	url = f.url
	f = Opener.open(url)
	html = f.read().decode("UTF-8")
	return html

def extract_name(html):
	if("この画像の最良の推測結果" in html):
		html = html[html.index("この画像の最良の推測結果"):]
		html = html[:html.index("</a>")]
		name = html[html.rindex('>')+1:]
		return name
	else:
		return "NotFound"

BASE_SEARCH_URL = 'https://www.google.co.jp/searchbyimage?%s'

Opener = build_opener(HTTPCookieProcessor(CookieJar()))
Opener.addheaders = [
	('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0'),
	('Accept-Language','ja,en-us;q=0.7,en;q=0.3')
]

url = sys.argv[1]
html = search_image(url)
open("name.dat","w").write(extract_name(html))
