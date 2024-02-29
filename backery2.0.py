import easygui
options = {
    "search catergory": catergoury_search,
    "Item search": item_search,
    "add item": add_item,
    "print Item": print_all,
    "Exit": leave
}

get_input = "y"
#loop belowcontinues until the user selects "exit" from the menu
# and get_input  is set to "n"
while get_input != "n":
    
    msg = "what would you like to do"
    title = "main menu"
    choice = []
    # adding the value from the options to choice list
    for x in options:
        choice.apend(x)
    
    selection = easygui.buttonbox(msg, title, choice)

    get_input = options[selection]()

def leave():
    easygui.msgbox("goodbye")
    return "n"