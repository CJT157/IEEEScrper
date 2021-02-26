from bs4 import BeautifulSoup
import requests
import datetime
import dateparser as dp

def get_movie_info(URL):
    # Variables
    title = ''
    release =''
    genres_html = []
    genres = []
    director = ''
    plot = ''
    rating = ''
    stars_html = []
    stars = []
    poster = ''

    # Gets info for movie from IMDB
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, features="html.parser")

    # Gets title of movie
    title = soup.find('h1', class_='').text

    # Gets list of genres
    genres_html = soup.find('div', class_='subtext').find_all('a')

    # Adds html genres to the genre list
    for i in genres_html[:-1]:
        genres.append(i.text)

    # Gets and formats the release date
    release = genres_html[-1].text
    release = release.split('(')[0]
    release = dp.parse(release)

    # Gets director of movie
    director = soup.find('div', class_="credit_summary_item").find('a').text

    # Gets the plot of movie
    plot = soup.find('div', class_="summary_text").text
    plot = plot.replace('\n', '')
    plot = plot.replace('                    ', '')

    # Gets rating of movie and converts to a numerical value
    rating = soup.find('div', class_='ratingValue').text
    rating = rating.split('/')[0]
    rating = rating.replace('\n', '')
    rating = float(rating)

    """
    # Gets stars of movie
    # TODO: Figure out how to get a specific div from a list that use the same class name
    stars_html = soup.find('div', class_='credit_summary_item').find_all('a')
    for i in stars_html[:-1]:
        stars.append(i.text)
    """

    # Gets poster of the movie
    poster = soup.find('div', class_='poster').find('img')['src']
    
    # Prints movie info
    print('-----------------------------------------------------------------')
    print(title)
    print(release)
    print(genres)
    print(director)
    print(plot)
    print(rating)
    # print(stars)
    print(poster)
    print('-----------------------------------------------------------------')
    

print('Welcome to the IMDB Scraper!')
URL = input('Please enter a IMDB Movie URL: ')

get_movie_info(URL)

# https://www.imdb.com/title/tt1130884/?ref_=fn_al_tt_1