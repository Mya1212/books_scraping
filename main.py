import requests
from bs4 import BeautifulSoup
from pathlib import Path
from slugify import slugify
import csv

BASE_URL= "https://books.toscrape.com/"
DATA_DIR= "data/csv/"
IMG_DIR ="data/img/" 

def recup_data(url):
    """transforme les données homepage en html"""
    response = requests.get(url)
    if not response.ok:
        print("Un problème est survenu")
        return None
    return BeautifulSoup(response.content,"html.parser")

def get_category_url():
    """récupère une liste des urls de toutes les catégories"""
    soup = recup_data(BASE_URL)
    div=soup.find("div","side_categories")
    result=[]
    name = soup.find('h1').text
    if soup is None:
        return
    for link in div.find_all("a"):
        result.append(BASE_URL+link.get("href"))
    return result[1:]

def get_book_url(url_page):
    """récupère une liste des urls des livres"""
    book_url = []
   
    go_next_page = True
    page_number = 1
    while go_next_page:
        if page_number == 1:
            url = url_page
        else:
            url= url_page.replace("index.html", f"page-{page_number}.html")
        
        soup = recup_data(url)

        h3_elements = soup.find_all('h3')
        for h3 in h3_elements:
           link = BASE_URL+"catalogue/"+h3.a.get("href").strip('../../../')
           book_url.append(link)

        next_page_button = soup.find('li', class_="next")
        if next_page_button is None:
            go_next_page = False
        page_number += 1

    return book_url


def get_book_data(url):
    """récupère les données d'un livre dans un dictionnaire"""
    soup = recup_data(url)
    if soup is None:
        return
    product_page_url = url
    universal_product_code = soup.find_all('td')[0].get_text()
    title = soup.find('h1').get_text()
    price_including_tax = soup.find_all('td')[3].get_text()
    price_excluding_tax = soup.find_all('td')[2].get_text()
    number_available = soup.find_all('td')[5].get_text() 
    number_available = number_available.strip("In stock (available)")
    product_description = soup.find_all('p')[3].get_text()
    category = soup.find_all('a')[3].get_text()
    review_rating = soup.find(class_ = "star-rating")['class'][1]
    review_rating=convert_rating(review_rating)
    image_url = soup.find_all('img')[0]['src'].replace('../..', 'https://books.toscrape.com')

    info = {'product_page_url':product_page_url,
    'universal_product_code':universal_product_code,
    'title' :title,
    'price_including_tax': price_including_tax,
    'price_excluding_tax':price_excluding_tax,
    'number_available':number_available,
    'product_description':product_description,
    'category':category,
    'review_rating':review_rating,
    'image_url':image_url,
}
    return info

def convert_rating(rating):
    rating_number ={'One':1,'Two':2,'Three':3,'Four':4,'Five':5,}
    return rating_number.get(rating)

def save_data_to_csv(category, books_data):
    # écriture fichier csv livre 
    # en_tete = ['product_page_url', 'upc', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url'] 
    header = books_data[0].keys()
    category = books_data[0].get("category")
    with open(DATA_DIR+category+".csv",'w',encoding='utf-8-sig',newline="") as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(books_data)

def save_image(books_data):
    category = slugify(books_data[0].get("category"))
    Path(f"{IMG_DIR+category}").mkdir(parents=True,exist_ok=True)
    for book in books_data:
        image_url = book.get("image_url")
        title = slugify(book.get("title"))
        image_response = requests.get(image_url)
        with open(IMG_DIR+category+"/"+title+".jpg",'wb') as img:
            img.write(image_response.content)

def main():
    #liste de toutes les catégories
    print ("Récupération des liens des catégories en cours...")
    categories=get_category_url()

    #création directory pour fichiers CSV
    Path(DATA_DIR).mkdir(parents=True,exist_ok=True)
    Path(IMG_DIR).mkdir(parents=True,exist_ok=True)
    print ("Récupération des liens des livres en cours...")
    for category in categories:
        #récupère la liste des livres d'une catégorie
        books_url = get_book_url(category)
        #dictionnaire pour stocker la liste des livres
        books_data = []
        print ("Récupération des données des livres en cours...")
        for book_url in books_url:
            book_data = get_book_data(book_url)
            #récupère les données pour un livre
            books_data.append(book_data)

        print ("Ecriture du fichier CSV en cours...")    
        save_data_to_csv(category,books_data)

        print ("Récupération des images en cours...")
        save_image(books_data)

if __name__ == '__main__':
    main()

