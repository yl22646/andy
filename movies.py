import easygui

# Dictionary for movies
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
        'Officebox profits': '$2B'},

    'Lorax': {

        'Genre': ['Fatnasy', 'Animated', 'Romance'],
        'Year released': '2001',
        'Rating': '7/10',
        'Officebox profits': '$42M'},

    'Cars 2': {

        'Genre': ['Comedy', 'Animated', 'Adventure'],
        'Year released': '2006',
        'Rating': '7/10',
        'Officebox profits': '$1.4B'},
    
    'The Grinch': {

        'Genre': ['Animated', 'Adventure', 'Action'],
        'Year released': '2008',
        'Rating': '7/10',
        'Officebox profits': '$60M'},

    'Black Panther': {
        'Genre': ['Action', 'Adventure', 'Sci-Fi'],
        'Year released': '2018',
        'Rating': '7/10',
        'Officebox profits': '$2B'}, 

    'Thor': {
        'Genre': ['Action', 'Adventure', 'Sci-Fi'],
        'Year released': '2018',
        'Rating': '7/10',
        'Officebox profits': '$2B'}

}




def print_all():
    '''When called this function will print all movies and it's information
    on easygui'''
    description = ''
    msg = ''
    #This for loop will take all values in the dictionary and add to a new list
    #which will print neatly
    for movie_title, movie_info in movies.items():
        description = ''
        for catergory in movie_info:
            description += (f'\n{catergory}: {movie_info[catergory]}')
        msg += (f'\n\n{movie_title} \n{description}') 
    easygui.msgbox(f'{msg}')


def movie_search():
    '''When called this function will allow the user to pick a movie and it 
    will print all information of that movie'''
    choices = []
    
    #This for loop will gather all movies in the dictionary and print out
    #for the user to pick
    for film in movies:
        choices.append(film)
        msg = 'What movie would you like to check out?'
        title = 'All movies'
    user_pick = easygui.choicebox(msg, title, choices)
    
    #This for loop will get the movie that the user has picked and will
    #print out the movie's information
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
    for movie_name, movie_info in movies.items():
        if movie_name == movie_title:
            for catergory in movie_info:
                msg += (f'\n{catergory}: {movie_info[catergory]}')
    txt = f'{movie_title}: \n{msg} \n\nPlease confirm your movie'
    title = ''
    choice = 'Yes', "No"
    user_pick = easygui.buttonbox(txt, title, choice)
    #if user_pick == 'No':


def delete_movie():
    choices = []
    for film in movies:
        choices.append(film)
        msg = 'Which movie would you like to delete?'
        title = 'All movies'
    user_pick = easygui.choicebox(msg, title, choices)
    if user_pick in movies:
        del movies[user_pick]


def edit():
    output = ''
    movie_title = []
    movie_info = []

    for title in movies:
        movie_title.append(title)

    msg = 'choose what movie you would like to edit'
    title = ' Edit movie'

    movie_choice = easygui.choicebox(msg,title, movie_title)

    for info in movies[movie_choice]:
        movie_info.append(info)

    msg = f'wwhich aspect of {movie_choice} ot edit'
    title=''
    edit_choice = easygui.buttonbox(msg,title,movie_info)
        
    msg = 'what y change it to'
    movies[movie_choice[edit_choice]] = easygui.enterbox(msg)


def leave():
    '''This function will exit the program when called'''
    easygui.msgbox("Goodbye")
    return "n"
    
#list of actions the user is able to preform
options = {
    'Print all': print_all,
    'Search movie': movie_search,
    'Add movie': add_movie,
    'Delete movie': delete_movie,
    'Edit movie': edit,
    'Exit': leave
}

get_input = "y"

#This loop is the main menu which allows the user to preform actions and 
#will call the functions
while get_input != 'n':
    
    msg = 'What would you like to do?'
    title = 'Pick an option'
    
    choice = []
    for x in options:
        choice.append(x)

    selection = easygui.buttonbox(msg, title, choice)
    get_input = options[selection]()
