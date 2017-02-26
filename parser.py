from bs4 import BeautifulSoup
import urllib
import RAKE
import re
import cgi

from flask import Flask, render_template
from flask import request

app = Flask(__name__)

# endpoints have get post put patch delete etc http protocol. default is get
# @app.route('/')
# def parse_url():
# 	return get_keywords(url)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/form-url')
def urlForm():
    return render_template('page2.html')

@app.route('/submitUrl', methods=['POST'])
def submitUrl():
	url = request.form['link']
	print "hi it's working"
	get_keywords(url)
	return url

# @app.route('/', methods=['POST'])
# def words_post():
#     text = request.form.link
#     get_keywords(text)

# js will make a 'POST' to this url: 'http://127.0.0.1:5000/' and include the "url" paramater as an argument


def get_keywords(url):
	# Make below a function where the url is passed in
	r = urllib.urlopen(url).read()
	soup = BeautifulSoup(r)


	textWithTags = soup.findAll('p')

	#removes p tags
	noTags = ""
	for content in textWithTags:
		noTags += content.text

	#get keywords in tuple form
	Rake = RAKE.Rake("./SmartStoplist.txt");
	keywords = Rake.run(noTags)

	# for pairing in keywords:
	# 	word = pairing[0]
	# 	number = pairing[1]

	# instead of printing store these words and return them
	i = 0
	displayed = 0
	all_words = []
	while displayed < 20: 
		word = keywords[i][0]
		spaced_words = re.sub(r"\s+", ' ', word)
		all_words.append(spaced_words)
		displayed += 1
		i += 1

	return all_words

# form = cgi.FieldStorage()
# url =  form.getvalue('link')
# get_keywords(url)

if __name__ == '__main__':
	app.run(debug=True)


# You can use one of the stoplists included in the repository under stoplists/


