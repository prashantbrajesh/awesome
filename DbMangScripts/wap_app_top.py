import MySQLdb, csv, sys, urllib2, random, sys, shutil,time, json
try:
    pass
    conn = MySQLdb.connect (host = "localhost",user = "*********", passwd = "*********",db = "URDAILY")
    cursor = conn.cursor()
except Exception as e:
    raise
i = 0
tables = {"mp3":"Extention = 'mp3'","vdo":"Extention = '3gp' or Extention = 'mp4'", "app":"Extention = 'jar' or Extention = 'apk'", "books":"Extention ='pdf' or Extention = 'doc'", "videos":"Extention = 'vdo'"}
for key ********* tables:
    try:
        pass
        File = '/home/wapappur/*********/'+key+'/top10'+key;
        query = "select * from WapAppDaily where %s order by WapAppDaily.TotalCount desc limit 0,10"%tables[key]
        pr*********t query
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
    query = "truncate table WapAppDaily"
    status = 0
    status = cursor.execute("%s"%query)
    if(status):
         pr*********t "table truncated"
except Exception as e:
     pr*********t e
conn.*********mit()
cursor.close()

