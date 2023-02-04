import requests, json, os, re
from icecream import ic
from lxml import etree
import save

def get_kuwo_info(data_id, os_path):
    headers_kuwo = {
        "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        "referer": 'https://www.kuwo.cn/',
        "cookie": ''
        # 填写自己已登录酷我音乐账号的cookie
    }
    data_url = "http://kuwo.cn/api/v1/www/music/playUrl?mid=" + data_id + "&type=music&httpsStatus=1&reqId=b04993a1-a434-11ed-98cc-77bac83a6152"
    json_data = requests.get(data_url, headers=headers_kuwo).text
    data_json = json.loads(json_data)
    #ic(data_json)
    playlink = data_json["data"]["url"]
    #ic(playlink)
    web_url = "http://kuwo.cn/play_detail/" + data_id
    web_data = requests.get(web_url, headers=headers_kuwo).text
    web_str = etree.HTML(web_data)
    song_name = web_str.xpath('//*[@id="__layout"]/div/div[2]/div/div[1]/div[2]/div[1]/p[1]/span/text()')[0]
    song_name = "".join(re.findall('\\n            (.*?)\\n            ', song_name))
    #ic(song_name, type(song_name))
    author_name = "".join(web_str.xpath('//*[@id="__layout"]/div/div[2]/div/div[1]/div[2]/div[1]/p[2]/span/text()'))
    #ic(author_name, type(author_name))
    name = song_name + "-" + author_name
    print("将要操作的歌曲=", name)
    if not os.path.exists(os_path + "/kuwo/"):
        os.mkdir(os_path + "/kuwo/")
    name = os_path + "/kuwo/" + name + ".mp3"
    # ic(playlink, type(playlink), name)
    # print("获取到音频URL=", playlink)
    data = requests.get(playlink, headers=headers_kuwo).content
    # ic(data, type(data))
    save.save_data(data, name)