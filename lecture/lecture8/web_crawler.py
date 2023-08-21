import requests 
from bs4 import BeautifulSoup


def main():
	url = 'https://www.imdb.com/chart/top'
	header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
	response = requests.get(url, headers=header)
	html = response.text  # simple string
	soup = BeautifulSoup(html)
	tags = soup.find_all('span', {'class': 'sc-14dd939d-6 kHVqMR cli-title-metadata-item'})
	d = {}
	for tag in tags:
		if tag.text.isdigit():
			year = tag.text
			if year not in d:
				d[year] = 1
			else:
				d[year] += 1
	for year, count in sorted(d.items(), key=lambda t:t[1]):
		print(year, '-->', count)
if __name__ == '__main__':
	main()
