import os
import json
import logging
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler("NetEase.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

def run():
    music_u = ""
    s = requests.Session()
    s.cookies.set("MUSIC_U", music_u, domain=".music.163.com")
    r = s.get("https://music.163.com/discover/toplist", headers=headers)
    html = BeautifulSoup(r.text, "html.parser")
    songs = json.loads(html.find(id="song-list-pre-data").text)
    assert len(songs), "Failed to obtain toplist!"
    r = s.post("https://music.163.com/weapi/login/token/refresh")
    print(r.status_code)
    if (r.status_code==200 and len(songs)>=90):
        logging.info("Attempt success!")
    else:
        logging.error("Attempt failed!")
if __name__ == "__main__":
    run()