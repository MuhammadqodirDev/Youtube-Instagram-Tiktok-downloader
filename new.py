# import youtube_dl

# def get_youtube_video_link(url):
#     ydl_opts = {
#         'format': 'bestvideo+bestaudio/best',
#         'outtmpl': '%(id)s.%(ext)s',
#         'postprocessors': [{
#             'key': 'FFmpegVideoConvertor',
#             'preferedformat': 'mp4',
#         }],
#     }

#     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#         try:
#             info = ydl.extract_info(url, download=False)
#             video_url = info['url']
#             return video_url
#         except youtube_dl.DownloadError as e:
#             print(f"Error fetching video URL: {e}")
#             return None

# # Example usage
# youtube_url = "https://www.youtube.com/shorts/MnLfrD4EHLY"
# video_link = get_youtube_video_link(youtube_url)
# print(video_link)



# import requests

# url = "https://auto-download-all-in-one.p.rapidapi.com/v1/social/autolink"

# payload = { "url": "https://www.youtube.com/shorts/MnLfrD4EHLY" }
# headers = {
# 	"content-type": "application/json",
# 	"X-RapidAPI-Key": "f37f5d5d32msha77067df491efdbp1252a1jsn1c1999033af8",
# 	"X-RapidAPI-Host": "auto-download-all-in-one.p.rapidapi.com"
# }

# response = requests.post(url, json=payload, headers=headers)

# print(response.json())



# import requests

# url = "https://youtube-media-downloader.p.rapidapi.com/v2/video/details"

# querystring = {"videoId":"MnLfrD4EHLY"}

# headers = {
# 	"X-RapidAPI-Key": "f37f5d5d32msha77067df491efdbp1252a1jsn1c1999033af8",
# 	"X-RapidAPI-Host": "youtube-media-downloader.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# print(response.json())



# import requests

# url = "https://auto-download-all-in-one.p.rapidapi.com/v1/social/autolink"

# payload = { "url": "https://youtu.be/C-nG6H5DsEI?si=kkB6H2z-C2HrF1Lh" }
# headers = {
# 	"content-type": "application/json",
# 	"X-RapidAPI-Key": "f37f5d5d32msha77067df491efdbp1252a1jsn1c1999033af8",
# 	"X-RapidAPI-Host": "auto-download-all-in-one.p.rapidapi.com"
# }

# response = requests.post(url, json=payload, headers=headers)

# print(response.json())





