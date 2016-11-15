#! $PATH/python3

#import http.client
import urllib.parse
import urllib.request
import sys

def encode(plain):
    encoding_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    i = 0
    cipher = ""
    length = len(plain)
    ltext = plain.encode('utf-8')
    #ltext = plain.encode('ascii')
    while (i< length):
        c1 = ltext[i] & 0xff;
        i += 1
        if (i == length):
            cipher += encoding_table[(c1 >> 2)]
            cipher += encoding_table[((c1 & 0x3) << 4)]
            cipher += "=="
            break
        c2 = ltext[i]
        i += 1
        if (i == length):
            cipher += encoding_table[(c1 >> 2)]
            cipher += encoding_table[(((c1 & 0x3) << 4) | ((c2 & 0xF0) >> 4))]
            cipher += encoding_table[((c2 & 0xF) << 2)]
            break
        c3 = ltext[i]
        i += 1
        cipher += encoding_table[(c1 >> 2)]
        cipher += encoding_table[(((c1 & 0x3) << 4) | ((c2 & 0xF0) >> 4))]
        cipher += encoding_table[(((c2 & 0xF) << 2) | ((c3 & 0xC0) >> 6))]
        cipher += encoding_table[(c3 & 0x3F)]
    return cipher

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
##
data = urllib.parse.urlencode(
{
'username': sys.argv[1],
'password': sys.argv[2],
'pwd': sys.argv[2],
'secret':'true',
'savename':'' })
#en_passwd = encode('pt12345')
#params = urllib.parse.urlencode({'username':'lianghuayue@putian.com','password':en_passwd,
     #'pwd':en_passwd, 'secret':'true', 'savename':'true' })
data = data.encode('ascii')
#data = params.encode('utf-8')
urr = urllib.request.Request("http://10.3.254.233/webAuth/index.htm", data, head)
with urllib.request.urlopen(urr) as f:
    turl = f.geturl()
    tres_hex = turl.split('=')[1]
    thex_ch = tres_hex.replace('%','')
    bstr = bytes.fromhex(thex_ch)
    print(bytes(bstr).decode('utf-8'))
    #print(f.geturl().decode('utf-8'))
    print("done")
    #print(f.read().decode('utf-8'))
#params = urllib.parse.urlencode({'username':'lianghuayue','password':'',
#    'putian':'study',  'secret':'true', 'savename':'' })
#headers = {"Content-Type":"application/x-www-form-urlencode", "Accept":"text/plain"}
#conn = http.client.HTTPConnection("10.3.254.233/webAuth")
#conn = http.client.HTTPConnection("10.3.254.233")
#conn.request("POST", "/webAuth/index.htm", params, headers)
#response = conn.getresponse()
#print(response.status, response.reason)
#data = response.read()
#print(data)
#conn.close()
