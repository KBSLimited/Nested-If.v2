# Task 1: Code Correction
attendees = int(input("Enter number of attendees: "))  
venue = "large hall" if attendees > 100 else "conference room"
print(f"Venue selected: {venue}")

# Task 2: Venue Selection
attendees = int(input("Enter number of attendees: "))  
venue = "large hall" if attendees > 100 else "conference room"
additional_facilities = []

if attendees > 50:
    additional_facilities.append("audio system")
if attendees > 80:
    additional_facilities.append("projector")

# Output results
print(f"Venue selected: {venue}")
if additional_facilities:
    print("Recommended additional facilities:", ", ".join(additional_facilities))