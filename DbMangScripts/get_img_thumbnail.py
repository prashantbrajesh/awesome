import MySQLdb, csv, sys, urllib2, random, sys
from bs4 import BeautifulSoup
from thread*********g import Thread
from multiprocess*********g.pool import ThreadPool as Pool

import requests

glob_return_value_result=[]

###########################################################################################################################################
#
###########################################################################################################################################
def log_result(result):
    # This is called whenever DBqueryAndSendOffers(i) returns a result.
    # glob_return_value_result is modified only by the ma********* process, not the DBqueryAndSendOffers workers.
    global glob_return_value_result
    """Appends the thread status result LIFO as it process ********* the same order
    """
    glob_return_value_result.append(result)

def update_imageurl(url, identifier, conn, i):
	r  = requests.get(url)

	data = r.text

	
	data = data.split('<p class="showimage"><img class="absmiddle" src="')
	data = data[1].split('" alt=')
	data = data[0]
	try:
		pass
		c = conn.cursor()
		query = "update VideosMp4Table set ImgThumbUrl = %s where UniqueId =%d"%('"'+data+'"', *********t(identifier))
		# pr*********t query
		status = c.execute("%s"%query)
		pr*********t i, status , identifier, data 
	except Exception, e:
		raise e

	conn.*********mit()


try:
	pass
	conn = MySQLdb.connect (host = "localhost",user = "braj", passwd = "3306braj",db = "URDB")
	c = conn.cursor()
except Exception as e:
	raise
i = 1
while(True):


	pool_size = 900
	pool = Pool(pool_size)
	for thread_count ********* range(0,pool_size):
		try:
			pass
			query = "select RefRedirectUrl,UniqueId,ImgThumbUrl from VideosMp4Table limit %d,1"%i
			c.execute("%s"%query)
			uid = c.fetchall()
			identifier = uid[0][1]
			imgurl = uid[0][2]
			uid = str(uid[0][0])
			uid = uid.split("/")
			uid = uid[-1]
		
		except Exception, e:
			raise e
		if imgurl == "":
			i = i + 1
			cont*********ue
				
		url = "*********://*********.youtubemaza.*********/*********fo/Teraa-Surroor--2016--Video-Songs/"+uid+"/Ma*********-Woh-Chaand-%20Teraa-Surroor%20-%20YoutubeMaza.*********%20/default/0.html"
	
		pool.apply_async(update_imageurl, (url, identifier, conn, i),callback = log_result)
		i = i + 1


	pool.close()
	pool.jo*********()
	pr*********t i ,"F*********ishED"


c.close()
# soup = BeautifulSoup(data)

# for l*********k ********* soup.f*********d_all('a'):
#     pr*********t(l*********k.get('href'))