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

def extract_indeed_job(html):
        title =html.find("h2", {"class": "title"}).find("a")["title"]
        company = html.find("span", {"class": "company"})
        company_anchor = company.find("a")
        if company_anchor is not None:
            company = (str(company_anchor.string))
        else:
            company = (str(company.string))
        company = company.strip()
        location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
        job_id = html.find("h2", {"class":"title"}).find("a")["href"]
        return {'title': title, 'company': company, 'location': location, 'link': f"https://kr.indeed.com{job_id}"}


def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{indeed_url}&start={page*limit}")
        soup = BeautifulSoup(result.text,"html.parser")
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        for result in results:
            job = extract_indeed_job(result)
            jobs.append(job)
    return jobs