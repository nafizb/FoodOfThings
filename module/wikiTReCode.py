import requests
import re
import json

link = 'https://tr.wikipedia.org/wiki/G%C4%B1da_katk%C4%B1lar%C4%B1_listesi'
page = requests.get(link)
content = page.content.decode('utf-8')


chemicalPattern = '''<td>([0-9]+)</td>
<td>A</td>
<td>E</td>
<td><a href=".*?" title=".*?">(.*?)</a>.*?</td>'''

compiled = re.compile(chemicalPattern)

match = compiled.findall(content)

data = {}


for code, name in match:
    data[name] = code
    #print(code + ' => ' + name)


with open('wikitrecode.txt', 'w') as f:
    json.dump(data, f, ensure_ascii=False)


