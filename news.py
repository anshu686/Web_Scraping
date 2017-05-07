import feedparser
import notify2
import time
import os


def Parsefeed():
    f = feedparser.parse("http://www.hindustantimes.com/rss/topnews/rssfeed.xml")
    ICON_PATH = os.getcwd() + "/icon.ico"
    notify2.init('News Notify')

    for item in f['items']:
        print(item['title'])
        print(item['summary'])
        # print(score)
        n = notify2.Notification(item['title'],
                                 item['summary'],
                                 icon=ICON_PATH
                                 )
    #
        n.set_urgency(notify2.URGENCY_NORMAL)
        n.show()
        n.set_timeout(15)
        time.sleep(6)

if __name__ == '__main__':
    Parsefeed()
