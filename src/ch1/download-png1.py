import urllib.request


url = "http://uta.pw/shodou/img/28/214.png"
savename: str = "test.png"

urllib.request.urlretrieve(url, savename)
print(f"Saved image ${savename}")

