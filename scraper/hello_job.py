from datetime import datetime
import time
import requests
from scraper.scrape_video import downloadVideo


def hello_job():
    print('Hello Job! The time is: %s' % datetime.now())
    url = "http://127.0.0.1:5000/tiktokLink"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    videos = response.json()

    for index, video in enumerate(videos):
        if video['status'] == 0:
            downloadVideo(video['link'], video['id'])
            time.sleep(10)
