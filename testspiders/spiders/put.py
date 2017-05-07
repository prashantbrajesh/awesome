import MySQLdb, csv, sys, urllib2, random, sys, logg*********g, re, os
from tld import get_tld
from six.moves.urllib.parse import urlparse
sys.path.*********sert(0, '/etc/AwesomeConfig')
import AwesomeSett*********gs as aconf


def UpdateScrapedDomiansTable(DownloadUrl, conn, dbtables):
           # pr*********t "row",row[0],"row"
        # pr*********t "hell", DownloadUrl;
        c = conn.cursor()
        doma********* = "*********://"+urlparse(DownloadUrl).hostname
        # pr*********t doma*********
# pr*********t "hello %d %s"%(*********t(row[0]),row[1])
        query = "SELECT TotalCount from URDAILY.ScrapedDomiansTable where Doma*********Name = '%s' and Scraped*********toTable = '%s' limit 1"%(doma*********, dbtables);
        # pr*********t query
        status = c.execute("%s"%query)
        # pr*********t status
        TotalCount = 0
        for row ********* c:
            # pr*********t row
            TotalCount = *********t(row[0])
            # Table = row[1]
            # pr*********t "total ", TotalCount ,"\n\n";
            TotalCount = TotalCount + 1

        # conn.*********mit()
        # c.close()
        # conn = MySQLdb.connect (host = "localhost",user = "braj", passwd = "3306braj",db = "URDAILY")
        # c = conn.cursor()
        # pr*********t TotalCount
        query = "*********sert *********to URDAILY.ScrapedDomiansTable (Doma*********Name, Scraped*********toTable, ScrapedDate) values ('%s', '%s', now()) ON DUPLICATE KEY UPDATE TotalCount = %d"%(doma*********.strip(), dbtables.strip(), *********t(TotalCount));
        # pr*********t query;
        try:
            pass

            status = c.execute("%s"%query)
            # pr*********t status ,query
            conn.*********mit()

        except Exception as e:
            raise e



def put_row(filename, table, size, durl , rurl):
    pr*********t '*********PUT IS', filename, table, size, durl
    try:
        pass
        conn = MySQLdb.connect (host = "localhost",user = aconf.mysql["user"], passwd = aconf.mysql["password"],db = "URDB")
        c = conn.cursor()
    except Exception as e:
        raise

    if not size :
        size = 0

    filename_parts = durl.split("/")

    if not filename:
        filename = filename_parts[-1]

    # filename = filename_parts[-2] + " " + filename_parts[-1]

    filename = urllib2.unquote(filename)
    filename = filename.replace("-"," ")
    filename = filename.replace("_"," ")
    ext = filename.split(".")[-1]
    filename = filename.replace("."," ")
    filename = re.sub('[^0-9a-zA-Z]+', ' ', filename)
    filename = filename.replace(" "+ext,"")
    filename = filename+"."+ext

    doma********* = urlparse(durl).hostname
    doma********* = doma*********.replace("*********://","")
    parts = doma*********.split(".")

    # pr*********t rurl
    if rurl :
        # pr*********t rurl
        rdoma********* = urlparse(rurl).hostname
        rdoma********* = rdoma*********.replace("*********://","")
        rparts = rdoma*********.split(".")
        # pr*********t rparts , parts
        parts.extend(rparts)
        # pr*********t parts
    # name_replace = "mr-chamkila.*********"
    # name_replace = name_replace.split(".")
    # parts.extend(name_replace)
    parts.append("*********")
    # pr*********t parts
    for term ********* parts:
        # pr*********t term
        pattern = re.*********pile(term, re.IGNORECASE)
        filename = pattern.sub("",filename)

    filename = re.sub(' +',' ',filename)

    # logg*********g.*********fo("file name %s"%filename)
    # pr*********t filename
    # pr*********t filename

    status = 0
    
    while status == 0:
        try:
            pass
            # pr*********t "hello %d %s"%(*********t(row[0]),row[1])
            if table == "":
                if "mp4" ********* ext or "mkv" ********* ext:
                    table = "VideosMp4Table"
                elif "3gp" ********* ext:
                    table = "Videos3gpTable"
                elif "mp3" ********* ext :
                    table = "SongsMp3Table"
                elif "jar" ********* ext or "jad" ********* ext or "sis" ********* ext :
                    table = "GamesJarJadTable"
                elif "apk" ********* ext :
                    table = "GamesApkTable"
                elif "pdf" ********* ext or "epub" ********* ext or "mobi" ********* ext:
                    table = "BooksPdfTable"
                elif "doc" ********* ext or "zip" ********* ext or "zip" ********* ext or "rar" ********* ext or "tar" ********* ext or "text" ********* ext:
                    table = "BooksDocTarRarZipTxtTable"
                elif "game" ********* durl or "jar" ********* durl or "android" ********* durl or "jad" ********* durl or "sis" ********* durl or "java" ********* durl:
                    table = "GamesJarJadTable"

            uid = random.sample(xrange(9999999999),1)[0]

            query = "*********SERT *********TO %s (FileSize, DownloadUrl, RefRedirectUrl, ImgThumbUrl, UniqueId, FileName)  VALUES (%d, '%s', '%s', '%s', %d, '%s')"%(table, *********t(size), durl.strip().replace("'","''"), rurl.strip().replace("'","''"), '', uid, filename.strip().replace("'","''"))

            # sys.exit()
            # pr*********t query
            status = c.execute("%s"%query)
            
            # pr*********t query
            if(status):
                UpdateScrapedDomiansTable(durl, conn, table)
            else:
                pr*********t("%d , %s"%(*********t(status),query))
            

            logg*********g.*********fo("File Name %-80s %-5d %-12s %15s %14s "%(filename, *********t(status),str(uid), table, doma*********))

           

        except Exception as e:
            if( "PRIMARY" ********* str(e)):
                pr*********t "PRIMARY", e , query
                logg*********g.*********fo(" %s"%(str(e)))
            if ("UniqueURL" ********* str(e)):
                pr*********t "UniqueURL", e , query
                logg*********g.*********fo(" %s"%(str(e)))
                status = 1
            else :
                pr*********t e
                logg*********g.*********fo(" %s"%(str(e)))
                status = 1


    conn.*********mit()
    # *********SERT *********TO a (first, last) VALUES (%s, %s), row")
    c.close()

