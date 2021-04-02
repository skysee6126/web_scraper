import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://kr.indeed.com/jobs?q=python&limit=50")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class": "pagination"})
pages = pagination.find_all('li')
spans = []
for page in pages:
    spans.append(page.find("span"))
spans = spans[1:-1]
print(spans)
