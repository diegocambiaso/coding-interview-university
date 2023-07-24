from pytube import Playlist, YouTube

playlist_url = 'https://www.youtube.com/watch?v=eaMuE8N9AfY'
p = Playlist(playlist_url)
for url in p.video_urls:
    try:
        yt = YouTube(url)
    except VideoUnavailable:
       print(f'Video {url} is unavaialable, skipping.')
    else:
        print(f'Downloading video: {url}')
        yt.streams.first().download()
