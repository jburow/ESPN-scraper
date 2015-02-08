__author__ = 'Justin'
import requests
from bs4 import BeautifulSoup

r = requests.get("http://scores.espn.go.com/nba/scoreboard")

html_doc = r.text

soup = BeautifulSoup(html_doc)

# print(soup.prettify())
status = soup.find_all("div", "game-status")  # finds status of game or time of game start

homeTeam = soup.find_all("div", "team home")  # homeTeam - finds all divs with class id 'team home'

awayTeam = soup.find_all("div", "team away")  # awayTeam - finds all divs with class id 'team away'

print "Home Teams:"
for team in homeTeam:
    print team.contents[2].find_all("p", "team-name")[0].text  # finds all home teams

print

print "Away Teams:"
for team in awayTeam:
    print team.contents[2].find_all("p", "team-name")[0].text  # finds all away teams

print

print"Status:"
for i in status:
    print i.text
