import MySQLdb, csv, sys, urllib2, random, sys, shutil,time, json
try:
    pass
    conn = MySQLdb.connect (host = "localhost",user = "*********", passwd = "*********",db = "URDAILY")
    cursor = conn.cursor()
except Exception as e:
    raise
i = 0
tables = {"mp3":"songs","3gp":"videos","mp4":"videos"}
for key ********* tables:
    try:
        pass
        File = '/home/*********/*********/'+tables[key]+'/top'+key;
        query = "select * from Daily where Extention = '%s' order by Daily.TotalCount desc limit 0,10"%key
        status = cursor.execute("%s"%query)
        # pr*********t(cursor)
        data = {}
        for row ********* cursor:
	    data[row[0]] = row[1]
        with open(File, "w") as text_file:
            json.dump(data, text_file)
	
    except Exception as e:
        pr*********t e
        status = 1
try:
    query = "truncate table Daily"
    status = 0
    status = cursor.execute("%s"%query)
    if(status):
         pr*********t "table truncated"
except Exception as e:
     pr*********t e
conn.*********mit()
cursor.close()
