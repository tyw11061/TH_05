import sys
import urllib.request
import urllib.parse

if(len(sys.argv) >= 2 ):
	title = sys.argv[1]
else:
	title = input("title>")

templates = ['Persondata', 'Infobox 人物', 'ActorActress', 'Infobox Astronaut', 'Infobox aviator', 'Infobox Baduser', 'Infobox Buddhist', 'Infobox character', 'Infobox chef', 'Infobox Chess player', 'Infobox Christian leader', 'Infobox Dalai Lama', 'Infobox HelloProject', 'Infobox HelloProject2', 'Infobox Chinese-language singer and actor', 'Infobox Engineer', 'Infobox Given name', 'Infobox journalist', 'Infobox Judge', 'Infobox manner of address', 'Infobox medical person', 'Infobox Musician', 'Infobox Muslim scholars', 'Infobox Officeholder', 'Pharaoh Infobox', 'Infobox poker player', 'Infobox religious biography', 'Infobox Scientist', 'Infobox Serial Killer', 'Infobox vice-regal', '基礎情報 アナウンサー', 'Infobox 囲碁棋士', 'AV女優', 'Infobox オウム真理教徒', 'Infobox お笑い芸人', 'Infobox お笑いコンビ', '架空の人物', 'Infobox 学者', 'Infobox 革命家', '歌舞伎役者', '金庸人物', '基礎情報 軍人', 'Infobox 経済学者', 'Infobox 芸術家', 'Infobox 原画家', 'Infobox 建築家', 'Infobox 作家', '三国志の人物', 'Infobox 写真家', 'Infobox 殉教者', 'Infobox 将棋棋士', '女性アイドル', '女性モデル', '水滸伝の人物', '政治家', 'Infobox 聖人', '声優', '大統領', '男性モデル', '中華圏の人物', '調教師', '朝鮮の人物', 'Infobox 哲学者', '日本の脚本家', '日本の国会議員', 'Infobox 犯罪者', 'ベトナムの人物', 'Infobox 漫画家', '落語家', 'ラジオパーソナリティ', 'Infobox 利用者']

# dbg, json, none, php, txt, xml, yaml
data_format = "?format=txt"
data_action = "&action=query"
data_prop = "&prop=revisions"
data_titles = "&titles="+urllib.parse.quote(title)
data_rvprop = "&rvprop=content"

baseurl = "http://ja.wikipedia.org/w/api.php"
apiurl = baseurl + data_format + data_action + data_prop + data_titles + data_rvprop

reply = urllib.request.urlopen(apiurl).read().decode("utf-8")
open(title+"_base.txt","w").write(reply)

for temptitle in templates:
	if("{{"+temptitle in reply):
		infodata = []
		lines = reply.splitlines()
		flag = False
		for l in lines:
			if(flag):
				if(l[0]=="|"):
					infodata.append(l)
				elif("<!--" not in l):
					break
			else:
				if("{{"+temptitle in l):
					flag=True
			
		info = {}
		for l in infodata:
			if(l[0] == "|"):
				key = l.split(" =")[0][1:].replace(" ","")
				if(l.split(" =")[1] == "" or l.split(" =")[1] == " "):
					value = None
				elif(l.split(" =")[1][1:5] == "<!--"):
					value = None
				else:
					#value = re.sub("[\[\]]","",l.split(" = ")[1])
					value = l.split(" =")[1][1:]
				info[key] = value
		open(title+".txt","w").write(str(info))
		break
