import requests
import json

def tk_ins(link):
    url = "https://auto-download-all-in-one.p.rapidapi.com/v1/social/autolink"

    payload = { "url": link}
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "f37f5d5d32msha77067df491efdbp1252a1jsn1c1999033af8",
        "X-RapidAPI-Host": "auto-download-all-in-one.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)


    if response.status_code == 200:
        try:
            data = response.json()
            # Access the 'medias' key from the response
            medias = data.get('medias', [])
            data = []

            for i in medias:
                dt = {
                    'quality': i['quality'],
                    'url': i['url'],
                    'extension': i['extension'],
                    'type': i['type'],
                }

                if not dt in data:
                    data.append(dt)
                
            return {
                "datas": data
            }
        except json.JSONDecodeError:
            print("Failed to decode JSON response.")
            return None
    else:
        print(f"Failed to get response. Status code: {response.status_code}")
        return None





from pytube import YouTube
import re

def get_youtube_video_id(url: str):
    pattern = r'(?:https?://)?(?:www\.)?(?:youtube\.com|youtu\.be)/watch\?v=([\w-]{11})'
    
    match = re.search(pattern, url)
    
    if match:
        return match.group(1)
    elif url.startswith('https://www.youtube.com/shorts/'):
        return url.replace('https://www.youtube.com/shorts/', '')
    elif url.startswith('https://www.youtube.com/watch?v'):
        return url.replace('https://www.youtube.com/watch?v=', '')
    
    elif url.startswith('https://m.youtube.com/watch?v='):
        return url.replace('https://m.youtube.com/watch?v=', '')
    elif url.startswith('https://m.youtube.com/shorts/'):
        return url.replace('https://m.youtube.com/shorts/', '')
    
    elif re.search(r"youtu\.be/([^/?]+)", url):
        return re.search(r"youtu\.be/([^/?]+)", url).group(1)
    else:
        print('eeee')
        # Try to extract video ID from YouTube object
        try:
            yt = YouTube(url)
            # print(yt.strams)
            return yt.video_id
        except Exception as e:
            print(f"Error extracting video ID: {e}")
            return None


def yt(link):
    url = "https://youtube-media-downloader.p.rapidapi.com/v2/video/details"

    id = get_youtube_video_id(link)

    if not id:
        return None
    querystring = {"videoId": id}

    headers = {
        "X-RapidAPI-Key": "e81ff79744msh6d13aeb911b1de6p10294cjsn2a265eac617e",
        "X-RapidAPI-Host": "youtube-media-downloader.p.rapidapi.com"
    }


    response = requests.get(url, headers=headers, params=querystring)


    if response.status_code == 200:
        try:
            data = response.json()
            # Access the 'medias' key from the response
            medias = data['videos'].get('items', [])
            data = []

            for i in medias:
                if i['extension'] == 'mp4' and i['hasAudio'] == True:
                    dt = {
                        'quality': i['quality'],
                        'url': i['url'],
                        'extension': i['extension'],
                        'sizeText': i['sizeText'],
                    }

                if not dt in data:
                    data.append(dt)
            
                
            return {
                "datas": data
            }
        except json.JSONDecodeError:
            print("Failed to decode JSON response.")
            return None
    else:
        print(f"Failed to get response. Status code: {response.status_code}")
        return None


# print(youtube('https://www.youtube.com/shorts/X9wh8EaGcY4'))


# youtube_url = "https://www.youtube.com/shorts/X9wh8EaGcY4"  # Rick Astley - Never Gonna Give You Up
# video_id = get_youtube_video_id(youtube_url)
# print(f"YouTube Video ID: {video_id}")


