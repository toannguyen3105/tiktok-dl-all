from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import json


def downloadVideo(link, id):
    cookies = {
        '_ga': 'GA1.2.1019296552.1675676470',
        '__cflb': '02DiuEcwseaiqqyPC5qqJA27ysjsZzMZ7iCGqJN4dP8DZ',
        '_gid': 'GA1.2.1998875232.1676778008',
        '_gat_UA-3524196-6': '1',
    }

    headers = {
        'authority': 'ssstik.io',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_ga=GA1.2.1019296552.1675676470; __cflb=02DiuEcwseaiqqyPC5qqJA27ysjsZzMZ7iCGqJN4dP8DZ; _gid=GA1.2.1998875232.1676778008; _gat_UA-3524196-6=1',
        'hx-current-url': 'https://ssstik.io/en',
        'hx-request': 'true',
        'hx-target': 'target',
        'hx-trigger': '_gcaptcha_pt',
        'origin': 'https://ssstik.io',
        'referer': 'https://ssstik.io/en',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }

    params = {
        'url': 'dl',
    }

    data = {
        'id': 'https://www.tiktok.com/@cedricgrolet/video/7196411593922448646',
        'locale': 'en',
        'tt': 'Z1hnem5l',
    }

    response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)
    downloadSoup = BeautifulSoup(response.text, "html.parser")

    downloadLink = downloadSoup.a["href"]

    mp4File = urlopen(downloadLink)
    with open(f"/home/tony/Documents/Github/tiktok-dl-all/videos/{id}.mp4", "wb") as output:
        while True:
            data = mp4File.read(4096)
            if data:
                output.write(data)

                url = f"http://127.0.0.1:5000/tiktokLink/update-status/{id}"

                payload = json.dumps({
                    "status": 1
                })
                headers = {
                    'Content-Type': 'application/json'
                }

                response = requests.request("PUT", url, headers=headers, data=payload)

                print(response.text)

            else:
                break



