"""Hacker News: Top Stories.

Get a list of the top stories (>200 points) on Hacker News.

Example:
    Get the top stories for today.

        $ python topstories.py

"""


import pprint

import requests

from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')

soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.storylink')
links2 = soup2.select('.storylink')

subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2


def sort_stories_by_votes(hnlist):
    """Sort stories by total number of votes."""
    print(f'Today\'s Top {len(hnlist)} Articles:\n')
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    """Create a list of all stories with 200+ points."""
    hn = []
    for idx, _item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
        else:
            points = 0
        if points > 199:
            hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(mega_links, mega_subtext))
