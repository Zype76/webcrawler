#!/usr/bin/python3.4
import random
import urllib.request


def download_web_image(url):
    #generate random number to prevent naming conflicts:
    name = random.randrange(1, 1000)
    #append a .jpg onto the random name:
    full_name = str(name) + ".jpg"
    #download image from requested url and give it the random name:
    urllib.request.urlretrieve(url, full_name)

#prompt for a download link: 
dl_link = input("Image Link:")

#run the function created above to download the image from the provided link:
download_web_image(dl_link)
