from bs4 import BeautifulSoup
import collections #SAVE TAGS TO COLLECTIONS
import argparse #COMMANDS, SAVE, GET, VIEW
import requests #REQUEST PAGE

parser = argparse.ArgumentParser()
parser.add_argument('--get', type=str)
args = parser.parse_args()
r = requests.get('http://toscrape.com/')
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())

def GET_TAGS():
	print('getting')



def SAVE_TAGS():
	pass


def VIEW_SAVED_TAGS():
	pass

def main():
	if args.get == 'tags':
		GET_TAGS()
	if args.get == 'view':
		VIEW_SAVED_TAGS()