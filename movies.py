import easygui

movies = {
    'Sherk': {
        'Genre': ['Fatnasy', 'Animated', 'Romance'],
        'Year released': '2001',
        'Rating': '7/10',
        'Officebox profits': '$42M'},
    
    'Cars': {
        'Genre': ['Comedy', 'Animated', 'Adventure'],
        'Year released': '2006',
        'Rating': '7/10',
        'Officebox profits': '$1.4B'},
    
    'Kunfu Panda': {
        'Genre': ['Animated', 'Adventure', 'Action'],
        'Year released': '2008',
        'Rating': '7/10',
        'Officebox profits': '$60M'},

    'Black Panther': {
        'Genre': ['Action', 'Adventure', 'Sci-Fi'],
        'Year released': '2018',
        'Rating': '7/10',
        'Officebox profits': '$2B'}
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
    msg = ''
    for movie_title, movie_info in movies.items():
        if user_pick == movie_title:
            for catergory in movie_info:
                msg += (f'\n{catergory}: {movie_info[catergory]}')
    easygui.msgbox(f'{user_pick}: \n{msg}')


def add_movie():
    msg = 'What is the name of the movie?'
    title = 'Movie title'
    movie_title =  easygui.enterbox(msg,title)
    movies[movie_title] = {}

    msg = 'What is the genre of the movie?'
    title = 'Genre'
    choices = ['Sci-Fi', 'Adventure', 'Animated', 'Mystery',
                           'Romance', 'Drama', 'Action', 'Fantasy',
                           'comdey', 'Crime', 'Horror', 'Thriller']
    genre = easygui.multchoicebox(msg, title, choices)
    movies[movie_title][title] = genre

    msg = 'When what year was the movie released?'
    title = 'Year released'
    release_date = easygui.integerbox(msg, title, upperbound=2050)
    movies[movie_title][title] = release_date

    msg = 'What rating do you give this movie out of 10?'
    title = 'Rating'
    rating = easygui.integerbox(msg,title)
    movies[movie_title][title] = f'{rating}/10'

    msg = 'What is the Officebox profits for this movie? (In millions)'
    title = 'Officebox profits'
    officebox = easygui.enterbox(msg, title)
    movies[movie_title][title] = f'${officebox}M'

    msg = ''
    for movie_title, movie_info in movies.items():
        for catergory in movie_info:
            msg += (f'\n{catergory}: {movie_info[catergory]}')
    txt = f'{movie_title}: \n{msg} \n\n Please confirm your movie'
    title = ''
    choice = 'Yes', "No"
    user_pick = easygui.buttonbox(txt, title, choice)




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
