#!/usr/bin/python3.4
#Import the required functions
from bs4 import BeautifulSoup
import requests

#Prompt the user for a site to search
url = input("Enter a website to extract the URL's from: ")

#Search the provided site for links
r = requests.get("http://" + url)

#Turn the provided output into plain text
data = r.text

#Create BeautifulSoup object
soup = BeautifulSoup(data)

#Find and print all urls for the page
for link in soup.find_all('a'):
    print(link.get('href'))
