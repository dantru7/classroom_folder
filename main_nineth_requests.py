import requests

param = {"id": "5"}
proxy = {'http': 'http://UserVPN:UserVPN@192.168.17.1:8080/', 'https': 'http://UserVPN:UserVPN@192.168.17.1:8080/'}
a = requests.get("http://192.168.16.114:5000/api/task?id=5")#, proxies=proxy) #, params=param
print(a.text)
