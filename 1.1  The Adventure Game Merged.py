# Merged Tasks: Code Correction, Setting the Scene, and Default Path

# Step 1: Choose a place
place = input("Choose a place: forest or cave? ").lower()  # Standardize input to lowercase

if place == "forest":
    # Task 1 and Task 2: Action options in the forest
    action = input("climb a tree or cross a river? ").lower()
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        print("Invalid action. Please choose 'climb a tree' or 'cross a river'.")
elif place == "cave":
    # Task 2 and Task 3: Action options in the cave
    action = input("light a torch or proceed in the dark? ").lower()
    if action == "light a torch":
        print("You can see a path leading deeper into the cave.")
    elif action == "proceed in the dark":
        print("You stumble in the darkness and find nothing.")
    else:
        print("Invalid action. Please choose 'light a torch' or 'proceed in the dark'.")
else:
    print("Invalid place. Please choose 'forest' or 'cave'.")