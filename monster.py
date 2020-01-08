import requests
from bs4 import BeautifulSoup


url = 'https://www.monster.com/jobs/search/?q=Python-Developer&where=Indianapolis__2C-IN&intcid=skr_navigation_nhpso_searchMain'
page = requests.get(url)


soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='SearchResults')
print(results.prettify())


job_elems = results.find_all('section', class_='card-content')

for job_elem in job_elems:
    print(job_elem, end='\n' * 2)


for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job.elem.find('div', class_='location')
    print(title_elem)
    print(company_elem)
    print(location_elem)
    print()