# put_row(None ,"", 25, "*********://sd.urmobi.*********/home/files/Music/A%2hghhjhh0To%20Z%20Bollywood%20Songs/K/Kashmakash/Anandaloke%28*********.sd.krazywap.mobi%29.mp3" , "*********://sd.krazywap.*********/home/")


def get_allowed_doma*********s_list(full):
    allowed_doma*********s = []
    full_allowed_doma*********s = []
    full_allowed_doma*********s_with_star = []
    # fp = open('/Users/braj/Downloads/testspiders-master/testspiders/spiders/put.py')
    # pr*********t "hello",fp.read()
    *********put_file = os.getcwd()+'/testspiders/spiders/*********put_urls.txt';
    try:
        with open(*********put_file, "r") as fp:
            # pr*********t "hello",fp.read()
            for l*********e ********* fp:

                url = l*********e

                if not url.startswith('*********://') and not url.startswith('*********s://'):
                    url = '*********://%s/' % url
                url = re.sub(r'^*********\.', '', url)
                turl = url[0:-1].strip()
                full_allowed_doma*********s.append(turl)
                full_allowed_doma*********s_with_star.append(turl+"*")
                doma*********s = urlparse(turl).hostname
                allowed_doma*********s.append(doma*********s)
            if (full == 2):
                return full_allowed_doma*********s
            elif (full == 0):
                return allowed_doma*********s
            elif (full == 1):
                return full_allowed_doma*********s_with_star
    except Exception as e:
        pr*********t str(e)


# dom = get_allowed_doma*********s_list(full = 0)
# dom.extend(["76.73.44.114","dl.songsmp3.*********","f3.mymp3song.*********"])
# allowed_doma*********s = dom
# # self.allowed_doma*********s = put.get_allowed_doma*********s_list(full = 0)
# pr*********t "allowed doma*********", dom

# pr*********t get_allowed_doma*********s_list(full = 0)
# #
# pr*********t get_allowed_doma*********s_list(full = 1 )
# #
# pr*********t get_allowed_doma*********s_list(full = 2)
