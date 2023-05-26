'=================================Parsing============================'
#парсинг - процесс автоматического сбора данных 
# Библиотека
# 1. requests - отправляет запрос на сайт и в итоге получает html код страницы
# 2 . BeautifulSoup - помогает извлечь информациюю из html.помогает обращаться к определенным тегам и вытаскивать инфо
# 3. lxml - вступает в роли парсера для BeautifulSoup. (ОН разбивает информацию на мелкие части и анализирует данные.)
#  python3 -m venv venv -создание виртуальное окружения
# source venv/bin/active     ативировали виртуальное окружение или .venv/bin/active 
# 

# import requests 
# from bs4 import BeautifulSoup
# import csv
# url= 'https://enter.kg/computers/noutbuki_bishkek'

# def write_to_csv(data):
#     with open('data.csv', 'a') as file:
#         writer = csv.writer(file)
#         writer.writerow([data['title'],data['price'],data['image']])


# def get_html(url):
#     response = requests.get(url)
#     return response.text

# def get_data(html):
#     soup = BeautifulSoup(html,'lxml')
#     list_comp = soup.find_all('div', class_ = 'row')
#     for comp in list_comp:
#         title = comp.find('span', class_ = 'prouct_name').text
#         price = comp.find('span', class_ = 'price').text
#         image = 'https://enter.kg' + comp.find('img').get('src')
#         dict_ = {'title':title, 'price':price, 'image': image}
    
#         write_to_csv(dict_)



# # count = 1
# # while True:
# #     print(f'count->{count}')
# import requests
# from bs4 import BeautifulSoup
# import time

# url = 'https://www.example.com'
# count = 0

# while True:
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     print(soup.title.string)
#     count += 1
#     print(f'count->{count}')
#     time.sleep(60)  


#print(get_data(get_html(url)))
'=============================================='
# Метод find_all
# find_all просматривает все вложенные элементы указанного тега, а также может производить поиск по указанному классу тега.

# find_all возвращает все совпадения в виде списка, например:

# my_page.find_all('p', 'title')  
# в my_page хранится страница в виде объекта BeautifulSoup, с помощью find_all указываем найти все теги <p>, с классом title, получим список:

# [<p class="title">Хоббит, или Туда и Обратно</p> , 
# <p class="title">Сильмариллион</p>, 
# <p class="title">Неоконченные предания Нуменора и Средиземья</p>] 
# Теперь, с данным списком можно работать как с обычным объектом Python - перебирать циклами, использовать в функциях и.т.п

# Задание 3
# Выведите с главной страницы википедии:

# https://www.wikipedia.org/

# сколько всего статей есть немецком языке.

# Вывод в консоль должен быть таким:
# Deutsch
# 2 590 000+ Artikel 

# import requests 
# from bs4 import BeautifulSoup
# import csv

# source = requests.get('https://www.wikipedia.org/').text 
# my_page = BeautifulSoup(source, 'lxml') 
# blog_lang = my_page.find('div', class_ = 'central-featured-lang lang4')
# print(blog_lang.text)

'))================================='
# 1. BeautifulSoup
# 2. Requests
# 3. Lxml


# import requests
# from bs4 import BeautifulSoup


# def get_html(url):
#     response = requests.get(url)
#     return response.text

# def get_total_pages()



# def main():
#     notebooks_url = 'https://www.eldorado.ru/c/noutbuki/'
#     pages = '?page'
#     get_html(notebooks_url)

# main()


import requests
from bs4 import BeautifulSoup
import csv
url = 'http://kenesh.kg/ru/news/all/list'

def write_to_csv(data1):
    with open('data1.csv','a')as f:
        writer = csv.writer(f)
        writer.writerow([data1['title'],data1['date'],data1['img']])

def get_html(url):
    response = requests.get(url)
    return response.text


def get_data(html):
    soup = BeautifulSoup(html,'lxml')
    list_news = soup.find_all('div', class_="news__grid")
    # print(list_news)

    for news in list_news:
        title = news.find_all('a', class_='news__item__title__link')
        for x in title:
            title1 = x.text
            date = news.find('div',class_ = 'news__item__date').text
            img = 'http://kenesh.kg'+news.find('img').get('src') if news.find('img') != None else 'None'
            dict_ = {'title':title1, 'date': date, 'img':img}
            write_to_csv(dict_)

    count = 1
get_data(get_html(url))


# # while True:
# #     print(f'count->{count}')


# def get_total_pages()


# def main():
#     jk= 'http://kenesh.kg/ru/news/all/list'
#     pages = ''
#     get_html(jk)

# main()

# import requests
# import csv
# import requests
# from bs4 import BeautifulSoup as bs

# def write_csv(data):
#     with open('kenesh.csv','a') as f:
#         writer = csv.writer(f)
#         writer.writerow([data['title'],data['date'],data['image'],data['description']])
# def get_html(url):
#     response = requests.get(url)
#     return response.text


# for page in range(20):
#     url = f'http://kenesh.kg/ru/news/all/list?page={count}'
#     response = requests.get(url)
#     htmltext = response.text
#     soup = BeautifulSoup(htmltext, 'lxml')
#     news_items = soup.find_all('div','news__item news__item__3')
#     for i in news_items:
#         title = i.find('a', class_ = 'news__item__title__link').text
#         date = i.find('div','news__item__date').text
#         image = 'http://kenesh.kg'+i.find('img').get('src') if i.find('img') != None else 'NONE'
#         dict_ = {'title':title,'date':date,'image':image}
    
#         write_to_csv(dict_)
        
#     count+=1