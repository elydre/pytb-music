import youtube_dl

def start(todo, nom):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'/audio/{nom}.%(ext)s',
            'postprocessors': [
                {
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '320',
                }
            ],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([todo])
        return True
    except:
        return False