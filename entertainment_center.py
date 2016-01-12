import fresh_tomatoes
import media


#creates multiple instances of the class
#Media to represent a list of favorite movies
the_aristocats=media.Movie(
        "The Aristocats",
        "1970",                          
		"the story of 4 aristocratic cats kidnapped and brought home by a stray cat",
		"http://fffmovieposters.com/wp-content/uploads/17431-275x413.jpg",
		"https://www.youtube.com/watch?v=223bYlLJSnU")

the_never_ending_story=media.Movie(
        "The NeverEnding Story",
        "1984",  
		"the story of a boy and a magical book that brings him to the land of Fantasy",
		"http://fffmovieposters.com/wp-content/uploads/31543-275x414.jpg",
		"https://www.youtube.com/watch?v=qWcHO86w1MA")

labyrinth=media.Movie(
        "Labyrinth",
        "1986",  
		"the story of a girl that challenges the Goblin king to get her brother home",
		"http://fffmovieposters.com/wp-content/uploads/4706.jpg",
		"https://www.youtube.com/watch?v=G6C2p6H4TQ8")

the_cutting_edge=media.Movie(
        "The Cutting Edge",
        "1992",  
		"the love story between two ice skaters",
        "http://fffmovieposters.com/wp-content/uploads/20811-275x411.jpg",
  		"https://www.youtube.com/watch?v=QratAk_OUuc")

braveheart=media.Movie(
        "Braveheart",
        "1995",
        "the story of Scottish hero William Wallace",
		"http://fffmovieposters.com/wp-content/uploads/09948-275x405.jpg",
		"https://www.youtube.com/watch?v=1cnoM8EiGGU")

star_wars=media.Movie(
        "Star wars",
        "1977",  
		"the space battle of the rebels against the Empire",
		"http://fffmovieposters.com/wp-content/uploads/11670-275x414.jpg",
		"https://www.youtube.com/watch?v=vZ734NWnAHA")

#define the list of movies to show on the web page
movies=[the_aristocats,the_never_ending_story,labyrinth,the_cutting_edge,
        braveheart,star_wars] 

#call the function open_movies_page for the list of movies
fresh_tomatoes.open_movies_page(movies)     
