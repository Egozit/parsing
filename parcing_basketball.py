import urllib
import urllib.request
import os
from bs4 import BeautifulSoup


def make_soup(url):
    the_page = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(the_page, "html.parser")
    return soupdata


playerdatasaved = ""
soup = make_soup("https://www.basketball-reference.com/players/a/")

for record in soup.findAll('tr'):
    playerdata = ""
    playername = ""
    for data in record.findAll('td'):
        playerdata = playerdata + "," + data.text
    playername = playername + record.find('th').text
    playerdatasaved = playerdatasaved + "\n" + playername + "," + playerdata[
                                                                  1:]

playerdatasaved = playerdatasaved[8:]

header = "Player, From, To, Pos, Ht, Wt, Birth, Date, College"
file = open(os.path.expanduser("Basketball.csv"), "wb")
file.write(bytes(header, encoding="ascii", errors='ignore'))
file.write(bytes(playerdatasaved, encoding="UTF-8", errors='ignore'))

print(playerdatasaved)
