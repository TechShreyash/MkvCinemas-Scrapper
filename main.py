# You must have installed latest version techzapi wrapper on your pc
# pip install -U techzapi

from techzapi.api import TechZApi
import time

API_KEY = "Your API Key"  # Fill Your Api Key Here

scrapper = TechZApi.MkvCinemas(API_KEY)

url = input("Enter url of any movie or series: ")
max = 3  # Max no. of links to scrap

print("\nAdding task to queue...")
data = scrapper.add_task(url, max)
queue = data["queue"]
hash = data["hash"]
print(f"\nAdded task to queue, Queue Position : {queue}")

while True:
    time.sleep(15)
    print("\n", "Checking queue".center(50, "="))
    data = scrapper.get_task(hash)

    if data["status"] == "pending":
        print(f'Status: Pending || Queue Position : {data["queue"]}'.center(50))
        continue

    if data["status"] == "processing":
        print(f'Status : Processing || Links Scrapped : {data["scrapped"]}'.center(50))
        continue

    if data["status"] == "completed":
        print("Task completed...\n")
        print(f'Links: {data["results"]}'.center(50))
        break

    if data["status"] == "failed":
        print("Task failed...")
        break
