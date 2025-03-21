from downloader import download_video, download_audio

def main():
    url = input("Enter YouTube video URL: ")
    choice = input("Do you want to download (1) Video or (2) Audio? Enter 1 or 2: ")

    if choice == '1':
        resolution = input("Enter video resolution (e.g., 720p, 1080p, best): ")
        download_video(url, resolution)
    elif choice == '2':
        download_audio(url)
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
