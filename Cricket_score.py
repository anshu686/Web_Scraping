from urllib.request import urlopen
from bs4 import BeautifulSoup
import notify2
import os, time, random, re

def Parsefeed():

    while True:

        time.sleep(random.uniform(6, 10))
        f = urlopen("http://www.espncricinfo.com/ci/engine/match/1082636.html?CMP=OTC-RSS")
        ICON_PATH = os.getcwd() + "/icon.ico"
        notify2.init('News Notify')
        time.sleep(random.uniform(6, 10))
        soup = BeautifulSoup(f, 'html.parser')
        # print(soup.prettify())

        j = soup.get_text('class:', 'large-13 medium-13 columns innings-information')

        regex = r".*:"
        
        matches = re.findall(regex, j)[0]
        regex2 = r".*\)"
        title = re.findall(r"\|.*\|", matches)[0]
        score = re.findall(regex2, matches)[0]

        n = notify2.Notification(title,
                                 score,
                                 icon=ICON_PATH
                                 )
        #
        n.set_urgency(notify2.URGENCY_NORMAL)
        n.show()
        n.set_timeout(20)
        time.sleep(10)


if __name__ == '__main__':
    Parsefeed()
