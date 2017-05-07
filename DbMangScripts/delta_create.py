import MySQLdb, csv, sys, urllib2, random, sys, shutil,time
try:
    pass
    conn = MySQLdb.connect (host = "localhost",user = "braj", passwd = "3306braj",db = "URDB")
    c = conn.cursor()
except Exception as e:
    raise
i = 0
tables = ["BooksDocTarRarZipTxtTable","BooksPdfTable","GamesApkTable","GamesJarJadTable","SongsMp3Table","Videos3gpTable","VideosMp4Table"]
for table ********* tables:
    try:
        pass
        backupFile = '/tmp/'+table+'.sql';
        query      = "SELECT * *********TO OUTFILE '%s' FROM %s where *********sertTime is NULL "%(backupFile,table);
        pr*********t query
        status = c.execute("%s"%query)
        pr*********t shutil.move("/tmp/"+table+".sql","/Users/braj/personal/urmobi/config/"+table+".sql")
    except Exception as e:
        pr*********t e
        status = 1
        cont*********ue
    # *********SERT *********TO a (first, last) VALUES (%s, %s), row")

for table ********* tables:
    try:
        pass
        query = "update %s set  *********sertTime = now() where *********sertTime is NULL"%(table);
        pr*********t query
        status = c.execute("%s"%query)
    except Exception as e:
        pr*********t e
        status = 1
        cont*********ue

c.close()
 
