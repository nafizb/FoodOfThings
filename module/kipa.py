import time
from lxml import html
import math
import requests
import re
from module.kipaContent import ingredients

baseUrl = "http://kapimda.kipa.com.tr/tr-TR/"

catUrl = "Product/BrowseProducts?taxonomyID=Cat00000336&pageNo=1&sortBy=Default"

targetUrl = baseUrl + catUrl

'''
print("http://kapimda.kipa.com.tr/tr-TR/Product/BrowseProducts?taxonomyID=Cat00000336&pageNo=1&sortBy=Default")

listSource2 = urllib.request.urlopen(targetUrl)

listSource = listSource2.read().decode('windows-1252')
'''

listSource = requests.get(targetUrl).content.decode("utf-8")

pageCountPattern = '<span>1&nbsp;-&nbsp;24&nbsp;/&nbsp;([0-9]+)&nbsp;</span>gösteriliyor'

p = re.compile(pageCountPattern)
productCount = p.findall(listSource)[0]

pageCount = math.ceil(int(productCount) / 24)


tree = html.fromstring(listSource)

match = tree.xpath('//a[@id="img-5103069422"]/@href')[0]


#print(match)

pageItemPattern = '<a id="img-([0-9]+)" .+>.+<img'

p = re.compile(pageItemPattern)

productIds = p.findall(listSource)

#print(productIds)

a = 0
for i in productIds:
    print(ingredients(i))
    a += 1

    if a % 5 == 0:
        time.sleep(1)
