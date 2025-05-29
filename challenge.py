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
