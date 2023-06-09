from bs4 import BeautifulSoup

html = """
<html><body>
    <ul>
        <li><a href="https://www.naver.com/">Naver</a></li>
        <li><a href="https://www.google.com/">Google</a></li>
    </ul>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all("a")

for a in links:
    href = a.attrs['href']
    text = a.string
    print(f"{text} > {href}")


