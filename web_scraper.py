import requests
from bs4 import BeautifulSoup
def web_scraper(URL, keywords):
    page = requests.get(URL)
    keywords = keywords.strip()
    keywords = keywords.split(',')
    for i in range(len(keywords)):
        if (keywords[i][0] == ' '):
            keywords[i] = keywords[i][1:]
    print(keywords)
    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.find("meta", property="og:title")
    description = soup.find("meta", property="og:description")
    job_elements = soup.find_all("div", class_="ssrcss-7uxr49-RichTextContainer e5tfeyi1")


    for job_element in job_elements:
        title_element = job_element.find("p", class_="ssrcss-1q0x1qg-Paragraph eq5iqo00")
        if title_element is not None:
            for keyword in keywords:
                if(str(title_element.text).__contains__(keyword)):
                    print(title_element.text)
                    break
