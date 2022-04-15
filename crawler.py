from urllib.request import urlopen
import urllib.parse
from bs4 import BeautifulSoup

charNM = "웨르끼"
charNM = urllib.parse.quote(charNM)
html = urlopen("https://lostark.game.onstove.com/Profile/Character/"+charNM)
#print(charNM)

#bs = BeautifulSoup(html, "html.parser")
bs = BeautifulSoup(html, "lxml")
#서버명
serverNM = bs.select_one('.profile-character-info__server').get_text().replace("@","")
#전투레벨

level = bs.select('.profile-ingame .level-info__item span')[1].get_text()

#캐릭명
originCharNM = bs.select_one('.profile-character-info__name').get_text()

#템렙
itemlevel = bs.select('.profile-ingame .level-info2__item span')[1].get_text()
print(level, originCharNM, itemlevel)
##https://cdn-lostark.game.onstove.com/2018/obt/assets/images/common/thumb/blade.png


charDiv = bs.find('div',{"id":'expand-character-list'})
servers = charDiv.find_all('strong', {"class": "profile-character-list__server"})
chars = charDiv.find('ul', {"class": "profile-character-list__char"})
print(servers)