# {
#    "url":"https://www.tiktok.com/@vantoan___/video/7334406156577770785?is_from_webapp=1&sender_device=pc&web_id=7357304711508952609",
#    "author":"Van",
#    "title":"Just wait for it \\U0001f979❤️ I was playing in a train station when suddenly a young boy asks me to play «\\xa0Another Love\\xa0» but I didn’t expect that he can sing so well \\U0001f979❤️ #piano #singer #publicsinging #publicreaction #anotherlove ",
#    "thumbnail":"https://p16-sign-useast2a.tiktokcdn.com/tos-useast2a-p-0037-euttp/1ed2ad6266144e279e7889376a0f001e_1707674522~c5_300x400.webp?lk3s=d05b14bd&nonce=20501&refresh_token=0f88a7dcb1cdd878f7f7fd97224f7bd0&x-expires=1713092400&x-signature=d7K79xPICTfe2UcDu06Ex9KYAJc%3D&s=AWEME_DETAIL&se=false&sh=&sc=cover&l=202404131118283FF6F8983C4A7818B597",
#    "duration":110334,
#    "medias":[
#       {
#          "url":"https://v77e.tiktokcdn.com/a37a0e2b240196fd919a353c9b2a9312/661abed3/video/tos/useast2a/tos-useast2a-ve-0068c001-euttp/o0eEkReAmhAMKe51gQTj9r8CIrGWSHQLgQ0I1e/?a=1340&bti=OUBzOTg7QGo6OjZAL3AjLTAzYCMxNDNg&ch=0&cr=13&dr=0&lr=all&cd=0%7C0%7C0%7C&cv=1&br=1210&bt=605&cs=2&ds=3&ft=4bEs3MOa8Zmo0~ggu-4jVhp5t_1rKsd.&mime_type=video_mp4&qs=14&rc=M2UzaGdoOmllZjhlOzk0PEBpM280dXE5cm9qcTMzZjczM0AuL18wNi5hX2MxLTNiNC01YSNxaWw0MmRjZDFgLS1kMWNzcw%3D%3D&vvpl=1&l=202404131118283FF6F8983C4A7818B597&btag=e00090000",
#          "quality":"hd_no_watermark",
#          "extension":"mp4",
#          "type":"video"
#       },
#       {
#          "url":"https://v77e.tiktokcdn.com/ab8e75ac548532c0631da2b8443731ab/661abed3/video/tos/useast2a/tos-useast2a-ve-0068c001-euttp/osCAAqIonYAi6iICT9I135fvTQBVhAREaQ6yPJ/?a=1340&bti=OUBzOTg7QGo6OjZAL3AjLTAzYCMxNDNg&ch=0&cr=13&dr=0&lr=all&cd=0%7C0%7C0%7C&cv=1&br=2568&bt=1284&cs=0&ds=6&ft=4bEs3MOa8Zmo0~ggu-4jVhp5t_1rKsd.&mime_type=video_mp4&qs=0&rc=OTRoOGg0NDtkNzZlZTlnN0BpM280dXE5cm9qcTMzZjczM0BiY2IwMDU0NjAxM14wLTFiYSNxaWw0MmRjZDFgLS1kMWNzcw%3D%3D&vvpl=1&l=202404131118283FF6F8983C4A7818B597&btag=e00090000",
#          "quality":"no_watermark",
#          "extension":"mp4",
#          "type":"video"
#       },
#       {
#          "url":"https://v77e.tiktokcdn.com/2022cff3963885879a6c3f80250c1024/661abed3/video/tos/useast2a/tos-useast2a-ve-0068-euttp/o4ICv5QjPia6AAnZAy3qI8oUQiI0fh1BEJC8M4/?a=1340&bti=OUBzOTg7QGo6OjZAL3AjLTAzYCMxNDNg&ch=0&cr=13&dr=0&lr=all&cd=0%7C0%7C0%7C&cv=1&br=3028&bt=1514&cs=0&ds=3&ft=4bEs3MOa8Zmo0~ggu-4jVhp5t_1rKsd.&mime_type=video_mp4&qs=0&rc=aGhoOjhoOmg6ZDQ2ZGVlNEBpM280dXE5cm9qcTMzZjczM0AvL2NiX2BhX2IxNmE2MDFeYSNxaWw0MmRjZDFgLS1kMWNzcw%3D%3D&vvpl=1&l=202404131118283FF6F8983C4A7818B597&btag=e00090000",
#          "quality":"watermark",
#          "extension":"mp4",
#          "type":"video"
#       },
#       {
#          "url":"https://sf16-ies-music.tiktokcdn.com/obj/ies-music-euttp/7334406225441819425.mp3",
#          "duration":110,
#          "quality":"audio",
#          "extension":"mp3",
#          "type":"audio"
#       }
#    ],
#    "error":false
# }







# import requests

# url = "https://youtube-media-downloader.p.rapidapi.com/v2/video/details"

# querystring = {"videoId":"C-nG6H5DsEI"}

# headers = {
# 	"X-RapidAPI-Key": "f37f5d5d32msha77067df491efdbp1252a1jsn1c1999033af8",
# 	"X-RapidAPI-Host": "youtube-media-downloader.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# print(response.json())


# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context


# from pytube import YouTube
# url = "https://www.youtube.com/shorts/X9wh8EaGcY4"
# yt1 = YouTube(url)


# for stream in yt1.streams:
#     print(stream)




import requests

url = "https://youtube-media-downloader.p.rapidapi.com/v2/video/details"

querystring = {"videoId":"WNCl-69POro"}

headers = {
	"X-RapidAPI-Key": "e81ff79744msh6d13aeb911b1de6p10294cjsn2a265eac617e",
	"X-RapidAPI-Host": "youtube-media-downloader.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())