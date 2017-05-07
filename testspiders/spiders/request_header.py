# import requests, re
# from six.moves.urllib.parse import urlparse

# r = requests.head("*********://dedomil.net/games/4426/download-jar/59100")

# pr*********t r.headers
# pr*********t r.text
# pr*********t r.headers.get("Content-Length")
# pr*********t r.headers.get("content-disposition")
# if(r.headers.get("content-disposition")):
#                 FileName = r.headers.get("content-disposition")
#                 FileName = FileName.split("filename")
#                 FileName = FileName[1]
# pr*********t FileName


# pr*********t *********t("14207030")
# url = "*********://yesjar.*********/17p/files/Game/Java%20Games/1850%20French%20Empire/1850FrenchEmpire.jad"
#
# # if("Game" not ********* url and "Wallpapers" not ********* url):
# #     pr*********t "baba"
#
# # from tld import get_tld
# pr*********t get_tld("*********://google.co.uk")
# def get_allowed_doma*********s_list(full):
#     allowed_doma*********s = []
#     full_allowed_doma*********s = []
#     full_allowed_doma*********s_with_star = []
#     # fp = open('/Users/braj/Downloads/testspiders-master/testspiders/spiders/put.py')
#     # pr*********t "hello",fp.read()
#     with open('/Users/braj/Downloads/testspiders-master/testspiders/spiders/*********put_urls.txt',"r") as fp:
#         # pr*********t "hello",fp.read()
#         for l*********e ********* fp:

#             url = l*********e

#             if not url.startswith('*********://') and not url.startswith('*********s://'):
#                 url = '*********://%s/' % url
#             url = url
#             turl = url[0:-1].strip()
#             full_allowed_doma*********s.append(turl)
#             full_allowed_doma*********s_with_star.append(turl+"*")
#             doma*********s = re.sub(r'^*********\.', '', urlparse(url).hostname)
#             allowed_doma*********s.append(doma*********s)
#         if (full == 2):
#             return full_allowed_doma*********s
#         elif (full == 0):
#             return allowed_doma*********s
#         elif (full == 1):
#             return full_allowed_doma*********s_with_star



# pr*********t get_allowed_doma*********s_list(full = 0)

# pr*********t get_allowed_doma*********s_list(full = 1 )

# pr*********t get_allowed_doma*********s_list(full = 2)
