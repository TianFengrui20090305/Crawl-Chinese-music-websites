import codecs
from icecream import ic

def save_data(data, audio_name):
    with open(f'{audio_name}', 'wb') as f:
        f.write(data)