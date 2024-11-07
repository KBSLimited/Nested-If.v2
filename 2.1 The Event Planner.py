# Complete Code: Venue, Facilities, and Catering Choices

# Get the number of attendees
attendees = int(input("Enter number of attendees: "))  

# Select venue based on the number of attendees
venue = "large hall" if attendees > 100 else "conference room"

# Initialize list for additional facilities
additional_facilities = []

# Recommend additional facilities based on attendees
if attendees > 50:
    additional_facilities.append("audio system")
if attendees > 80:
    additional_facilities.append("projector")

# Output venue and additional facilities
print(f"Venue selected: {venue}")
if additional_facilities:
    print("Recommended additional facilities:", ", ".join(additional_facilities))

# Ask for catering preferences
vegetarian_choice = input("Do you want vegetarian food? (yes/no): ").strip().lower()

# Recommend caterers based on food preference
if vegetarian_choice == "yes":
    print("We recommend Veggie Delight Caterers for vegetarian food.")
else:
    print("We recommend Gourmet Meals Caterers for non-vegetarian food.")