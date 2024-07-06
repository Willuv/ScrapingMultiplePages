from bs4 import BeautifulSoup
import requests

#Get the HTML
root = 'https://subslikescript.com/' #Homepage of the website 
website = f'{root}/movies' #concatenate the homepage with the movies section 
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')

#find the box that contains the list of movies
box = soup.find('article', class_='main-article')

#store each link in the links list
links = []
for link in box.find_all('a', href=True):
    links.append(link['href'])

#loop through each link and send a request to each link
for link in links:
    result = requests.get(f'{root}/{link}')
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    #find the box with the title and transcript
    box = soup.find('article', class_='main-article')
    #find the title and transcript
    title = box.find('h1').get_text()

    transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

    #export the files the the titles of each movie
    with open(f'{title}.txt', 'w', encoding='utf-8') as file:
        file.write(transcript)