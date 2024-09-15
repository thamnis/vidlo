"""
@info: Exploited vulnerability : sbnet video reader
"""

import logging
from API.torrent import search_torrent, get_torrent

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.StreamHandler(),
                              logging.FileHandler('vidlo.log', mode='w')])

search_torrent('Interstellar')
