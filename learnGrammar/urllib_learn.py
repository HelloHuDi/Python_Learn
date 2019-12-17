# -*- coding:utf-8 -*-
# Created by hd on 2017/12/5 .
import urllib.request
import ssl

# context = ssl._create_unverified_context()

ssl._create_default_https_context = ssl._create_unverified_context

url = 'http://blog.csdn.net/permike/article/details/52437492'

url2 = 'http://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}


# # req = urllib.request.Request(url, headers=headers)
# for line in urllib.request.urlopen(url2):
#     line = line.decode('utf-8')  # Decoding the binary data to text.
#     if 'EST' in line or 'EDT' in line:  # look for Eastern Time
#         print(line)


def download(_url):
    try:
        req = urllib.request.Request(_url, headers=headers)
        return urllib.request.urlopen(req).read()
    except:
        return None


csdn = download(url)
print(csdn)
