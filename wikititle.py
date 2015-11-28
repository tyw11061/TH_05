import urllib.request
import urllib.parse
name=open("name.dat","r").read()

encodedname = urllib.parse.quote(name)
html = urllib.request.urlopen("http://search.yahoo.co.jp/search?p="+encodedname+"&vs=ja.wikipedia.org").read().decode("UTF-8")


print(html)
