import easygui

bakery = {'Savouries':
            {'mice and cheese pie': '$5',
             'wrap': '$5',
             'pizza': '$5',
             'sausage roll': '$4',
             'spinich feta quiche': '$6'},
          
          'Sandwiches':
            {'ham and cheese': '$6',
             'roast beef': '$6',
             'blt': '$7',
             'egg salad': '$6',
             'vegetarian': '$5'},
          
          'sweets':
            {'chocolate cake': '$4',
             'lamington': '$4',
             'muffin': '$4',
             'pain un chocola': "$4",
             'danish': "$4"},

          'drinks':
            {'coffee': '$6',
             'hot chocolate': '$5',
             'soft drink': '$3',
             'juice': '$2',
             'smoothie': '$5'},
            
          'miscellaneous':
            {'donut': '$4',
             'stir fried rice': '$6',
             'tomato suace': '$4',
             'crossant': '$4',
             'curry': '$7'}}

def print_menu():
    

choice = easygui.buttonbox("would you like the whole menu list or would you like to search through the menu", choices=["print menu", "search menu"])
if choice == 'print menu':
    print_menu()
