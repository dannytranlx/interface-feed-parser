import BeautifulSoup
import urllib2

class InterfaceFeedParserApp:
	def run(self):
		WebParser().find_posts()

class WebParser:
	def __init__(self):
		self.url_interface = "http://interfaceets.wordpress.com/feed/"

	def find_posts(self):
		webparser = []

		try:
			webparser = BeautifulSoup.BeautifulStoneSoup(urllib2.urlopen("http://interfaceets.wordpress.com/feed/").read())
		except:
			print 'Error: Cannot parse url'

if __name__ == "__main__":
	InterfaceFeedParserApp().run()