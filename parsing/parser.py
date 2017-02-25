from bs4 import BeautifulSoup
import urllib
import RAKE
import re


r = urllib.urlopen('https://www.squarespace.com/about/careers?gh_jid=108575').read()
soup = BeautifulSoup(r, "lxml")


textWithTags = soup.findAll('p')

#removes p tags
noTags = ""
for content in textWithTags:
	noTags += content.text

#get keywords in tuple form
Rake = RAKE.Rake("/Users/reginalin/Desktop/femmehacks/femme-hacks-2017/parsing/stoplists/SmartStoplist.txt");
keywords = Rake.run(noTags)

# for pairing in keywords:
# 	word = pairing[0]
# 	number = pairing[1]

i = 0
displayed = 0
while displayed < 20: 
	word = keywords[i][0]
	print re.sub(r"\s+", ' ', word)
	displayed += 1
	i += 1





# You can use one of the stoplists included in the repository under stoplists/


