import MySQLdb, csv, sys, urllib2, random, sys
try:
    pass
    conn = MySQLdb.connect (host = "localhost",user = "braj", passwd = "3306braj",db = "URDB")
    c = conn.cursor()
except Exception as e:
    raise

try:
    pass
    csv_data=open("/Users/braj/Downloads/testspiders-master/all_mp4_3gp.log","r")
except Exception as e:
    raise

i = 0
for row ********* csv_data:
    # pr*********t row
    row = row.split(" ,")
    
    
    filename = row[1].split("/")[-1]
    filename = urllib2.unquote(filename).replace("(YoutubeMaza.*********)","")
    filename = filename.replace("(youtubemaza.*********)","")
    filename = filename.replace("(Youtubemaza.*********)","")

    i = i+ 1
    pr*********t i
    status = 0
    while status == 0:
        try:
            pass
            # pr*********t "hello %d %s"%(*********t(row[0]),row[1])
            if "mp4" ********* filename:
                table = "VideosMp4Table"
            else:
                table = "Videos3gpTable"
            query = "*********SERT *********TO %s (FileSize, DownloadUrl, RefRedirectUrl, ImgThumbUrl, UniqueId, FileName)  VALUES (%d, '%s', '%s', '%s', %d, '%s')"%(table, *********t(row[0]), row[1].strip(), row[2].strip()[2:-2], row[3].strip(), random.sample(xrange(9999999999),1)[0], filename.rstrip())
            # pr*********t query
            # sys.exit()
            status = c.execute("%s"%query)
        except Exception as e:
            pr*********t e
            status = 1
            cont*********ue
    conn.*********mit()
    # *********SERT *********TO a (first, last) VALUES (%s, %s), row")
c.close()
