from bs4 import BeautifulSoup
import urllib
import RAKE
import re

from flask import Flask
app = Flask(__name__)


@app.route('/b')
def parse_url():
	your_function()
	return 'Hello, World!'

# endpoints have get post put patch delete etc http protocol. default is get
@app.route('/')
def parse_url():
	your_function(url)
	return 'Hello, World!'

# js will make a 'POST' to this url: 'http://127.0.0.1:5000/' and include the "url" paramater as an argument

def your_function(url):
	# Make below a function where the url is passed in
	r = urllib.urlopen(url).read()
	soup = BeautifulSoup(r)


	textWithTags = soup.findAll('p')

	#removes p tags
	noTags = ""
	for content in textWithTags:
		noTags += content.text

	#get keywords in tuple form
	Rake = RAKE.Rake("/Users/catherineyang/Desktop/femmehacks/parsing/femme-hacks-2017/parsing/SmartStoplist.txt");
	keywords = Rake.run(noTags)

	# for pairing in keywords:
	# 	word = pairing[0]
	# 	number = pairing[1]

	# instead of printing store these words and return them
	i = 0
	displayed = 0
	while displayed < 20: 
		word = keywords[i][0]
		print re.sub(r"\s+", ' ', word)
		displayed += 1
		i += 1

if __name__ == '__main__':
	app.run(debug=True)



# You can use one of the stoplists included in the repository under stoplists/


