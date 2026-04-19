# -------------------------------
# Exercise 3-4: Guest List
# Make a list of at least three people you’d like to invite to dinner.
# Print a message to each person, inviting them to dinner.
# -------------------------------

guests = ["Albert Einstein", "Nelson Mandela", "Ada Lovelace"]

for guest in guests:
    print(f"Dear {guest}, you are invited to dinner!")


# -------------------------------
# Exercise 3-5: Changing Guest List
# One guest can’t make it. Print their name.
# Replace them with a new guest.
# Print a new set of invitations.
# -------------------------------

print(f"Unfortunately, {guests[1]} can't make it to dinner.")  # Show who can't come
guests[1] = "Marie Curie"  # Replace guest

for guest in guests:
    print(f"Dear {guest}, you are invited to dinner!")  # Send new invites


# -------------------------------
# Exercise 3-6: More Guests
# Found a bigger table, so invite three more guests.
# Insert one at the beginning, one in the middle, and append one at the end.
# Print new invitations.
# -------------------------------

print("Good news! I found a bigger dinner table, so more guests can join.")

guests.insert(0, "Leonardo da Vinci")   # Add to beginning
guests.insert(2, "Isaac Newton")        # Add to middle
guests.append("Katherine Johnson")      # Add to end

for guest in guests:
    print(f"Dear {guest}, you are invited to dinner!")


# -------------------------------
# Exercise 3-7: Shrinking Guest List
# Bad news: only space for two guests.
# Pop guests until only two remain, apologizing each time.
# Print invitations for the two still invited.
# Delete the final two names to empty the list.
# -------------------------------

print("Bad news! The new table won't arrive, so I can only invite two people.")

while len(guests) > 2:
    removed_guest = guests.pop()  # Remove last guest
    print(f"Sorry {removed_guest}, I can't invite you to dinner.")  # Apology message

for guest in guests:
    print(f"Dear {guest}, you are still invited to dinner!")  # Confirm invite

del guests[:]  # Delete all names to empty the list
print("Final guest list:", guests)  # Should print []
