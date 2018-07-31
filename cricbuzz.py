from selenium import webdriver
from bs4 import BeautifulSoup
driver = webdriver.PhantomJS(executable_path = r'C:\Users\arbaz\Downloads\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
url=input("enter url of match")
driver.get(url)

html_doc = driver.page_source
soup=BeautifulSoup(html_doc,'lxml')

paragraphtag=soup.find_all("p",{"class":"cb-com-ln ng-binding cb-col cb-col-90"})

comm=[]
for i in paragraphtag:
    comm.append(i.text)

with open ("test.txt","w")as fp:
   for line in comm:
       fp.write(line+"\n")
driver.quit()


"""

just copy and paste the url of match from cricnuzz and change the file name






"""
