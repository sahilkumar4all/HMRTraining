import bs4
import urllib.request as url
path = "https://www.indeed.co.in/jobs?q=java&l=New+Delhi%2C+Delhi"
res = url.urlopen(path)
page = bs4.BeautifulSoup(res,'lxml')
div = page.findAll("div",class_="title")
for i in range(len(div)):
    title = div[i].text
    title = title.replace(" ","")
    title = title.replace("\n"," ")
    print(f"{i+1}.{title}")

