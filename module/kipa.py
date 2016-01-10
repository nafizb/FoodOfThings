import time
import math
import requests
import re
from module.kipaContent import ingredients

baseUrl = "http://kapimda.kipa.com.tr/tr-TR/"

catUrl = "Product/BrowseProducts?taxonomyID=Cat00000336&pageNo=1&sortBy=Default"

targetUrl = baseUrl + catUrl

listSource = requests.get(targetUrl).content.decode("utf-8")

pageCountPattern = '<span>1&nbsp;-&nbsp;24&nbsp;/&nbsp;([0-9]+)&nbsp;</span>gösteriliyor'

p = re.compile(pageCountPattern)
productCount = p.findall(listSource)[0]
pageCount = math.ceil(int(productCount) / 24)

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
