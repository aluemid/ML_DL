from bs4 import BeautifulSoup
import re


fp = open('../notepad.html', encoding='utf-8')
soup = BeautifulSoup(fp, 'html.parser')

li = soup.find_all(href=re.compile(r"^https://"))
for i in li: print(i.attrs['href'])