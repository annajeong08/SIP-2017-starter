start = '''
"You wake up one morning and find that all of your family members are dead. You are then transported into the middle of an enchanted forest. A wizard appears and says,"Child, the evil witch has slaughtered your family. I was only able to protect you." You have the choice of seeking revenge or being with your family.""
'''
print(start)


validInput = False
while validInput == False:
    print("Type 'revenge' to seek revenge or 'give up' to die.")
    user_input = input()

    if user_input == "revenge":
        validInput = True
        print("You've decided to seek revenge!...")

    elif user_input == "give up":
        validInput = True
        print("You have chosen to die.")
        exit()

validInput = False
while validInput == False:
    print("You've encountered two animals! Choose a companion to take with you on your journey! Type 'bear' to choose the bear or 'snake' to choose the snake")
    user_input = input()

    if user_input == "snake":
        validInput = True
        print("Nice choice! This snake has the ability to sense evil lurking in the enchanted forest!")

    elif user_input == "bear":
        validInput = True
        print("Oh no! You have chosen to trust a hungry bear. Goodbye.")
        exit()

validInput = False
while validInput == False:
    print("Choose a name for your snake! Type 'M' for a name starting with M or type 'F' for a name starting with F.")
    user_input = input()
    if user_input == "M":
        validInput = True
        import random
        M_names = ["Your snake's name is Marco.", "Your snake's name is Miles.", "Your snake's name is Max."]
        print(random.choice(M_names))

    if user_input == "F":
        validInput = True
        import random
        F_names = ["Your snake's name is Fiona.", "Your snake's name is Franco.", "Your snake's name is Ferrari."]
        print(random.choice(F_names))


validInput = False
while validInput == False:
    print("Your snake starts to talk! He says he smells the nasty odor of the witch! Try to understand what the snake is saying! It seems that he is trying to point at a direction... Type 'left' to go left or 'right' to go right")
    user_input = input()
    if user_input == "right":
        validInput = True
        print("Nice! You guys have a natural connection!")

    elif user_input == "left":
        validInput = True
        print("Yikes! You've misinterpreted the snake and now you are falling down a bottomless hole! Goodbye!")
        exit()

validInput = False
while validInput == False:
    print("Type 'high five' to high five your snake!")
    user_input = input()
    if user_input == "high five":
            validInput = True
            print("Now, it's time to cross the bridge of fairies! The wizard appears again and tells you that you are close!")

validInput = False
while validInput == False:
    print("Type 'waterbreak' for a waterbreak or type 'go on' to go on.")
    user_input = input()
    if user_input == "go on":
        validInput = True
        print("Wow, you're determined, aren't you?")
    elif user_input == "waterbreak":
        validInput = True
        print("Oh no! The evil witch poisoned the water! Adios!")
        exit()

validInput = False
while validInput == False:
    print("Well, congratulations my friend. You are wise and determined. But you've been fooled. Seeking revenge is not moral. Good bye.")
    exit()
