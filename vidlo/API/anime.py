from requests import session, get, post
from bs4 import BeautifulSoup
import json

# Load hosts from JSON
with open('hosts.json', 'r') as j:
    hosts = json.load(j)

def get_movie(movie):
    instance = session()
    logging.info(f"Sending POST request to {hosts['general'][0]} with data: {{'story': movie}}")
    search = instance.post(hosts['general'][0], data={'story': movie})
    logging.info(f"Response received:\n{search.text}")
