import logging
from requests import session, get, post
from bs4 import BeautifulSoup
import json

# Configure logging
'''logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.StreamHandler(),
                              logging.FileHandler('vidlo.log', mode='w')])
'''

with open('hosts.json', 'r') as j:
    hosts = json.load(j)


def search_torrent(torrent: str) -> dict:
    # logging.info(f"Sending POST request to {hosts['torrent'][0]}/recherche/{torrent}")
    search = post(f"{hosts['torrent'][0]}/recherche/{torrent}")
    # logging.info(f"Response received:\nURL: {search.url}\nResponse object: {search}")

    soup = BeautifulSoup(search.content, 'html.parser')
    movies_table = soup.find_all('td')
    movies = {}
    i = 1
    for movie in movies_table:
        title = movie.text.split('\n')[0].lstrip()
        size = movie.find('div', {'class': 'poid'}).text.lstrip()
        seed = movie.find('div', {'class': 'up'}).text.lstrip()
        leech = movie.find('div', {'class': 'down'}).text.lstrip()
        link = movie.find('a', {'class': 'titre'})['href'].lstrip()
        movies.update({i: {'title': title, 'size': size, 'seed': seed, 'leech': leech, 'link': hosts['torrent'][0]+link}})
        i += 1
    '''
    logging.info('Movies found:')
    for movie in movies:
        logging.info(f"{str(movie).zfill(2)}. {movies[movie]['title']} : leech({movies[movie]['leech']}), seed({movies[movie]['seed']})")
    '''
    return movies   


    def get_torrent(n: int) -> int:
    # Process user choice
        if int(n) > 0 and int(n) < (len(movies)+1):
            r = movies[int(n)]['link']
            # logging.info(f"Fetching details from {r}")
            final_page = get(r)
            # logging.info(f"Final page fetched:\n{final_page}")

            soup = BeautifulSoup(final_page.content, 'html.parser')
            dl = soup.find('div', {'class', 'btn-download'}).find('a')['href']
            torrent_link = hosts['torrent'][0] + '/' + dl
            # logging.info(f"Downloading torrent from: {torrent_link}")

            # Downloading torrent file
            with open(f"{movies[int(choose)]['title']}.torrent", 'wb') as f:
                f.write(get(torrent_link).content)
            # logging.info(f"Torrent downloaded successfully.")
            return 0
        return 1
        # logging.error(f"Invalid input: {n}. Please enter a valid input (int between 1 and {len(movies)}).")
