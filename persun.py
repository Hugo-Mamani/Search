#!/usr/bin/python

from bs4 import BeautifulSoup
import mechanize, base64
#import cookielib

#reload(sys)
#sys.setdefaultencoding('utf8')

keys = [
        'aHR0cHM6Ly90cmFtaXRlc3ljb25zdWx0YXMudG9wL2NvbW8tYnVzY2FyLWxhLWRpcmVjY2lvbi1kZS11bmEtcGVyc29uYS1wb3ItZG5pLWdyYXRpcy1lbi1wZXJ1LyNyZXN1bHRhZG9z',
        'aHR0cHM6Ly90cmFtaXRlc3ljb25zdWx0YXMudG9wL2J1c2Nhci1ub21icmVzLXktYXBlbGxpZG9zLXBvci1kbmkvI3Jlc3VsdGFkb3M='
        ]

class Start():

    inp = input("dni~>> ")

    settings = (lambda e: base64.b64decode(keys[e].encode('ascii')).decode('ascii'))
	
    br = mechanize.Browser()
    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.addheaders = [('User-agent', 'Firefox')]
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    #cj = cookielib.LWPCookieJar()
    #br.set_cookiejar(cj)

    br.open(settings(0))
    br.select_form(nr=2)
    br.form['txt_dni'] = inp
    br.submit()

    data = BeautifulSoup(br.response().read(), 'html5lib')

    res = str(data.find('p', attrs={'id': 'resultados'}).text).split(':')

    print(res[2][2:], Datas.geturl()[1])
    print(res)

