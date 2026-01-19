# Lists of cities per country
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

# Ask user for a city
city = input("Enter a city name: ")

# Determine the country
if city in Australia:
    print(f"{city} is in Australia")
elif city in UAE:
    print(f"{city} is in UAE")
elif city in India:
    print(f"{city} is in India")
else:
    print(f"{city} is not in the list")
