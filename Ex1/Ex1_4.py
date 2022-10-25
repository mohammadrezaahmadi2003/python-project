days = ("monday", "tuesday", "wednesday","thursday", "friday", "saturday", "sunday")
number = int(input("please enter the number(1-7)"))
if number:
    print(days[number-1])
else:
    print("error")
#int -> str
#help: you enter the number in the specified range(1-7) and then one of the days of the week that related to that number will display
