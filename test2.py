import requests

url = "https://tradingeconomics.com/country-list/inflation-rate"

payload = ""
headers = {"cookie": "ASP.NET_SessionId=xcapdmpubdkoqfeq3ucxpw5t; TEServer=TEIIS"}

response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)