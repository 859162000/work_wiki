#! $PATH/python

#import http.client
import urllib
import urllib2
import sys


#head = urllib.urlencode(
head = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip,deflate',
'Accept-Language':'zh-CN',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Content-Length':'84',
'Content-Type':'application/x-www-form-urlencoded',
'Cookie':'auth_name='+sys.argv[1]+'; auth_password='+sys.argv[2]+'; ac_login_info=passwork',
'DNT':'1',
'Host':'10.3.254.233',
'Origin':'http://10.3.254.233',
'Referer':'http://10.3.254.233/webAuth/index.htm',
'User-Agent':'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.9.3.1000 Chrome/39.0.2146.0 Safari/537.36',
'X-DevTools-Emulate-Network-Conditions-Client-Id':'7DA993FC-A05A-4FC9-A693-C1DA47EDABF0'}
#)
data = urllib.urlencode(
{
'username': sys.argv[1],
'password': sys.argv[2],
'pwd': sys.argv[2],
'secret':'true',
'savename':None })
#'password':en_passwd,
#'pwd':en_passwd,
#data = params.encode('ascii')
#data = params.encode('utf-8')
#f= urllib2.urlopen("http://10.3.254.233/webAuth/index.htm", data)
f= urllib2.Request("http://10.3.254.233/webAuth/index.htm", data, head)
f = urllib2.urlopen(f)
turl = f.geturl()
print(urllib2.unquote(turl))
turl = urllib.toBytes(turl)
tres_hex = turl.split('=')[1]
thex_ch = tres_hex.replace('%','\\x')
print(thex_ch.decode('utf-8'))
print("done")
