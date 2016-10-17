#! $PATH/python3

#import http.client
import urllib.parse
import urllib.request

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

##
en_passwd = encode('pt12345')
params = urllib.parse.urlencode({'username':'lianghuayue@putian.com','password':en_passwd,
     'pwd':en_passwd, 'secret':'true', 'savename':'true' })
#data = params.encode('ascii')
data = params.encode('utf-8')
with urllib.request.urlopen("http://10.3.254.233/webAuth/index.htm", data) as f:
#with urllib.request.urlopen("http://10.3.19.232/net_verify.html", data) as f:
#with urllib.request.urlopen("http://10.3.19.232:9901", data) as f:
    print(dir(f))
    #turl = f.geturl()
    #tres_hex = turl.split('=')[1]
    #thex_ch = tres_hex.replace('%','')
    #bstr = bytes.fromhex(thex_ch)
    #print(bytes(bstr).decode('utf-8'))
    #print(f.geturl().decode('utf-8'))
    #print("done")
    print(f.read().decode('utf-8'))
#params = urllib.parse.urlencode({'username':'lianghuayue','password':'pt12345',
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
