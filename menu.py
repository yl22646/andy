import easygui

menu = {"Value" : {
    "Beef Burger" : 5.69,
    "Fries" : 1.00,
    "Fizzy Drink" : 1.00,},
        
        "Cheezy" : {
    "Cheese Buger" : 6.69,
    "Fries" : 1.00,
    "Fizzy Drink" : 1.00},
    
        "Super" : {
    "Cheese Burger" : 6.69,
    "Large Fries" : 2.00,
    "Smoothie" : 2.00}}

def print_all():
    '''When called this function will print all combos and it's information
    on easygui'''
    output = ''
    total_price = []
    msg = ''
    
    for combo_name, combo_info in menu.items():
        output = ''
        for price in combo_info:
            total_price.append(combo_info[price])
            output += (f'\n{price}: ${combo_info[price]: .2f}')
        add_total = sum(total_price)
        msg += (f'\n\n{combo_name} \n{output} \n${add_total: .2f}') 
    easygui.msgbox(f'{msg}')    
 
print_all()

def movie_search():
    '''When called this function will allow the user to pick a movie and it 
    will print all information of that movie'''
    choices = []
    
    for combo in menu:
        choices.append(combo)
        msg = 'What combo would you like to check out?'
        title = 'All Combos '
    user_pick = easygui.choicebox(msg, title, choices)
    
    msg = ''
    for movie_title, movie_info in menu.items():
        if user_pick == movie_title:
            for catergory in movie_info:
                msg += (f'\n{catergory}: {movie_info[catergory]}')
    easygui.msgbox(f'{user_pick}: \n{msg}')