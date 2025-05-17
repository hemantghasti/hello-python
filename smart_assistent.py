# Simple AI Assistant
name = input("What's your name? ")
mood = input("How are you feeling today? (happy/sad/angry): ")

if mood == "happy":
    print("That's awesome, " + name + "! Keep smiling and leading!")
elif mood == "sad":
    print("Stay strong, " + name + ". Every CEO has bad days. Keep going.")
elif mood == "angry":
    print("Take a deep breath, " + name + ". Use that fire to solve problems!")
else:
    print("Thank you for sharing. Let's keep growing today!")
