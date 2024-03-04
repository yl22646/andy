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
    msg_1 = ''
    
    #This for loop will get the movie that the user has picked and will
    #print out the movie's information
    for movie_title, movie_info in movies.items():
        if user_pick == movie_title:
            for catergory in movie_info:
                msg_1 += (f'\n{catergory}: {movie_info[catergory]}')
    easygui.msgbox(f'{user_pick}: \n{msg_1}')


def leave():
    '''This function will exit the program when called'''
    easygui.msgbox("Goodbye")
    return "n"
    
#list of actions the user is able to preform
options = {
    'Print all': print_all,
    'Search movie': movie_search,
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
