from pytube import YouTube, Playlist
from requests import get
from shutil import move



def playlist_extract(playlist_url: str) -> dict:
    playlist = Playlist(playlist_url)
    videos = {}
    for index, video in enumerate(playlist.videos, start=1):
        ## Below are the video attributes 
        #print(f"Title: {video.title}")
        #print(f"Duration: {video.length} seconds")
        #print(f"Author: {video.author}")
        #print(f"Views: {video.views}")
        #print(f"Publish Date: {video.publish_date}")
        #print(f"Description: {video.description}")
        videos.update({index: {'title': video.title, 'url': video.watch_url}})
    return videos


def download_playlist(playlist_url: str, media_type: str, location: str) -> tuple:
    urls = []
    i = 1
    videos = playlist_extract(playlist_url)
    for video in videos:
        print(video)
        download(videos[video]['url'], media_type, location)
        urls.append(videos[video]['url'])
    return tuple(urls)

def download(url: str, media_type: str, location: str) -> dict:
    yt = YouTube(url=url)
    # Attributes
    title = yt.title
    thumbnail = yt.thumbnail_url
    author = yt.author
    publish_date = yt.publish_date
    # Medias
    stream = yt.streams
    if media_type == 'audio':
        audio = stream.get_audio_only()
        audio.download(output_path=location)
        file_location = f'{location}{audio.default_filename}'
        move(file_location, f'{file_location.replace(audio.get_file_path().split(".")[-1], "mp3")}')
    elif media_type == 'hd':
        stream.get_highest_resolution().download(output_path=location)
    elif media_type == 'ld':
        stream.get_lowest_resolution().download(output_path=location)
    elif media_type == 'thumb':
        with open(f'{title}.jpg', 'wb+') as f:
            f.write(get(thumbnail).content)
    else:
        print('Incorrect')

    return {'title': title, 'author': author, 'publish_date': f'{str(publish_date.date().day).zfill(2)}/\
            {str(publish_date.date().month).zfill(2)}/{str(publish_date.date().year)}'}


print(download_playlist('https://www.youtube.com/playlist?list=OLAK5uy_nelG1OguYJ-1CGujrUoPXrn2Gvfc3QfAg', 'audio', '.'))
