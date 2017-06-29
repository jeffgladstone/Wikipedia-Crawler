
"""
    Filename: wiki_crawler.py
    Author: Jeff Gladstone
    Date: 6/29/2017
    Description:
    This program consists of two Web crawling games 
    that scrape links by parsing HTML from Wikipedia pages. 
    The first game allows the user to travel down a path 
    of links for a predetermined number of steps.
    The second game allows the user to travel 
    endlessly down a path of links.
"""


# Initial imports
from lxml import html
import requests
from random import randint

# This is a function that, given a URL for a Wikipedia page, scrapes the page and returns a list of links from the body of the page
def get_links(seed_url):
	links = list()
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
	page = requests.get('https://en.wikipedia.org' + seed_url, headers=headers)
	tree = html.fromstring(page.content)

	# Parse HTML
	links = tree.xpath('//div[@id="bodyContent"]//a/@href')
	links = list(filter(lambda k: '/wiki/' in k, links))
	links = list(filter(lambda k: '.' not in k, links))
	links = list(filter(lambda k: ':' not in k, links))
	links = list(filter(lambda k: 'ISO/' not in k, links))
	return links

# Inputs a wiki url and returns a random link from the page
def get_random_link(seed_url):
	new_links = get_links(seed_url)
	index = randint(0, len(new_links) - 1)
	print('link #' + str(index))
	return new_links[index]

# Special printing for Game One
def print_path(seed_url, k):
	print(seed_url)
	if k > 0:
		random_link = get_random_link(seed_url)
		print()
		print_path(random_link, k - 1)

# Game One: Travel down a path of links for a predetermined number of steps
def game1(seed_url, k):
	while(True):
		print_path(seed_url, k)
		print()
		question = input('Play again?')

# Game Two: Travel endlessly down a path of links
def game2(seed_url):
	counter = 0
	while(True):
		print(seed_url + '     [' + str(counter) + ']')
		print()
		question = input('Keep going?')
		print()
		seed_url = get_random_link(seed_url)
		counter += 1


# --------------------------------play games-------------------------------- #

# game1('/wiki/Peach', 6)

game2('/wiki/Peach')