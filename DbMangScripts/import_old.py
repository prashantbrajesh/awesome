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
		query = "update Videos3gpTable set ImgThumbUrl = %s where UniqueId =%d"%('"'+data+'"', *********t(identifier))
		# pr*********t query
		status = c.execute("%s"%query)
		pr*********t i, status , identifier, data 
	except Exception, e:
		raise e

	conn.*********mit()



i = 3
while(i<30622):
	try:
		pass
		conn = MySQLdb.connect (host = "localhost",user = "braj", passwd = "3306braj", db = "mp3")
		c = conn.cursor()
	except Exception as e:
		raise
	try:
		pass
		query = "select * from songs limit %d,1"%i
		c.execute("%s"%query)
		data = c.fetchall()
		# pr*********t data[0][0],data[0][1]
	except Exception, e:
		raise e

	c.close()
	
	try:
		pass
		conn = MySQLdb.connect (host = "localhost",user = "braj", passwd = "3306braj",db = "URDB")
		c = conn.cursor()
	except Exception as e:
		raise

	
	status = 0
	k = 0

	while status == 0:

		try:
			pass
			# pr*********t "hello %d %s"%(*********t(row[0]),row[1])
			
			identity = random.sample(xrange(9999999999),1)[0]


			table = "SongsMp3Table"
			query = "*********SERT *********TO %s (DownloadUrl, RefRedirectUrl, ImgThumbUrl, UniqueId, FileName,*********sertTime)  VALUES ('%s', '%s', '%s', %d, '%s',now())"%(table, data[0][1].strip(), None, None, identity, data[0][0].rstrip())
			pr*********t query
			# sys.exit()
			
			status = c.execute("%s"%query)
			pr*********t status
			
		except Exception as e:
			pr*********t e
			if k > 4:
				break
			k = k+1
			pr*********t k
			
	conn.*********mit()
	# *********SERT *********TO a (first, last) VALUES (%s, %s), row")
	c.close()
	i = i+1





