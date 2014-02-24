from flask import Flask
from flask import render_template
from bs4 import BeautifulSoup
import urllib2

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html', data = fetch_posts())

def fetch_posts():
	url_interface = "http://interfaceets.wordpress.com/feed/"
	webparser = []
	data = ""
	snippet_len = 800

	try:
		webparser = BeautifulSoup(urllib2.urlopen(url_interface).read(), "xml")
	except:
		print 'Erreur: Impossible de lire le fil RSS'

	if webparser:
		posts = webparser.channel.findAll('item')
		for post in posts:
			data += '<h1><a href="' + post.link.string + '">' + post.title.string + '</a></h1>'
				
			subtitles_len = post.encoded.string.index('</h6>') + len('</h6>')
			
			data += post.encoded.string[:subtitles_len].replace('<br />', ' - ')
			data += BeautifulSoup(post.encoded.string[subtitles_len:snippet_len + subtitles_len]).prettify()

	if data:
		return data

	return 'Aucun article trouv&eacute;'

if __name__ == "__main__":
	app.run()
