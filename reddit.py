import requests

resp = requests.get("https://www.reddit.com/r/cryptocurrency/top.json?limit=5&t=all")

print(resp)