from bs4 import BeautifulSoup
import time
import requests

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=&cboWorkExp1=0').text
    print("Put some Skill that you are not familiar with")
    unfamiliar_skill = input('>').casefold()
    print(f'Filtering Out {unfamiliar_skill}')
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li', class_ ='clearfix job-bx wht-shd-bx')

    for index, values in enumerate(jobs):
        posted_time = values.find('span',class_ = 'sim-posted').span.text
        if 'few' in posted_time: 
            company_name = values.find('h3', class_ = 'joblist-comp-name').text.replace(' ','').strip()
            skills = values.find('span',class_='srp-skills').text.replace(' ','').strip()
            more_info = values.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.json','w') as f:
                    f.write(f"Company Name : {company_name.strip()}")
                    f.write(f"Required Skills : {skills.strip()}")
                    f.write(f"More Info : {more_info}")
                print(f'File saved : {index}')
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} seconds.....')
        time.sleep(time_wait*60)
