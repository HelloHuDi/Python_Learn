# -*- coding:utf-8 -*-
# Created by hd on 2017/12/5 .
import urllib.request


def download(url):
    try:
        return urllib.request.urlopen(url).read()
    except:
        return None


csdn = download("http://blog.csdn.net/permike/article/details/52437492")
print(csdn)
