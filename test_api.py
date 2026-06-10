import requests

url = "https://restcountries.com/v3.1/all?fields=name,capital,population,region"

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()

print("Total Countries:", len(data))

print(data[0])
