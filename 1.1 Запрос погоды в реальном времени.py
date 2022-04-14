from bs4 import BeautifulSoup
# если возникает проблема с сертификатом при запуске кода то добавить строчки 1-8
import urllib.request
import ssl
import requests

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE
mint, maxt = 0, 0
min_city, max_city = "", ""
d1 = {
    "Калуга": "https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B0%D0%BB%D1%83%D0%B3%D0%B0-100553915",
    "Москва": "https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BC%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
    "Санкт-Петербург": "https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%81%D0%B0%D0%BD%D0%BA%D1%82-%D0%BF%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
    "Львов": "https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BB%D1%8C%D0%B2%D0%BE%D0%B2",
    "Киров": "https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D1%80%D0%BE%D0%B2",
    "Самара": "https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%81%D0%B0%D0%BC%D0%B0%D1%80%D0%B0-100499099",
    "Якутск": "https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%8F%D0%BA%D1%83%D1%82%D1%81%D0%BA",
    "Сочи": "https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%81%D0%BE%D1%87%D0%B8",
    "Тбилиси": "https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%82%D0%B1%D0%B8%D0%BB%D0%B8%D1%81%D0%B8",
    "Ялта": "https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%8F%D0%BB%D1%82%D0%B0",
    "Бодрум": "https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%B1%D0%BE%D0%B4%D1%80%D1%83%D0%BC",
    "Аланья": "https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%B0%D0%BB%D0%B0%D0%BD%D1%8C%D1%8F",
    "Шарм-эль-Шейх": "https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%88%D0%B0%D1%80%D0%BC-%D1%8D%D0%BB%D1%8C-%D1%88%D0%B5%D0%B9%D1%85",
    "Хургарда": "https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%85%D1%83%D1%80%D0%B3%D0%B0%D0%B4%D0%B0",
    "Дубай": "https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%B4%D1%83%D0%B1%D0%B0%D0%B9",
    "Портленд": "https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BF%D0%BE%D1%80%D1%82%D0%BB%D0%B5%D0%BD%D0%B4-105746545",
    "Майами": "https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BC%D0%B0%D0%B9%D0%B0%D0%BC%D0%B8",
    }

print("Текущая погода:")
for key, value in d1.items():
    resp = requests.get(value)
    soup = BeautifulSoup(resp.content, 'html.parser')
    cls1 = "weather__article_main_temp"
    cls2 = "_2LM4MsxZ"
    cls3 = "today-temp"
    value_f = soup.find("p", class_=cls3).text.lstrip()
    print(key + ":", value_f)
    temp = int(value_f[0:len(value_f) - 2])

    if temp < mint:
        mint = temp
        min_city = key
    elif temp > maxt:
        maxt = temp
        max_city = key
print("Холоднее всего в городе", min_city, str(mint) + "°C")
print("Теплее всего в городе", max_city,  str(maxt) + "°C")


