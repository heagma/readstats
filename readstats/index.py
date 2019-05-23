#Statistics for what a user reads
import sys
import requests
from bs4 import BeautifulSoup
import getdata
import commands
import collections


class Users:
   
    def __init__(self, name):
        """Instantiate user data to use with other methods"""
        self.name = name
        #self.email = email

    def search_user(self):
        """Search if an user name exist on Goddreads Database
        Parameters: self
        Return: url"""
        
        if getdata.page_main.status_code == 200: 
            print(f"The User {username.name} EXIST in GoodReads", 
            "Now get a few stats with the optional parameters [-AagTtbrsrlr]", 
            "EXAMPLE: 'heagma -a' to look for favorite Authors ", sep="\n") 
        else:
             print(f"The User {username.name} DOESN'T EXIST in GoodReads", "Please Try another User", sep="\n")#como puedes ver usamos name e email the lo instaciado arriba
        return self.name

    def get_all_stats(self):
        return True
    
    def get_authors(self):
        """Get the most read atuthors and how many books
        Return: Authors"""
        authors = []
        for author in getdata.parsed_read_shelf.find_all("td", class_="field author"):
            authors.append(author.get_text().strip("author").strip("*").strip("\n*").strip())
        most_read = collections.Counter(authors).most_common(3)
        print(f"The 3 most read Authors are:")
        for name, num in most_read:
            print(f"{name:{4}{2}}{num:{2}} Books"  )        
        return authors
    
    def get_genres(self):
        user = command.user
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

    

    

if __name__ == "__main__":
    command = commands.command_args
    username = Users(command.user)
    #no need at the moment ya que siendo posicionalargument es necesario para entrar otro argumetoopcional
    #if command_args.genre: #If we use Optional commands before --user 
    #    parser.print_help(sys.stderr) # Then print the error, print_help() is a verbose function 
    #    sys.exit(1)
    if command.user and len(sys.argv[:]) == 2: #To check if the user only input 1 argument (user) 
        username.search_user()
    elif command.user and command.genres:
        
        username.get_genres() #imprimimos los generos
    elif command.user and command.authors:
        username.get_authors()