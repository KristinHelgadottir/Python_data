import urllib.request
import os

def download(url, path = './'):
    filename = url.split("/")[-1]
    fullfilename = os.path.join(path, filename)
    file_name, headers = urllib.request.urlretrieve(url, fullfilename)
