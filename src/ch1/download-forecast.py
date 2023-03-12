import urllib.request
import urllib.parse
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

value = {
    'stnId': '109'
}

params = urllib.parse.urlencode(value)
# url: str = f"${API}?${params}"
url = API + "?" + params
print(f"DEBUG: url = ${url}")

data = urllib.request.urlopen(url).read()
text = data.decode('utf-8')
print(text)