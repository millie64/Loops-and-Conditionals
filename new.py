


def smart_assistant():
    name = input("What's your name? ")
    mood = input("How are you feeling today?(happy/sad/tired/excited) ").strip().lower()
    if mood == "happy":
        print(f"That's awesome {name}, keep spreading good vibes!")
    elif mood == "sad":
        print(f"I'm here for you {name}, tomorrow will be better.")
    elif mood == "tired":
        print(f"Get some rest {name}, you deserve it.")
    elif mood == "excited":
        print(f"Woohoo! {name}! What's making you excited? ")
    else:
        print(f"Got it, {name}, I hope you had a great day.")
smart_assistant()

def qualifications(ID, birth_certificate):
    if ID:
        if birth_certificate:
            print("You are hired")
        else:
            print("You are shortlisted")
    else:
        print("Go home.")
identity = input("Do you have ID? (yes/no)") == "yes"
nationality = input("Do you have birth certificate? (yes/no)") == "yes"
qualifications(identity, nationality)



def voters_registration(age, good_conduct):
    if age >=18:
        if good_conduct:
            print("You are registered!")
        else:
            print("You need good-coduct")
    else:
        print("You are too young.")
requirements = int(input("How old are you? "))
another = input("Do you have good_conduct? (yes/no)") == "yes"
      
voters_registration(requirements, another)


def square(i):
    return i * i
result = square(6)
print(result)


def make_sentence(p, f):
    return p  + " is " + f
sentence = make_sentence("power" , "fab")
print(sentence)

def check_even_odd():
    a = int(input("What's a? "))
    b = int(input("What's b? "))
    if a % 2 == 0:
        print(str(a) + " is even ")
    else:
         print(str(a) + " is odd")   
    if b % 2 != 0:
        print(str(b) + " is odd") 
    else:
        print(str(b) + " is even")
check_even_odd()
