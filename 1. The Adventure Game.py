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

# Task 2: Setting the Scene
place = input("Choose a place: forest or cave? ").lower()  # Standardize input

if place == "forest":
    action = input("climb a tree or cross a river? ").lower()
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        print("Invalid action. Please choose 'climb a tree' or 'cross a river'.")
elif place == "cave":
    action = input("light a torch or proceed in the dark? ").lower()
    if action == "light a torch":
        print("You can see a path leading deeper into the cave.")
    elif action == "proceed in the dark":
        print("You stumble in the darkness and find nothing.")
    else:
        print("Invalid action. Please choose 'light a torch' or 'proceed in the dark'.")
else:
    print("Invalid place. Please choose 'forest' or 'cave'.") 

# Task 3: Default Path
place = input("Choose a place: forest or cave? ").lower()  # Convert to lowercase for consistency

if place == "forest":
    action = input("climb a tree or cross a river? ").lower()
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        print("Invalid action. Please choose 'climb a tree' or 'cross a river'.")
elif place == "cave":
    action = input("light a torch or proceed in the dark? ").lower()
    if action == "light a torch":
        print("You can see a path leading deeper into the cave.")
    elif action == "proceed in the dark":
        print("You stumble in the darkness and find nothing.")
    else:
        print("Invalid action. Please choose 'light a torch' or 'proceed in the dark'.")
else:
    print("Invalid place. Please choose 'forest' or 'cave'.")