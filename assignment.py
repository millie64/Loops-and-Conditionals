i = 0
while i < 3:
    print("Meow")
    i += 1

for i in range(50):
        print(i)

def election():
    ward = input("Which ward do you come from? ").strip().title()
    match ward:
        case "Kasarani":
            print("Your MCA is Mary")
        case "Githurai":
            print("Your MCA is Ken")
        case "Kinoo":
            print("Your MCA is Jalas")
        case _:
            print("Not valid.")
election()

 
def main():
    def score():
        results = int(input("What did you score? "))
        if results >= 90:
             print("A")
        elif results >=80:
            print("B")
        elif results >= 70:
            print("B")
        else:
            print("F")
    score()
main()

def smart_assistant():
    mood = input("How are you feeling today? ").strip().lower()
    if mood == "tired" or  mood == "sad":
        print("Get some rest")
    else:
         print("Why so?")
         respnse = input("How can I be of help? ")
smart_assistant()