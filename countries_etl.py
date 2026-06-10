import requests
import psycopg2

# EXTRACT

url = "https://restcountries.com/v3.1/all?fields=name,capital,region,population"

response = requests.get(url)

data = response.json()

# TRANSFORM

transformed_data = []

for country in data:

    capital = "N/A"

    if "capital" in country and len(country["capital"]) > 0:
        capital = country["capital"][0]

    transformed_data.append({
        "country_name": country["name"]["common"],
        "capital": capital,
        "region": country["region"],
        "population": country["population"]
    })

# CHECK DATA

for country in transformed_data[:10]:
    print(country)

print(f"\nTotal Countries: {len(transformed_data)}")

# LOAD

conn = psycopg2.connect(
    host="192.168.1.45",
    database="countries_db",
    user="postgres",
    password="postgres123"
)

cur = conn.cursor()

for country in transformed_data:
    cur.execute("""
        INSERT INTO countries_data
        (country_name, capital, region, population)
        VALUES (%s, %s, %s, %s)
    """, (
        country["country_name"],
        country["capital"],
        country["region"],
        country["population"]
    ))

conn.commit()

print("\nCountries data inserted successfully!")

cur.close()
conn.close()
