from bs4 import BeautifulSoup

fp = open('../testing.html', encoding='utf-8')
soup = BeautifulSoup(fp, 'html.parser')

print(soup)
sel = lambda q : print(soup.select_one(q).string)

sel("li:nth-of-type(8)")
sel("#ve-list > li:nth-of-type(4)")

print(soup.select("#ve-list > li[data-lo='us']")[1].string)
print(soup.select("#ve-list > li.black")[1].string)

cond = {"data-lo": "us", "class": "black"}
print(soup.find("li", cond).string)

print(soup.find(id="ve-list").find("li", cond).string)

