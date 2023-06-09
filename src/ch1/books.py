from bs4 import BeautifulSoup

fp = open('../testing.html', encoding='utf-8')
soup = BeautifulSoup(fp, 'html.parser')

sel = lambda q : print(soup.select_one(q).string)

sel("#nu")
sel("li#nu")
sel("ul > li#nu")
sel("li[id='nu']")
sel("li:nth-of-type(4)")

print(soup.select("li")[3].string)
print(soup.find_all("li")[3].string)
