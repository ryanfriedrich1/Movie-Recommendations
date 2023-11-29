# TreeNode Class
class TreeNode:
    def __init__(self, genre):
        self.genre = genre
        self.movies = []

    def add_child(self, node):
        self.movies.append(node)

    def recommendation(self):
        loop = True
        while loop:   
            print("What genre of movie would you like to watch?")
            userInput = input("Type the beginning of that genre and press enter so see movie recommendations\n")
            genres = autoComplete(userInput.lower())
            while len(genres) > 1:
                print("With those beginning letters your choices are: ")
                for x in genres:
                    print(x.genre)
                userInput = input("What genre of movie do you want to watch?\n")
                genres = autoComplete(userInput.lower())
            userInput = input("The only option with those beginning letters is {0}. Do you want to look at {0} movies? Enter (y/n): ".format(genres[0].genre))
            if userInput.lower() == "y":
                print("Genre | Title | Release date | rotten tomato score | movie length")
                for x in genres[0].movies:
                    print(x)
            userInput = input("Would you like to search for more movie recommendations? Enter (y/n): ")
            if userInput.lower() == "n":
                loop = False
        print("Thank you for using Movie Recommendations V1.0!")

def autoComplete(input):
    genreAutoComplete = []
    for x in movieGenres:
        if x.genre.startswith(input):
            genreAutoComplete.append(x)
    return genreAutoComplete

movieGenres = [TreeNode("action"), TreeNode("adventure"), TreeNode("comedy"), TreeNode("horror"), TreeNode("romance"), TreeNode("sci-fi"), TreeNode("history"), TreeNode("holiday"), TreeNode("documentary")]

# genre, movie title, release date, audience score, movie length
movieData = [["Action", "The Killer", "November 10 2023", "59%", "1h 58m"],
             ["Action", "The Creator", "November 14 2023", "76%", "2h 12m"],
             ["Action", "Blue Beetle", "September 26 2023", "91%", "2h 7m"],
             ["Action", "The Hunger Games", "September 9 2016", "81%", "2h 22m"],
             ["Action", "Mission: Impossible - Dead Reckoning, Part One", "October 10 2023", "94%", "2h 43m"],
             ["Adventure", "The Wonderful Story of Genry Sugar", "September 27 2023", "81%", "39m"],
             ["Adventure", "A Walk In The Woods", "October 11 2016", "48%", "1h 44m"],
             ["Adventure", "Interstellar", "May 24 2016", "86%", "2h 45m"],
             ["Adventure", "Triple Frontier", "March 15 2019", "58%", "2h 5m"],
             ["Adventure", "Dune", "October 22 2021", "90%", "2h 35m"],
             ["Comedy", "The Holdovers", "November 28 2023", "90%", "2h 13m"],
             ["Comedy", "Good Buger 2", "November 22 2023", "73%", "1h 30m"],
             ["Comedy", "Mad Cats", "November 21 2023", "82%", "1h 27m"],
             ["Comedy", "Genie", "November 22 2023", "67%", "1h 32m"],
             ["Comedy", "Barbie", "September 13 2023", "83%" , "1h 54m"],
             ["Horror", "Five Nights at Freddy's", "October 27 2023", "87%", "1h 50m"],
             ["Horror", "When Evil Lurks", "October 27 2023", "80%", "1h 39m"],
             ["Horror", "Talk to Me", "September 12 2023", "82%", "1h 35m"],
             ["Horror", "The Jester", "October 3 2023", "35%", "1h 30m"],
             ["Horror", "Saw X", "October 20 2023", "89%", "1h 58m"],
             ["Romance", "May December", "December 1 2023", "93%", "1h 53m"],
             ["Romance", "Best Christmas Ever", "November 16 2023", "19%", "1h 20m"],
             ["Romance", "No Hard Feelings", "August 15 2023", "87%", "1h 43m"],
             ["Romance", "Past Lives", "August 22 2023", "92%", "1h 46m"],
             ["Romance", "Fifty Shades of Grey", "January 5 2016", "2h 5m"],
             ["Sci-fi", "The Creator", "November 14 2023", "76%", "2h 12m"],
             ["Sci-fi", "Quantum Cowboys", "November 14 2023", "92%", "1h 39m"],
             ["Sci-fi", "Prometheus", "March 1 2013", "68%", "2h 3m"],
             ["Sci-fi", "Interstellar", "May 24 2016", "86%", "2h 45m"],
             ["Sci-fi", "The Hunger Games", "September 9 2016", "81%", "2h 22m"],
             ["History", "Oppenheimer" , "November 21 2023", "91%", "3h 0m"],
             ["History", "Gladiator", "June 15 2011", "87%", "2h 34m"],
             ["History", "Schindler's List", "March 5 2013", "97%", "3h 15m"],
             ["History", "All Quiet On The Western Front", "October 28 2022", "90%", "2h 28m"],
             ["History", "Titanic", "June 1 2014", "69%", "3h 15m"],
             ["Holiday", "The Holdovers" ,"November 28 2023", "90%", "2h 13m"],
             ["Holiday", "Genie", "November 22 2023", "67%", "1h 32m"],
             ["Holiday", "Best Christmas Ever", "November 16 2023", "19%", "1h 20m"],
             ["Holiday", "How The Grinch Stole Christmas", "Dec 1 2015", "58%", "1h 45m"],
             ["Holiday", "Spirited", "November 18 2022", "81%", "2h 7m"],
             ["Documentary", "Stamped From The Beginning", "November 20 2023", "67%", "1h 31m"],
             ["Documentary", "Mister Organ", "November 21 2023", "92%", "1h 36m"],
             ["Documentary", "Bye Bye Barry", "November 21 2023", "98%", "1h 32m"],
             ["Documentary", "Omoiyari: A Song Fily By Skishi Bashi", "November 21 2023", "93%", "1h 33m"],
             ["Documentary", "American Symphony", "November 29 2023", "80%", "1h 40m"],]

# setting up tree structure
# each genre is a tree branch with the 5 movies in the genre as its children
for x in range(len(movieGenres)):
   counter = x * 5
   for y in range(5):
       movieGenres[x].add_child(movieData[counter + y])

movieGenres[0].recommendation()

