from requests_html import HTMLSession

session = HTMLSession()

r = session.get(r"https://mangamirror.com/manga/23497-passion/chapter-0-prologue-official-translati")

r.html.render()  # this call executes the js in the page
print(r.text)
