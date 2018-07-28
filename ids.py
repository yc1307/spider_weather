# encoding: utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


def city_choice():
    f = open('ids.txt', 'r', encoding='utf-8')
    city_dict = {}

    for city in f.readlines():
        city_id, city_name = city.split('=')
        city_name = re.sub('\n', '', city_name)
        city_dict[city_name] = city_id
    return city_dict


def weather_find():
    city_name = input("请输入查询地名称:")
    c = city_choice()
    if city_name in c:
        response = urlopen("http://www.weather.com.cn/weather/" + c[city_name] + ".shtml")
        soup = BeautifulSoup(response, "html.parser")
        tagToday = soup.find("p", class_="tem")
        try:
            tem_high = tagToday.span.string
        except AttributeError as e:
            tem_high = tagToday.find_next("p", class_="tem").span.string

        tem_low = tagToday.i.string
        weather = soup.find("p", class_="wea").string

        print("最高温度：" + tem_high)
        print("最低温度：" + tem_low)
        print("天气：" + weather)


if __name__ == '__main__':
    weather_find()
