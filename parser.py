import requests
from bs4 import BeautifulSoup
#from selenium import webdriver
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","firstproject1.settings")
import django
django.setup()
from blogapp.models import BlogData

def parse_blog():
    # python파일의 위치
   #BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    #options = webdriver.ChromeOptions()
    #options.add_experimental_option('excludeSwitches', ['enable-logging'])
    #driver = webdriver.Chrome("C:\selenium\chromedriver.exe")
    #driver.get('https://post.naver.com/my.nhn?memberNo=938657')

    #html = driver.page_source
    req = requests.get('http://www.naeilmohaji.co.kr/news/articleList.html?sc_sub_section_code=S2N7')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    #my_titles = soup.select('div > div.feed_body > div.text_area > a.link_end > strong')
    my_titles = soup.select('#user-container > div.float-center.max-width-960 > div.user-content > section > article > div.article-list > section > div> div.list-titles.table-cell > a')
    data = {}

    for title in my_titles:
        data[title.text] = title.get('href')
    return data
    #print(title)

if __name__=='__main__':
    blog_data_dict = parse_blog()
    for t, l in blog_data_dict.items():
        BlogData(title=t, link=l).save()

