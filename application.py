from flask import Flask
from bs4 import BeautifulSoup
import urllib2
import re

app = Flask(__name__)

@app.route("/")
def fetch_posts():
	url_interface = "http://interfaceets.wordpress.com/feed/"
	webparser = []
	data = ""
	snippet_len = 350

	try:
		webparser = BeautifulSoup(urllib2.urlopen(url_interface).read(), "xml")
	except:
		print 'Error: Cannot parse url'

	if webparser:
		posts = webparser.channel.findAll('item')
		for post in posts:
			data += '<h1><a href="' + post.link.string + '">' + post.title.string + '</a></h1>'
				
			subtitles_len = post.encoded.string.index('</h6>') + len('</h6>')
			
			data += post.encoded.string[:subtitles_len].replace('<br />', ' - ')
			data += post.encoded.string[subtitles_len:snippet_len + subtitles_len]

	if data:
		return data

	return 'yolo'

if __name__ == "__main__":
	app.run()