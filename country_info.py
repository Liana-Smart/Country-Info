import requests

country = str(input("Entry Country name:\n"))

url = f"https://api.restcountries.com/countries/v5?q={country}"

headers = {
    "Authorization": "Bearer rc_live_ef58b70f97164d4595199c5e1b9dfc65"
}

response = requests.get(url, headers=headers)

data = response.json()

print(f"Full Name: {data["data"]["objects"][0]["names"]["official"]}")
print(f"{data["data"]["objects"][0]["flag"]["description"]}")
print(f"Region: {data["data"]["objects"][0]["region"]}")
print(f"Sub-Region: {data["data"]["objects"][0]["subregion"]}")
print(f"Area: {data["data"]["objects"][0]["area"]["kilometers"]} sq.km")
print(f"Population: {data["data"]["objects"][0]["population"]}")