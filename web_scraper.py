import requests
from bs4 import BeautifulSoup
import csv

# URL to scrape – replace with ShadowFox or any website
url = "https://example.com"

try:
    # Step 1: Download the webpage
    response = requests.get(url)
    response.raise_for_status()  # raises an error if request fails

    print("Webpage downloaded successfully!")

    # Step 2: Parse the webpage with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Step 3: Extract page title
    title = soup.title.text
    print("Page Title:", title)

    # Step 4: Extract all links
    links = soup.find_all("a")

    # Step 5: Save links to CSV file
    with open("scraped_data.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Link Text", "URL"])  # CSV header

        for link in links:
            text = link.get_text()
            href = link.get("href")
            writer.writerow([text, href])

    print("All links have been saved to scraped_data.csv")

# Step 6: Error handling
except requests.exceptions.RequestException as e:
    print("Error while downloading the webpage:", e)

except Exception as e:
    print("An error occurred:", e)
