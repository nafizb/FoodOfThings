from lxml import html
import requests
import re

def ingredients(productID):
    link = 'http://kapimda.kipa.com.tr/tr-TR/ProductDetail/ProductDetail/' + productID

    page = requests.get(link)
    content = page.content.decode('utf-8')
    if content.find('indekiler') is not -1:
        '''
        tree = html.fromstring(content)
        additives = tree.xpath('//div[@class="longTextItems"]//p/text()')
        '''

        pattern = re.compile('<h3>İçindekiler</h3><div class="longTextItems"><p>(.*?)</p>')

        match = pattern.findall(content)

        scrappedhtml = re.sub('<.{1,2}>', '', match[0].replace(' içerir', ''))
        brackets = re.findall('\((.*?)\)', scrappedhtml)
        return brackets

        #return match

        #return additives[1].split(',')

    return []

#for test

print (ingredients("5114978074"))

#print additives

# http://kapimda.kipa.com.tr/tr-TR/ProductDetail/ProductDetail/5131570337 GOA
