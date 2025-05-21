# This program takes the phone number from the main.py program
# This program uses the api-id provided by numverify 

from dotenv import load_dotenv
import os
import requests

def num_locator(num):

    load_dotenv()# loading the .env file

    api_id = os.getenv("NUMVERIFY_API_KEY")# To use your API key create a .env file and type in as given in the readme.md file
    #sending a get request to obtain the result
    response = requests.get(f"https://apilayer.net/api/validate?access_key={api_id}&number={num}")
    return response.json()# returning it as json file to the main.py program
