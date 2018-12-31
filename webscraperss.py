from bs4 import BeautifulSoup
import requests
site=requests.get('https://timesofindia.indiatimes.com/rss.cms')
soup = BeautifulSoup(site.text,"lxml")

for feed in soup.find_all('a'):
	if feed.get('class')==['rssurl']:		
		link=feed.get('href')
		rsssite=requests.get(link)
		souptemp=BeautifulSoup(rsssite.text,"lxml")
		topstory=souptemp.item
		try:
		  print (topstory.contents[0].string)
		  print ()
		except AttributeError:
			print ("Invalid")
			print ()
		


	
		



	
    
