# import requests
# import bs4
# import json

# keywords = ['Django', 'Flask']
# headers = {
#   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/58.0.3029.110 ',
# }
# main_response = requests.get('https://spb.hh.ru/search/vacancy?text=python&area=1&area=2', headers=headers)
# main_html_data = main_response.text
# main_soup = bs4.BeautifulSoup(main_html_data, features='lxml')
# main_tag = main_soup.find('main', class_='vacancy-serp-content')

# parsed_data = []

# if main_tag is not None:
#     all_job_cards = main_tag.find_all('div', {'data-qa': 'vacancy-serp__vacancy vacancy-serp__vacancy_standard_plus'})
#     for job in all_job_cards:
#         city = job.find('span', {'data-qa': 'vacancy-serp__vacancy-address'}).text
#         header = job.find('span', {'data-qa': 'serp-item__title'}).text
#         salary = job.find('span', class_='bloko-text').text
#         link = job.find('a', class_='bloko-link')['href']
#         parsed_data.append({
#             'city': city,
#             'header': header,
#             'salary': salary,
#             'link': link
#             })
# else:
#     print("Ничего не найдено")

# print(parsed_data)




import requests
import bs4
import json

keywords = ['Django', 'Flask']
city_mapping = {
    '1': 'Moscow',
    '2': 'St. Petersburg'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/58.0.3029.110 ',
}
main_response = requests.get('https://spb.hh.ru/search/vacancy?text=python&area=1&area=2', headers=headers)
main_html_data = main_response.text
main_soup = bs4.BeautifulSoup(main_html_data, features='lxml')
main_tag = main_soup.find('main', class_='vacancy-serp-content')

job_listings = []

if main_tag:
    description_element = main_tag.find('div', {'data-qa': 'vacancy-serp__vacancy_snippet_responsibility'})
    if description_element:
        description = description_element.text.lower()
    else:
        description = ""
    for job in job_listings:
        description = job.find('div', {'data-qa': 'vacancy-serp__vacancy_snippet_responsibility'}).text.lower()
        if all(keyword.lower() in description for keyword in keywords):
            job_info = {
                'link': job.find('a', {'data-qa': 'vacancy-serp__vacancy-title'})['href'],
                'salary': job.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'}),
                'company': job.find('a', {'data-qa': 'vacancy-serp__vacancy-employer'}).text,
                'city': city_mapping[job.find('span', {'data-qa': 'vacancy-serp__vacancy-address'}).find('a')['href'].split('=')[-1]]
            }
            job_listings.append(job_info)
else:
    print("Main tag не найден")

with open('job_listings.json', 'w') as json_file:
    json.dump(job_listings, json_file, indent=4)