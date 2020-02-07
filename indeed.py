import requests
from bs4 import BeautifulSoup

url = 'https://www.indeed.com/jobs?q=python%20developer&l=Indianapolis%2C%20IN&advn=2658045788698410&vjk=34f0fc6430bd0db8'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='jobsInLocation')
#print(results.prettify())

# THIS IS CAUSING NO POSTINGS TO SHOW UP, SPECIFICALLY THE SECTION AND CLASS ARE WRONG!!!!!!
job_elems = results.find_all(id='resultsCol')


for job_elem in job_elems:
    title_elem = job_elem.find('div', class_='title')
    company_elem = job_elem.find('div', class_='sjcl')
    location_elem = job_elem.find('div', class_='recJobLoc')
    salary_elem = job_elem.find('div', class_='salarySnippet.holisticSalary')
    if None in (title_elem, company_elem, location_elem, salary_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print(salary_elem.text.strip())
    print()


#python_jobs = results.find_all('div', string=lambda text: 'python' in text.lower())
# print(len(python_jobs))

# for p_job in python_jobs:
#    link = p_job.find('a')['href']
#    print(p_job.text.strip())
#    print(f'Apply here: {link}\n')
