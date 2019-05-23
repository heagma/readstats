#No uso por el momento, solo para probar
from bs4 import BeautifulSoup
import requests
url = 'https://www.goodreads.com/heagma'
page = requests.get(url) 
parsed_page = BeautifulSoup(page.text, 'html.parser')
properurl = parsed_page.find('link')['href']
#print(parsed_page.prettify())
print() #find the first link tag on the document and as i know is the one with the url i get the attributte hrefas it is a key value pair
print(properurl[36:properurl.find("-")])