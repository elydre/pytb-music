import requests

recherche = "clara luciani allo"

page = requests.get('https://www.youtube.com/results?search_query=' + recherche).text

class video:
    def __init__(self, title, link, views, date, channel, duration, image):
        self.title = title
        self.link = link
        self.views = views
        self.date = date
        self.channel = channel
        self.duration = duration
        self.image = image

def ftry(e, debut, id1, fin, id2 = 0):
    try:
        return e.split(debut)[id1].split(fin)[id2]
    except:
        return "?"


def get_info(e):
    title = ftry(e, '"}],"accessibility":{"accessibilityData":{"label":"', 0, ',"title":{"runs":[{"text":"', 1)
    image = ftry(e, '","thumbnail":{"thumbnails":[{"url":"', 1, '","width":').split('?')[0]
    link = 'https://www.youtube.com' + ftry(e, '{"webCommandMetadata":{"url":"', 2, '","')
    views = ftry(e, '"viewCountText":{"simpleText":"', 1, '"')
    date = ftry(e, '"publishedTimeText":{"simpleText":"', 1, '"')
    channel = ftry(e, '"longBylineText":{"runs":[{"text":"', 1, '"')
    duration = ftry(e, ',"simpleText":"', 1, '"')
    return video(title, link, views, date, channel, duration, image)

videos = [
    get_info(e)
    for e in page.split(',{"videoRenderer":{"videoId":"')[1:]
    if '}],"accessibility":{"accessibilityData":{"label":"' in e
]

for video in videos:
    print(video.title)
    print(video.link)
    print(video.views)
    print(video.date)
    print(video.channel)
    print(video.duration)
    print(video.image)
    print("\n")