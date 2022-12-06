from bs4 import BeautifulSoup
import requests, base64

key = input("inserte dni ~ >> ")

if len(key) != 8 and not key.isnumeric:
    print("dni incorecta")
    exit(404)

settings = (lambda e: base64.b64decode(e.encode('ascii')).decode('ascii'))

with open("nets.txt", 'r') as file:
    uri, uri2, uri3 = file.readlines()
    net, net2, net3 = settings(uri), settings(uri2), settings(uri3)
    file.close()

def getnet(key):
    res = requests.post(net, data={'txt_dni':key}).text
    res2 = requests.get(net2.format(key)).text
    res3 = requests.get(net3.format(key)).text
    bs = BeautifulSoup(res, 'html5lib')
    bs2 = BeautifulSoup(res2, 'html5lib')
    bs3 = BeautifulSoup(res3, 'html5lib')
    tag = bs.find('p', id='resultados').contents
    name = f'{tag[5][1:]} {tag[8][1:]} {tag[11][1:]}'
    location = bs2.find('p', id='resultados').contents[4][2:]
    code = bs3.find('p', id='resultados').contents[5][1:]
    return f'{name} : {location} : {code}'

if __name__ == '__main__':
    output = getnet(key)
    print(output)


