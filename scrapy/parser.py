import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt

HOST = "https://www.cinematica.kg/"

HEADERS ={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36",


}

@csrf_exempt
def get_html(url):
    req = requests.get(url=url, headers=HEADERS)
    return req

@csrf_exempt
def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("a", class_="movie-dummy")
    movies = []

    for item in items:
        movies.append(
            {
                "link": item.find("a class").get("href"),
                "title": item.find("div", class_="movie-title").get_text(strip=True),
                "image": item.find("a class").find("img").get("src"),
            }
        )
    return movies

@csrf_exempt
def parser_fuct():
    if html.status_code == 200:
        movies = []
        for i in range(0,2):
            movies.extend(get_data(html.text))
        return movies
    else:
        raise Exception("Error in parser function")

print(parser_fuct())

html = get_html(HOST)
get_data(html.text)