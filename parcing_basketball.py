import urllib
import urllib.request
import os
from bs4 import BeautifulSoup
from string import ascii_lowercase


def make_soup(url):
    the_page = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(the_page, "html.parser")
    return soupdata


playerdatasaved = ""
for letter in ascii_lowercase:
    if letter != "x":
        soup = make_soup("https://www.basketball-reference.com/players/" +
                         letter + "/")

        for record in soup.findAll('tr'):
            playerdata = ""
            playername = ""
            for data in record.findAll('td'):
                playerdata = playerdata + "," + data.text
            playername = playername + record.find('th').text
            playerdatasaved = playerdatasaved + "\n" + playername + "," + \
                              playerdata[1:]

        playerdatasaved = playerdatasaved[8:]

        header = "Player, From, To, Pos, Ht, Wt, Birth, Date, College"
        file = open(os.path.expanduser("Basketball.csv"), "wb")
        file.write(bytes(header, encoding="ascii", errors='ignore'))
        file.write(bytes(playerdatasaved, encoding="UTF-8", errors='ignore'))
    else:
        pass
