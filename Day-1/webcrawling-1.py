import bs4
import urllib.request as url

path ="https://www.flipkart.com/"
http_response = url.urlopen(path)
page = bs4.BeautifulSoup(http_response)
data = page.find('div',class_="iUmrbN")
print(data.text)
data = page.find('div',class_="BXlZdc")
print(data.text)

