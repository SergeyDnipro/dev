import requests

url = "https://www.bikeshop-crm.xyz/service"

response = requests.get(url)

print(response.text)