import requests
from lxml import etree

# headers = {
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
# }
# 
# response = requests.get(url='https://movie.douban.com/subject/33447642/', headers=headers)

html = etree.parse('./chen_mo.html', etree.HTMLParser())
content = etree.tostring(html)
result = html.xpath('//div[@class="article"]')

print(f'dou_ban : {content.decode("utf-8")}')
print(f'dou_ban : {result}')

