from django.shortcuts import render

# Create your views here.

def rss3(request):

	import sys
	import requests
	from bs4 import BeautifulSoup
	feed = Feed.objects.all()
	rsscreater={}

	for f in feed:
		rsscreater[f.name]=f.url

	"""
		rsscreater={'vgsport': 'http://www.vg.no/rss/feed/?categories=1072&keywords=&limit=10&format=rss',
		'vgforside':'http://www.vg.no/rss/feed/forsiden/','Aftenposten':'http://www.aftenposten.no/rss/',
		'itavisen':'http://www.itavisen.no/rss.php','huffington' : 'http://www.huffingtonpost.com/feeds/index.xml',
		 'huffftech': 'http://www.huffingtonpost.com/feeds/verticals/technology/index.xml'
		 ,'huffent':'http://www.huffingtonpost.com/feeds/verticals/entertainment/index.xml',
		 'huffcode':'http://www.huffingtonpost.com/feeds/verticals/huffpost-code/index.xml'
		 ,'huffscience': 'http://www.huffingtonpost.com/feeds/verticals/science/index.xml'}

		 """
	
	mydict={}
	

	for k,v in rsscreater.items():
		links=[]
		titles=[]
		desc=[]
		currentrss=k
		mydict[k]={}
		tempdict=mydict[k]

		myrequest = requests.get(v)
		soup = BeautifulSoup(myrequest.text, 'xml')
		items = soup.find_all('item')
		for item in items:
	        
		    links.append(item.find('link').text.encode("utf-8"))
		    titles.append(item.find('title').text.encode("utf-8"))
		    a=item.find('description').text.encode("utf-8")
		    if(len(a)<200):
		    	desc.append(item.find('description').text.encode("utf-8"))

		    else:
		    	
		    	b=a[0:200]
		    	desc.append(b)


		for i in range(len(items)):
		    tempdict['item' + str(i)]=[links[i],titles[i],desc[i]]

	return render(request, 'rss3.html', {'mydict':mydict})