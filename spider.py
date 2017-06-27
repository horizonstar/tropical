# -*- coding: utf-8 -*-

import urllib2

new = urllib2.urlopen('http://www.baidu.com')
html = new.read()

print html