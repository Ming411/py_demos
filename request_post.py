import requests

r = requests.post("http://httpbin.org/post", data={"key": "value"})
r.json()
print(r.text)
