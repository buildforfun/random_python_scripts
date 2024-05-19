import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Enter URL
url = input("URL: ")

# Sends a HTTP GET request to the specified url and returns a Response object
response = requests.get(url)

# Uses BeautifulSoup to parse the HTML into BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")

# Finds all image tags in the HTML
# Image tags have 2 main attributes:
#   src = 'https://path.com/to/file.png'
#   alt='alternative text'
img_tags = soup.find_all("img")

# Makes a folder to store images
os.makedirs("images", exist_ok=True)

# Loops through all the image tags
for img in img_tags:
    # Get's the path to image file
    img_url = img.get("src")
    if img_url:
        # Constructs an absolute URL for the image by joining the
        # base URL of the webpage with the relative path to the image.
        img_url = urljoin(url, img_url)
        # Sends a HTTP GET request to the specified url
        img_response = requests.get(img_url)
        # Ensure the image request was successful
        if img_response.status_code == 200:
            # Creates a file name based on alt attribute of url
            # or generate a unique name by hasing url.
            # This will give a unique identifier for the image filename.
            filename = os.path.join(
                "images",
                img["alt"] if img.get("alt") else f"image_{hash(img_url)}.jpg"
                )
            # Opens the file
            with open(filename, "wb") as f:
                # Writes the content of the image to the file
                f.write(img_response.content)
            print("Image saved: {}".format(filename))
        else:
            print("Failed to download image from {}".format(img_url))
