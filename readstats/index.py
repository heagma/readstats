#Statistics for what a user reads
from commands import parse_commands
import sys
import requests
from bs4 import BeautifulSoup



class Users:
    #aqui voy guardando las urls donde voy a tomar los datos y prettifying them
    goodreads_url = "https://www.goodreads.com"
    main_url = goodreads_url + command_args.user  #The one you write on the url to check an username url
    page_main = requests.get(main_url) 
    parsed_page_main = BeautifulSoup(page_main.text, 'html.parser')
    
    url_user = parsed_page_main.find('link')['href'] #Get the proper username url in goodreads format
    #page_user = requests.get(url_user) not need anything from here at the moment
    url_read_shelf = goodreads_url + "/review/list" + url_user[36:url_user.find("-")]  + "?shelf=read" #where most of the dat is in frthe user
    #link when click read is https://www.goodreads.com/review/list/86868346?shelf=read
    page_read_shelf = requests.get(url_read_shelf)
    parsed_read_shelf = BeautifulSoup(page_read_shelf.text, 'html.parser') #The parsed page and from thi is where i will get the most of the data
    
    def __init__(self, name):
        """Instantiate user data to use with other methods"""
        self.name = name
        #self.email = email

    def search_user(self):
        """Search if an user name exist on Goddreads Database
        Parameters: self
        Return: url"""
        
        if page_main.status_code == 200: 
            print(f"The User {command_args.user} EXIST in GoodReads", 
            "Now get a few stats with the optional parameters [-AagTtbrsrlr]", 
            "EXAMPLE: 'heagma -g' to look for favorite genres ", sep="\n") 
        else:
             print(f"The User {command_args.user} DOESN'T EXIST in GoodReads", "Please Try another User", sep="\n")#como puedes ver usamos name e email the lo instaciado arriba
        return url
    def get_all_stats(self):
        return True
    
    def get_authors(self):
        return True
    
    def get_genres(self):
        user = command_args.user
        fav_genres = []
        num_books = 0
        print(f"""{user} Favorite Genres: {fav_genres}
        Number of Books: {num_books}""")
        return True
    
    def get_longest_review(self):
        return True
    
    def get_shortest_review(self):

        return True
    
    def get_liked_review(self):

        return True
    
    def get_less_time(self):   
 
        return True
    
    def get_more_time(self):
        return True

    
#aqui impleeto la busqueda del suruaio    



if __name__ == "__main__":
    parser = parse_commands()
    command_args = parser.parse_args()
    username = Users(command_args.user)
    #no need at the moment ya que siendo posicionalargument es necesario para entrar otro argumetoopcional
    #if command_args.genre: #If we use Optional commands before --user 
    #    parser.print_help(sys.stderr) # Then print the error, print_help() is a verbose function 
    #    sys.exit(1)
    if command_args.user and len(sys.argv[:]) == 2: #To check if the user only input 1 argument (user) 
        username.search_user()
    elif command_args.user and command_args.genres:
        
        username.get_genres() #imprimimos los generos
    