import pytube

url = input("Enter the URL of the video: ")

path = ""

pytube.YouTube(url).streams.get_highest_resolution().download(path)
