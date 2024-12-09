import requests
from django.contrib.auth.decorators import login_required
from bs4 import BeautifulSoup
from django.shortcuts import render
@login_required(login_url='/users/login/')
def homepage(request):
    url = "https://tsn.ua/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        
        articles = []
        for item in soup.select(".c-card__title a"):  
            title = item.get_text(strip=True)
            link = item["href"]
            if not link.startswith("http"):
                link = f"https://tsn.ua{link}"
            articles.append({"title": title, "link": link})

        print("Отримані новини:")
        print(articles)

    except Exception as e:
        print(f"Помилка парсингу: {e}")
        articles = []  

    return render(request, 'home.html', {"news": articles})
