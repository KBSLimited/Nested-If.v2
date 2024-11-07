# Task 1: Code Correction
attendees = int(input("Enter number of attendees: "))  
venue = "large hall" if attendees > 100 else "conference room"
print(f"Venue selected: {venue}")