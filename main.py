# -*- coding: utf-8 -*-

import time
import sys
import codecs
import lxml.html
import urllib2

query = 'http://www39.atwiki.jp/osakahennyu/?cmd=backup&action=source&pageid=<PLACEHOLDER>&num=0'

for line in open(sys.argv[1], 'r'):
	url = query.replace('<PLACEHOLDER>', line.rstrip())

	while True:
		try:
			html = urllib2.urlopen(url)

			code = unicode(html.read(), 'utf-8')
			dom  = lxml.html.fromstring(code)
			wiki = dom.xpath('//pre')[0]
			
			fout = codecs.open(line.rstrip() + '.txt', 'w', 'utf-8')
			fout.write(wiki.text)
			fout.close()

			html.close()
			break
			
		except urllib2.HTTPError:
			raw_input('>>> error! press continue...')

	time.sleep(1)