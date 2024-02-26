import easygui

bakery = {'Savouries':
            {'mice and cheese pie': 5,
             'wrap': 5,
             'pizza': 5,
             'sausage roll': 4,
             'spinich feta quiche': 6},
          
          'Sandwiches':
            {'ham and cheese': 6,
             'roast beef': 6,
             'blt': '$7',
             'egg salad': 6,
             'vegetarian': 5},
          
          'Sweets':
            {'chocolate cake': 4,
             'lamington': 4,
             'muffin': 4,
             'pain un chocola': 4,
             'danish': 4},

          'Drinks':
            {'coffee': 6,
             'hot chocolate': 5,
             'soft drink': 3,
             'juice': 2,
             'smoothie': 5},
            
          'Miscellaneous':
            {'donut': 4,
             'stir fried rice': '$6', 
             'tomato suace': '$4',
             'crossant': '$4',
             'curry': '$7'}}

def print_menu():
  menu = ''
  shop = ''
  for catergory, food in bakery.items():
    menu = ''
    for price in food:
      menu += (f'\n{price}: {food[price]}')
    shop += (f'\n\n{catergory} \n{menu}') 
  easygui.msgbox(f'{shop}')

def search_menu():
  catgor = easygui.buttonbox('which catergory would you like to look through'
  , title="pick catergory"
  , choices=['Savouries', 'Sandwiches', 'Sweets', 'Drinks', 'Miscellaneous'])
  menu = ''
  for i, food in bakery.items():
    if i == catgor:
      for price in food:
        menu += (f'\n{price}: {food[price]}')
  easygui.msgbox(f'{catgor}: \n{menu}')

def search_item():
  menu = []
  check = []
  for category, food in bakery.items():
    for foods, price in food.items():
      menu.append(foods)
  cart = easygui.multchoicebox(f'bakery items', choices= menu)
  for category, food in bakery.items():
    for price in food:
      print(food[price])
      check.append(food[price])
  checkout = sum(check)
  easygui.msgbox(f'Your total is ${checkout}')
  

  
choice = easygui.buttonbox('''would you like the whole menu list 
or would you like to search through the menu?'''
, choices=["print menu", "search menu", "search_item"])
if choice == 'print menu':
  print_menu()
elif choice == 'search menu':
  search_menu()
elif choice == 'search_item':
  search_item()
