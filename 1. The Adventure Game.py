# Task 1: Code Correction
place = input("Choose a place: forest or cave? ").lower()  # Converts input to lowercase for consistency

if place == "forest":
    action = input("climb a tree or cross a river? ").lower()
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        print("Invalid action. Please choose 'climb a tree' or 'cross a river'.")
elif place == "cave":
    print("You find a hidden treasure!")
else:
    print("Invalid place. Please choose 'forest' or 'cave'.")

