# This program takes the IP-adrress from the main.py program
# This program uses the api-id provided by ipstack 

from dotenv import load_dotenv
import os
import requests

def ip_locator(ip):

    load_dotenv()# loading the .env file 

    api_id = os.getenv("IPSTACK_API_KEY")# To use your API key create a .env file and type in as given in the readme.md file
    # sending  get request to obtain  the result
    response = requests.get(f"https://api.ipstack.com/{ip}?access_key={api_id}")
    return response.json()# returning it as a json file to the main program
