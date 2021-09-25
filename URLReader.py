import urllib.request

class URLReader(object):

    html = ''

    def __init__(self, url):
        #takes html for url and converts it into a string
        fp = urllib.request.urlopen(url)
        mybytes = fp.read()
        self.html = mybytes.decode("utf8")
        fp.close()

    def find(self, text):
        return self.html.find(text)

    def load_new_url(self, url):
        #takes html for url and converts it into a string
        fp = urllib.request.urlopen(url)
        mybytes = fp.read()
        self.html = mybytes.decode("utf8")
        fp.close()
        
    def get_text(self):
        return self.html

    def print(self):
        print(self.html)
