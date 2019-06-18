import bs4
import urllib.request as url

path = "https://www.imdb.com/"
http_response = url.urlopen(path)

webpage = bs4.BeautifulSoup(http_response,'lxml')
newpath = path+"find?ref_=nv_sr_fn&q="

movie_name = input("Enter Movie Name")

newpath1 = newpath+movie_name
http_response = url.urlopen(newpath1)
webpage1 = bs4.BeautifulSoup(http_response,'lxml')
td = webpage1.find('td',class_='result_text') 
href = td.find('a')['href']

newpath2 = path+href
http_response3 = url.urlopen(newpath2)
webpage2 = bs4.BeautifulSoup(http_response3,'lxml')
div = webpage2.find('div',class_='title_wrapper')
h1 = div.find('h1')
print(h1.text)







 
