#search for certain day or certian subject from nested dic
#searching for certain subject will print out the day and period you have it
import easygui
timetable = {"1": 
                {" 1": "Chemistry",
                 " 2": "Biology",
                 " 3": "Math",
                 " 4": "Physics",
                 " 5": "English",
                 " 6": "DTP"},
            "2":
                {"1": "Biology",
                 "2": "Math",
                 "3": "Physics",
                 "4": "English",
                 "5": "DTP",
                 "6": "Chemistry"},
            "3":
                {"1": "Math",
                 "2": "Physics",
                 "3": "English",
                 "4": "DTP",
                 "5": "Chemistry",
                 "6": "Biology"},                 
            "4":
                {"1": "Physics",
                 "2": "English",
                 "3": "DTP",
                 "4": "Chemistry",
                 "5": "Biology",
                 "6": "Math"},
            "5":
                {"1": "English",
                 "2": "DTP",
                 "3": "Chemistry",
                 "4": "Biology",
                 "5": "Math",
                 "6": "Physics"},
            "6":
                {"1": "DTP",
                 "2": "Chemistry",
                 "3": "Biology",
                 "4": "Math",
                 "5": "Physics",
                 "6": "English"},}


choice = easygui.buttonbox("Would you like to search for a day or a subject?", choices = ["day", "subject"])
if choice == "day":
   search_day = easygui.integerbox("Which day would you like to search for?")
   for i in timetable:
        if search_day == i:
            easygui.msgbox(i)
#    if search_day in timetable:
#         print(timetable[search_day])
   else:
        easygui.msgbox(f"Sorry Day {search_day} does not exist")
