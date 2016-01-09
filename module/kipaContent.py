from lxml import html
import requests


def ingredients(content):
    link = 'http://kapimda.kipa.com.tr/tr-TR/ProductDetail/ProductDetail/' + content

    page = requests.get(link)
    content = page.content.decode('utf-8')
    if content.find('indekiler') is not -1:
        tree = html.fromstring(content)
        additives = tree.xpath('//div[@class="longTextItems"]//p/text()')

        return additives[1].split(',')
    return []



#print additives

# http://kapimda.kipa.com.tr/tr-TR/ProductDetail/ProductDetail/5131570337 GOA
