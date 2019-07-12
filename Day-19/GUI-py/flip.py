def flip(self):
    path="https://www.flipkart.com/"
    http_response=url.urlopen(path)
    page=bs4.BeautifulSoup(http_response,'lxml')
    name=self.lineEdit.text()
    new_path=path+"search?q="+name
    http_response1=url.urlopen(new_path)
    page1=bs4.BeautifulSoup(http_response1,'lxml')
    data=page1.find('div',class_="_3wU53n")
    a=data.text
    data1=page1.find('div',class_="_1vC4OE _2rQ-NK")
    b=data1.text
    data2=page1.find('ul',class_="vFw0gD")
    c=data2.text
    self.textEdit_2.setText(f"{a}")
    self.lineEdit_2.setText(f"{b}")
    self.textEdit_3.setText(f"{c}")
