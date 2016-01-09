from lxml import html
import requests

page = requests.get('http://www.traditionaloven.com/articles/122/dangerous-food-additives-to-avoid')
tree = html.fromstring(page.content)
additives = tree.xpath('//td[@class="addi"]/text()')
print additives

