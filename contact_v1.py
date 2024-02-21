#search for certain day or certian subject from nested dic
#searching for certain subject will print out the day and period you have it
import easygui
timetable = {"1": 
                {"Period 1": "chemistry",
                 "Period 2": "biology",
                 "Period 3": "math",
                 "Period 4": "physics",
                 "Period 5": "english",
                 "Period 6": "dtp"},
            "2":
                {"Period 1": "biology",
                 "Period 2": "math",
                 "Period 3": "physics",
                 "Period 4": "english",
                 "Period 5": "dtp",
                 "Period 6": "chemistry"},
            "3":
                {"Period 1": "math",
                 "Period 2": "physics",
                 "Period 3": "english",
                 "Period 4": "dtp",
                 "Period 5": "chemistry",
                 "Period 6": "biology"},                 
            "4":
                {"Period 1": "physics",
                 "Period 2": "english",
                 "Period 3": "dTP",
                 "Period 4": "chemistry",
                 "Period 5": "biology",
                 "Period 6": "math"},
            "5":
                {"Period 1": "english",
                 "Period 2": "dtp",
                 "Period 3": "chemistry",
                 "Period 4": "biology",
                 "Period 5": "math",
                 "Period 6": "physics"},
            "6":
                {"Period 1": "dtp",
                 "Period 2": "chemistry",
                 "Period 3": "biology",
                 "Period 4": "math",
                 "Period 5": "physics",
                 "Period 6": "english"},}

def search_day():
   day = easygui.enterbox("Which day would you like to search for?")
   if day in timetable:
          schedule = '\n'.join([f"{period}: {subject}" for period , subject in timetable[day].items()])
          easygui.msgbox(f"schedule for day {day}: \n{schedule}")
   else:
        easygui.msgbox(f"Sorry Day {day} does not exist")

def search_subject():
     subject = easygui.buttonbox("Which subject would you like to search for?", title="search subject", choices = ["physics", "chemistry", "dtp", "english", "biology", "math"])
     if subject == "physics":
          print("hi")

          



choice = easygui.buttonbox("Would you like to search for a day or a subject?", choices = ["day", "subject"])
if choice == "day":
    search_day()

elif choice == "subject":
     search_subject()

for perod, sub in time 
     for  key value in sub