import requests
import json

def youtube(link):

	url = "https://youtube-media-downloader.p.rapidapi.com/v2/video/details"

	querystring = {"link": link}

	headers = {
		"X-RapidAPI-Key": "e81ff79744msh6d13aeb911b1de6p10294cjsn2a265eac617e",
		"X-RapidAPI-Host": "tiktok-downloader-download-videos-without-watermark1.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)
	result = response.text
	rest = list(json.loads(result)['result']['video']['url_list'])
	qwer = rest[0]
	return {"video": qwer}
