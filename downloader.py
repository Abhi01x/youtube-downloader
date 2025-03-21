from pytube import YouTube

def download_video(url, resolution="best"):
    try:
        yt = YouTube(url)
        if resolution == "best":
            stream = yt.streams.get_highest_resolution()
        else:
            stream = yt.streams.filter(res=resolution, progressive=True).first()

        if stream:
            print(f"Downloading {yt.title} in {resolution} resolution...")
            stream.download()
            print("Download complete!")
        else:
            print("Resolution not available. Try another resolution.")
    except Exception as e:
        print(f"Error: {e}")

def download_audio(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        
        if stream:
            print(f"Downloading audio from {yt.title}...")
            stream.download(filename=yt.title + ".mp3")
            print("Audio download complete!")
        else:
            print("No audio stream available.")
    except Exception as e:
        print(f"Error: {e}")
