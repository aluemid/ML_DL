from bs4 import BeautifulSoup


html: str = """
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
<div id="meigan">
    <h1>위키북스 도서</h1>
    <ul class="items">
        <li>유니티 게임 이팩트 입문</li>
        <li>스위프트로 시작하는 아이폰 앱 개발 교과서</li>
        <li>모던 웹사이트 디자인의 정석</li>
    </ul>
</div>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

h1 = soup.select_one("div#meigan > h1").string
print(f"h1 = {h1}")

li_list = soup.select("div#meigan > ul.items > li")
for a in li_list:
    print(f"li = {a.string}")

