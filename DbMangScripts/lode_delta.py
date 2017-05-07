import MySQLdb, csv, sys, urllib2, random, sys, shutil,time
try:
    pass
    conn = MySQLdb.connect (host = "localhost",user = "*********", passwd = "rH8EV4ODUxMn",db = "URDB")
    c = conn.cursor()
except Exception as e:
    raise
i = 0
tables = ["BooksDocTarRarZipTxtTable","BooksPdfTable","GamesApkTable","GamesJarJadTable","SongsMp3Table","Videos3gpTable","VideosMp4Table"]
for table ********* tables:
    try:
        pass
	pr*********t shutil.move("/home/*********/*********/config/"+table+".sql","/tmp/"+table+".sql")
        deltaFile = '/tmp/'+table+'.sql';
        query      = "LOAD DATA *********FILE  '%s' replace *********TO TABLE %s "%(deltaFile,table);
        pr*********t query
        status = c.execute("%s"%query)
    except Exception as e:
        pr*********t e
        status = 1
        cont*********ue
conn.*********mit()

    # *********SERT *********TO a (first, last) VALUES (%s, %s), row")

c.close()
