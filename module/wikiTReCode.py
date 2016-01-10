import requests
import re


link = 'https://tr.wikipedia.org/wiki/G%C4%B1da_katk%C4%B1lar%C4%B1_listesi'
page = requests.get(link)
content = page.content.decode('utf-8')


chemicalPattern = '''<td>([0-9]+)</td>
<td>A</td>
<td>E</td>
<td><a href=".*?" title=".*?">(.*?)</a>.*?</td>'''

compiled = re.compile(chemicalPattern)

match = compiled.findall(content)

for code, name in match:
    print(code + ' => ' + name)

