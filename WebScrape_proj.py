from bs4 import BeautifulSoup
import collections #SAVE TAGS TO COLLECTIONS
import argparse #COMMANDS, SAVE, GET, VIEW
import requests #REQUEST PAGE

parser = argparse.ArgumentParser()
parser.add_argument('--get', type=str)
args = parser.parse_args()
r = requests.get('https://ca.indeed.com/jobs?q=python%20programmer&l=Toronto%2C%20ON')
soup = BeautifulSoup(r.content, 'html.parser')




def SAVE_TAGS():
	pass


def VIEW_SAVED_TAGS():
	pass


def GET_TAGS_LINKS():
	Job_Titles = [Job_name for Job_name in soup.find_all('span')]
	Company_name = []
	for tag in lst:
		tags = tag.get('title')
		if tags != None:
			print(tags)

def main():
	if args.get == 'tags':
		GET_TAGS_LINKS()
	if args.get == 'view':
		VIEW_SAVED_TAGS()

if __name__ == "__main__":
	main()