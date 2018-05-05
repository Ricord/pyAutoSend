from __future__ import unicode_literals
from threading import Timer

from wxpy import *
import requests

bot = Bot()


def get_news1():
    # get date
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    contents = r.json()['content']
    translation = r.json()['translation']
    return contents, translation


def send_news():
    try:
        # friendName is wx name. not 昵称 or 备注
        my_friend = bot.friends().search(u'friendName')[0]
        my_friend.send(get_news1()[0])
        my_friend.send(get_news1()[1][5:])
        my_friend.send(u"come from i")
        t = Timer(86400, send_news)
        t.start()
    except:
        my_friend = bot.friends().search('')[0]
        my_friend.send(u"message error")


if __name__ == "__main__":
    send_news()
