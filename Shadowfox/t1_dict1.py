# List of friends
friends = ["Aditya", "Sai Surya", "Mahi", "Vijay", "Santhi"]

# Create list of tuples with name and length
name_lengths = []
for friend in friends:
    name_lengths.append((friend, len(friend)))

print("Friend names with their lengths:")
print(name_lengths)
