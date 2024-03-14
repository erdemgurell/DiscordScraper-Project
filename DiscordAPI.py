from datetime import time
from urllib.parse import urlparse

import requests
import json

print("Welcome to the Discord data scrapper!")

while True:
    choice = int(input("Enter 1 to enter a channel ID or 2 to enter a message ID (any other input to exit): "))
    if choice == 1:
        channelid = input("Enter a channel ID: ")  # channel ID for scrape
        break
    elif choice == 2:
        messageid = input("Enter a message ID: ")  # message ID for scrape
        break
    else:
        print("Enter a valid choice")
        continue

auth = input("Your auth key: ")  # authorization key
messages = []
headers = {
    "authorization": auth
}


def fetch_messages(before=None):
    url = f"https://discord.com/api/v9/channels/{channelid}/messages"
    params = {"limit": 100}  # Adjust limit for past messages as needed, maximum is 100
    if before:
        params["before"] = messageid
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        if data:
            messages.extend(data)

    else:
        print(f"Error: Failed to fetch messages. Status code: {response.status_code}")


fetch_messages()

# CHECK IF THE MESSAGE CONTAINS ANY ATTACHMENTS (LINK, MEDIA etc.)
for value in messages:
    print(value["content"])
    if "attachments" in value:
        for attachment in value["attachments"]:
            attachment_url = attachment["url"]
#             print(attachment_url)

### FOR DOWNLOADING MEDIA ###

# filename = urlparse(attachment_url).path.split("/")[-1]
# image_response = requests.get(attachment_url)
# if image_response.status_code == 200:
#     # Save the image to a file
#     with open(filename, "wb") as f:
#         f.write(image_response.content)
