import requests

url = r"https://mangamirror.com/manga/23497-passion/chapter-0-prologue-official-translati"

r = requests.get(url)

#print(r.text)
#print(r.text.find(r'<img'))
with open("test.txt", "w+") as html:
    print(r.text)
    html.write(r.text)
