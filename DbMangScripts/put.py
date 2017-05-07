import MySQLdb, csv, sys, urllib2, random, sys


def put_row(size, durl , rurl):
    try:
        pass
        conn = MySQLdb.connect (host = "localhost",user = "braj", passwd = "3306braj",db = "URDB")
        c = conn.cursor()
    except Exception as e:
        raise


    filename = durl.split("/")[-1]
    filename = urllib2.unquote(filename).replace("(YoutubeMaza.*********)","")
    # filename = filename.replace("(youtubemaza.*********)","")
    # filename = filename.replace("(Youtubemaza.*********)","")
    pr*********t filename
    # logg*********g.getLogger("DoorcamLog")
    status = 0
    while status == 0:
        try:
            pass
            # pr*********t "hello %d %s"%(*********t(row[0]),row[1])
            if "mp4" ********* filename:
                table = "VideosMp4Table"
            elif "3gp" ********* filename:
                table = "Videos3gpTable"
            elif "mp3" ********* filename :
                table = "SongsMp3Table"

            uid = random.sample(xrange(9999999999),1)[0]

            query = "*********SERT *********TO %s (FileSize, DownloadUrl, RefRedirectUrl, ImgThumbUrl, UniqueId, FileName)  VALUES (%d, '%s', '%s', '%s', %d, '%s')"%(table, *********t(size), durl.strip().replace("'","''"), rurl.strip().replace("'","''"), '', uid, filename.rstrip().replace("'","''"))
            pr*********t query
            # sys.exit()
            status = c.execute("%s"%query)
            pr*********t status, query
        except Exception as e:
            if( "PRIMARY" ********* str(e)):
                pr*********t e
            if ("UniqueURL" ********* str(e)):
                pr*********t e
                status = 1
            else :
                pr*********t e
                status = 1


    conn.*********mit()
    # *********SERT *********TO a (first, last) VALUES (%s, %s), row")
    c.close()

put_row(25, "*********://h*********dimasti.net/bollywood/files/New%202015/Wel*********e%20Back/Damaa%20Dam%20Mast%20Kalandar.mp3" , "None")
