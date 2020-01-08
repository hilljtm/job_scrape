import requests
from bs4 import BeautifulSoup

url = 'https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=true&clickSource=searchBtn&typedKeyword=Python&sc.keyword=Python+Programmer&locT=C&locId=1145013&jobType='

page = requests.get(url)
print(page)

