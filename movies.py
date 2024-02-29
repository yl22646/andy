import easygui

movies = {
    'Sherk': {
        'Genre': ['Fatnasy', 'Animated', 'Romance'],
        'Year released': '18 May 2001',
        'IMDB rating': '7.9/10',
        'Type': 'Movie'},
    
    'Cars': {
        'Genre': ['Comedy', 'Animated', 'Adventure'],
        'Year released': '9 June 2006',
        'IMDB rating': '7.2/10',
        'Type': 'Movie'},
    
    'Kunfu Panda': {
        'Genre': ['Animated', 'Adventure', 'Action'],
        'Year released': '26 June 2008',
        'IMDB rating': '7.6/10',
        'Type': 'Movie'},

    'Black Panther': {
        'Genre': ['Action', 'Adventure', 'Sci-Fi'],
        'Year released': '16 February 2018',
        'IMDB rating': '7.3/10',
        'Type': 'Movie'}
}

def print_all():
    choices = []
    for film in movies:
        choices.append(film)
        msg = 'What movie would you like to check out?'
        title = 'All movies'
    easygui.multchoicebox(msg, title, choices)
    
def movie_search():
    while True:
        y = []

def leave():
    easygui.msgbox("Goodbye")
    return "n"
    

options = {
    'Print all': print_all,
    'Search movie': movie_search,
    'Exit': leave,
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
