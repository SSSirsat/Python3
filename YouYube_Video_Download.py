from pytube import YouTube
yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')
yt.streams.filter(progressive=True, file_extension='mp4')
video = yt.streams.get_lowest_resolution()
video.download()



