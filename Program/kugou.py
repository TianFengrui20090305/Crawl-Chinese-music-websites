import requests, json, os, re
from icecream import ic
import save

def get_kugou_info(url, os_path):
    headers_kugou = {
        "user-agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        "referer" : 'https://www.kugou.com/',
        "cookie" : ''
        #填写自己已登录酷狗音乐账号的cookie
    }
    json_data = requests.get(url, headers=headers_kugou).text
    data_json = json.loads(json_data)
    playlink = data_json["data"]["play_url"]
    song_name = data_json["data"]["song_name"]
    author_name = data_json["data"]["author_name"]
    name = song_name + "-" + author_name
    print("将要操作的歌曲=", name)
    if not os.path.exists(os_path + "/kugou/"):
        os.mkdir(os_path + "/kugou/")
    name = os_path + "/kugou/" + name + ".mp3"
    #ic(playlink, type(playlink), name)
    #print("获取到音频URL=", playlink)
    data = requests.get(playlink, headers=headers_kugou).content
    #ic(data, type(data))
    save.save_data(data, name)