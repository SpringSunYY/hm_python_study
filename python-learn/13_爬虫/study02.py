import re

import requests
url = "https://www.gdust.edu.cn"
response= requests.get(url)
response.encoding="utf-8"
html= response.text
text_data=re.findall(r"<p>(.*?)</p>",html,re.S)
for text in text_data:
    print(text)
print(text_data[0])

text_data=re.findall(r"<img .*?src='(.*?)'",html)
for text in text_data:
    print(text)
response.close()
