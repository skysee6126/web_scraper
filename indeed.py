import requests
from bs4 import BeautifulSoup

limit = 50
indeed_url = f"https://www.indeed.com/jobs?q=python&limit={limit}"

def extract_indeed_pages():
    result = requests.get(indeed_url)
    soup = BeautifulSoup(result.text,"html.parser")
    pagination=soup.find("div",{"class":"pagination"})
    links = pagination.find_all('a')
    pages=[]
    for link in links[0:-1]:
        pages.append(int(link.string))
    pages = pages[:]

    max_page = pages[-1]
    return max_page

def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{indeed_url}&start={page*limit}")
        soup = BeautifulSoup(result.text,"html.parser")
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        for result in results:
            title =result.find("h2", {"class": "title"}).find("a")["title"]
            print(title)
    return jobs