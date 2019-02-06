import urllib
import urllib2
import requests
from BeautifulSoup import BeautifulSoup

name= raw_input("Enter the Name of MOVIE = ")
name1= name.replace(" ","+")
que= "http://www.google.com/search?q=%s" % name1

page = requests.get(que)
soup = BeautifulSoup(page.content)
links = soup.findAll("a")
getst = ""
for link in links:
    getst= getst+ link["href"]


beg= getst.find("http://www.imdb.com/title")
end = beg + 36
alpha = getst[beg:end]


f= urllib.urlopen(alpha)
dbtxt= f.read()
print "\n DESCRIPTION OF MOVIE \n"
begdes =dbtxt.find('inline canwrap') + 55
enddes =dbtxt.find('Written by') - 30
if len(dbtxt[begdes:enddes])>2000:
    print "The Discription is Not given or it is Much less in size"
else:
    print dbtxt[begdes:enddes]
begdb1= dbtxt.find("strong title")
begdb= begdb1 + 14
enddb = begdb +3
print "\n imdb.com Rating :- ", dbtxt[begdb:enddb]


