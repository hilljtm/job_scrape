import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=true&clickSource=searchBtn&typedKeyword=Python&sc.keyword=Python+Programmer&locT=C&locId=1145013&jobType='

page = requests.get(url)


soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='')


job_elems = results.find_all('section', class_='')

for job_elem in job_elems:
    title_elem = job_elem.find()
    company_elem = job_elem.find()
    location_elem = job_elem.find()
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()

python_jobs = results.find_all()
