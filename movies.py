import easygui

movies = {
    'Sherk': {
        'Genre': ['Fatnasy', 'Animated', 'Romance'],
        'Year released': '2001',
        'Rating': '7/10',
        'Type': 'Movie'},
    
    'Cars': {
        'Genre': ['Comedy', 'Animated', 'Adventure'],
        'Year released': '2006',
        'Rating': '7/10',
        'Type': 'Movie'},
    
    'Kunfu Panda': {
        'Genre': ['Animated', 'Adventure', 'Action'],
        'Year released': '2008',
        'Rating': '7/10',
        'Type': 'Movie'},

    'Black Panther': {
        'Genre': ['Action', 'Adventure', 'Sci-Fi'],
        'Year released': '2018',
        'Rating': '7/10',
        'Type': 'Movie'}
}




def print_all():
    description = ''
    msg = ''
    for movie_title, movie_info in movies.items():
        description = ''
        for catergory in movie_info:
            description += (f'\n{catergory}: {movie_info[catergory]}')
        msg += (f'\n\n{movie_title} \n{description}') 
    easygui.msgbox(f'{msg}')


def movie_search():
    choices = []
    for film in movies:
        choices.append(film)
        msg = 'What movie would you like to check out?'
        title = 'All movies'
    user_pick = easygui.choicebox(msg, title, choices)
    msg_1 = ''
    for movie_title, movie_info in movies.items():
        if user_pick == movie_title:
            for catergory in movie_info:
                msg_1 += (f'\n{catergory}: {movie_info[catergory]}')
    easygui.msgbox(f'{user_pick}: \n{msg_1}')

def genre():
    genre = []
    choices = ['Sci-Fi', 'Adventure', 'Animated', 'Mystery',
                           'Romance', 'Drama', 'Action', 'Fantasy',
                           'comdey', 'Crime', 'Horror', 'Thriller']
    msg = 'What are the genres?'
    title = 'Genres'
    user_choice = easygui.multchoicebox(msg, title, choices)
    genre.append(user_choice)
    selection = {catergory: genre}
    movie_info.update(selection)

def release_date():
    msg = 'When was the movie released?'
    title = 'Year released'
    user_choice = easygui.integerbox(msg, title)
    selection = {catergory: user_choice}
    movie_info.update(selection)

def rating():
    msg = "What rating would you give it out of 10?"
    title = "Rating"
    option = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    user_choice = easygui.buttonbox(msg, title, option)
    selection = {catergory: user_choice/10}
    movie_info.update(selection)

def type():
    msg = 'Is it a movie or a Tv Series'
    title = 'Type'
    option = 'Movie', 'Tv Series'
    user_choice = easygui.choicebox(msg, title, option)
    selection = {catergory: user_choice}
    movie_info.update(selection)
    
def add_movie():
    global catergory
    global movie_info
    movie_info = {}
    
    message = 'What is the title of the movie?'
    name = 'Movie title'
    movie_title = easygui.enterbox(message, name)
    
    for movie_name, movie_detail in movies.items():
        for catergory in movie_detail:
            if catergory == 'Genre':
                genre()
            
            elif catergory == 'Year released':
                release_date()
            
            elif catergory == 'Rating':
                rating()
            
            elif catergory == "Type":
                type()
                
    movie_description = (f'\n{movie_info}')
    new_movie = {movie_title: movie_description}
    easygui.msgbox(new_movie)
    movies.update(new_movie)


  
            
def leave():
    easygui.msgbox("Goodbye")
    return "n"
    

options = {
    'Print all': print_all,
    'Search movie': movie_search,
    'Add movie': add_movie,
    'Exit': leave
    
}

get_input = "y"

while get_input != 'n':
    
    msg = 'What would you like to do?'
    title = 'Pick an option'
    
    choice = []
    for x in options:
        choice.append(x)

    selection = easygui.buttonbox(msg, title, choice)
    get_input = options[selection]()
