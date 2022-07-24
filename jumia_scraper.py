from bs4 import BeautifulSoup
import requests
import time
import openpyxl

def Scrape_Jumia():
    excel = openpyxl.Workbook()
    sheet = excel.active
    sheet.title = 'Jumia Phone Data'
    sheet.append(['Phone Name', 'Price', 'URL',])
    # Iterate through pages
    for page in range(1,51):        
        url = f'https://www.jumia.com.ng/smartphones/?page={page}.html'
        page = requests.get(url).text
        soup = BeautifulSoup(page, 'lxml')

        # Get data from each container
        smartphones = soup.find_all('article', class_='prd _fb col c-prd')
        for phone in smartphones:
            name = phone.h3.text
            price = phone.find('div', class_='prc').text
            url = 'https://www.jumia.com.ng/smartphones' + str(phone.find('a')['href'])

            print(f'Phone: {name}')
            print(f'Phone Price: {price}')
            print(f"Phone Link: {url}")

            sheet.append([name, price, url])

        excel.save('Jumia Phone Database.xlsx')


if __name__ == '__main__':
    while True:
        Scrape_Jumia()
        time_wait = 1
        print(f'Waiting {time_wait} day...')
        time.sleep(time_wait *60*60*24)
            