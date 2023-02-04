import re, os
from icecream import ic
import kugou, qq, netease, migu, kuwo

os_path = os.getcwd() + '/music/'
if not os.path.exists(os_path):
    os.mkdir(os_path)
if __name__ == "__main__":
    url = ""
    geturl = input("输入网址=")
    website = "".join(re.findall('\.(.*?)\.', geturl))
    if website == "":
        website = "".join(re.findall('//(.*?)\.', geturl))
    #ic(website)
    if website == 'kugou':
        url = "https://wwwapi.kugou.com/yy/index.php?r=play/getdata&encode_album_audio_id=" + (re.findall('\.(.*?)\.com/(.*?)/(.*?)\.html', geturl))[0][2]
        kugou.get_kugou_info(url, os_path)
    elif website == 'qq':
        qq.get_qq_info(geturl, os_path)
    elif website == '163':
        pass
    elif website == 'migu':
        pass
    elif website == 'kuwo':
        kuwo.get_kuwo_info(geturl.split('/')[4], os_path)
    else:
        print("你干嘛哎哟~")
    #print("爬取URL=", url)
