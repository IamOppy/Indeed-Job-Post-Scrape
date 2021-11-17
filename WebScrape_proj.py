from bs4 import BeautifulSoup
import collections #SAVE TAGS TO COLLECTIONS
import argparse #COMMANDS, SAVE, GET, VIEW
import requests #REQUEST PAGE

parser = argparse.ArgumentParser()
parser.add_argument('--get', type=str)
args = parser.parse_args()
r = requests.get('https://ca.indeed.com/jobs?q=python%20programmer&l=Toronto%2C%20ON')
soup = BeautifulSoup(r.content, 'html.parser')





def GET_TAGS_LINKS():
	Job_Titles = [Job_name.get('title') for Job_name in soup.find_all('span') if Job_name.get('title') != None]
	Company_name = [com_name.get_text() for com_name in soup.find_all('span', {'class': 'companyName'})]
	Company_Location = [Location.get_text() for Location in soup.find_all('div', {'class': 'companyLocation'})]
	return Job_Titles, Company_name, Company_Location

def return_zipped_list(lst=GET_TAGS_LINKS()):
	lst1 = lst[0]
	lst2 = lst[1]
	lst3 = lst[2]
	zip_all = zip(lst1, lst2, lst3)
	return list(zip_all)

def convert_to_dict(zipped_result):
	dictt_result = collections.defaultdict(dict)
	for jobname, company_name, companyLocation in zipped_result:
		dictt_result[jobname] = company_name, companyLocation
	return dictt_result

def View_result(dict_result):
	for k,v in dict_result.items():
		print(f'||JOB TITLE:--{k}  ||COMPANY NAME:--{v[0]}  ||COMPANY LOCATION/TYPE:--{v[1]}' )

def main():
	if args.get == 'view':
		zipped_result = return_zipped_list()
		dict_result = convert_to_dict(zipped_result)
		print(View_result(dict_result))	

if __name__ == "__main__":
	main()