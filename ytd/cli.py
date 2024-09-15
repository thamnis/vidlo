import argparse
from functions.yt import download
from typing import Union

parser = argparse.ArgumentParser(description='YT downloader')

parser.add_argument('--type', type=str, help='Download argument')
parser.add_argument('--url', type=str, help='YT video url')
parser.add_argument('--location', type=str, help='The desired location to save the file')

args = parser.parse_args()
if ',' in args.url:
    print('list')
    for url in str(args.url).split(','):
        print(url)
        print(download(url=url, media_type=args.type, location=args.location))
else:
    print('str')
    print(download(url=args.url, media_type=args.type, location=args.location))

print('Downloaded')
