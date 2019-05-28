from bs4 import BeautifulSoup
import requests
import commands
import collections


goodreads_url = "https://www.goodreads.com/"
# The one you write on the url to check an username url
main_url = goodreads_url + commands.command_args.user
page_main = requests.get(main_url)
parsed_page_main = BeautifulSoup(page_main.text, 'html.parser')
# Get the proper username url in goodreads format
url_user = parsed_page_main.find('link')['href']
#page_user = requests.get(url_user) not need anything from here at the moment
url_read_shelf = goodreads_url + "/review/list/" + url_user[36:url_user.find("-")] + "?shelf=read"  # where most of the dat is in frthe user
#link when click read is https://www.goodreads.com/review/list/86868346?shelf=read
page_read_shelf = requests.get(url_read_shelf)
# The parsed page and from thi is where i will get the most of the data
parsed_read_shelf = BeautifulSoup(page_read_shelf.text, 'html.parser')


reviews = []
for review in parsed_read_shelf.find_all("td", class_="field review"):
    reviews.append(review.get_text().strip("\n*").strip())
long_review = collections.Counter(reviews).most_common(3)
#print(f"The 3 most read Authors are:")
#for name, num in most_read:
#    print(f"{name:{4}{2}}{num:{2}} Books"  )
print(most_read)