from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

#Print basic video information
print("Title:", yt.title)
print("Views:", yt.views)
print("Rating:", yt.rating)
print("Youtuber", yt.author)

#Create a variable and assign it to download 
#Download video into specified folder by inputting filepath of the folder
dl_video = yt.streams.get_highest_resolution()
dl_video.download('/Users/Steve/Projects/100DaysofDS/P-Yt/ytvdowloader/youtube\\\ downloads')