import requests
import urllib.request
import os

class Downloader:
    def __init__(self, url):
        self.url = url
        self.vid_title = ''
        self.code = ''
        self.vid_URL = ''
        self.bin_URL = ''

    def find_code(self):
        url = self.url
        init_loc = url.find('wvideo=') + len('wvideo=')
        end_loc = url.find('">')
        code = url[init_loc:end_loc]
        self.code = code

    def find_title(self):
        url = self.url
        init_loc = url.rfind('">') + len('">')
        end_loc = url.rfind('.')
        title = url[init_loc:end_loc]
        self.vid_title = title

    def find_vid_URL(self):
        self.vid_URL = 'http://fast.wistia.net/embed/iframe/' + str(self.code)

    def find_bin_URL(self):
        r = requests.get(self.vid_URL)
        source = str(r.text)
        init_loc = source.find('http://embed.wistia.com/deliveries/')
        end_loc = source.find('.bin') + len('.bin')
        url = source[init_loc:end_loc]
        self.bin_URL = url

    def download_vid(self):
        self.find_code()
        self.find_vid_URL()
        self.find_bin_URL()

        url = self.bin_URL
        self.find_title()
        print('Downloading [fileName: {}] to [directory: {}]'.format(str(self.vid_title), os.getcwd()))
        urllib.request.urlretrieve(url, str(self.vid_title) + '.mp4')

# a = '<p><a href="https://acdcecon.thinkific.com?wvideo=n36ca9ppri"><img src="https://s3.amazonaws.com/thinkific-import/171244/PQWrZtW3RKGnzZlzEEzw_Practice Comparative Advantage Pic.jpg" width="400" height="225" style="width: 400px; height: 225px;"></a></p><p><a href="https://acdcecon.thinkific.com?wvideo=n36ca9ppri">Comparative Advantage Practice.mp4</a></p>'
# d = Downloader(a)
# d.download_vid()