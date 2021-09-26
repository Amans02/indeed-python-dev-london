import requests
from bs4 import BeautifulSoup
import schedule
import time

URL_ = "https://uk.indeed.com/jobs?q=python+developer&l=London,+Greater+London&start=0"


def extract(page):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/93.0.4577.82 Safari/537.36"}
    # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
    URL = f'https://uk.indeed.com/jobs?q=python+developer&l=London,+Greater+London&start={page}'
    req = requests.get(url=URL, headers=headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    return soup


class SalaryNotFoundException(BaseException):
    pass


def transform(soup: BeautifulSoup):
    # divs = soup.find_all('div', class_='job_seen_beacon')
    divs = soup.find_all('a', class_='tapItem')
    print(len(divs))
    # print(divs)

    job_data_list = []

    for item in divs:
        title = item.find('h2', class_='jobTitle').text.strip()
        # links = item.find('href', attrs={'class': 'tapItem'})
        link = item['href']
        # links = item.aclass['tapItem']['href']
        # print(links)
        if title.startswith('new'):
            title = title[3:]
        company_name = item.find('span', class_="companyName").text.strip()
        company_location = item.find('div', class_="companyLocation").text.strip()
        summary = item.find('div', {'class': 'job-snippet'}).text.strip()
        try:
            salary = item.find('span', class_="salary-snippet").text.strip()
        except:
            salary = 'not specified'
        job_data = {'title': title,
                    'company': company_name,
                    'location': company_location,
                    'salary': salary,
                    'summary': summary,
                    'link': link}
        job_data_list.append(job_data)

    return job_data_list


def send_message_to_telegram(job_data_list):
    for job in job_data_list:
        company = job.get('company')
        title = job.get('title')
        location = job.get('location')
        salary = job.get('salary')
        link = job.get('link')
        href_link = f'<a href="{link}">click to apply</a>'
        print(href_link)
        # html_text = "<html>" \
        #             '<p>{company}</p>' \
        #             "<p></p>" \
        #             "</html>"
        text = "Title: " + title + "\n" + "company: " + company + "\n" + "location: " + location + "\n" + "salary: " + salary + "\n" + "link to apply: " + href_link + "\n"
        # print(text)
        base_url = f'https://api.telegram.org/bot2012439390:AAEQ-yU7EM0LPYlVXgvv0E5TqGIOMwgQ83E/sendMessage?chat_id' \
                   f'=-473759634&text={text}'
        # & parse_mode = HTML
        requests.get(base_url)
    print("\n")

def main():
    s = extract(0)
    job_list = transform(s)
    send_message_to_telegram(job_list)


# for item in job_list:
#     print(item)
# schedule.every(1).minute.do(main)
schedule.every(10).minutes.do(main)
while True:
    schedule.run_pending()
    time.sleep(1)
