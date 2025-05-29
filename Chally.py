for n in range(5):
    print("i")

def days():
    today = input("What's the day today? ").strip().title()
    match today:
        case "Saturday" | "Sunday":
            print("Weekend")
        case "Monday"|"Tuesday"|"Wednesday"|"Thusday"|"Friday":
            print("Weekday")
        case _:
            print("Invalid day")
days()



def verification():
    visa = input("Do you have a visa? (yes/no)").strip().lower() == "yes"
    passport = input("Do you ave a passport? (yes/no)").strip().lower() == "yes"
    if visa and passport:
        print("You can travel.")
    else:
        print("You need both a visa and a passport to travel")
verification()

def documents ():
    dl = input("Do you have your driving licene? (yes/no)").strip().lower() == "yes"
    id = input("Do you have your Id? ").strip().lower() == "yes"
    if id:
        if dl:
            print("You can drive.")
    else:
        print("You need your documents.")
documents()