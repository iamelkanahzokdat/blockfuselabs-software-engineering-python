"""
Add guests to a party invite list, with optional special notes for VIP's.

Parameters:
invites: The existing list of invited guests.
guests: Any number of guest names (strings).
special_notes: Key-value pairs where the key is the guest name and the value is a special note.

Example:
    invites = []
    invited_guests(invites, "John", "Mary", Peter="Needs wheelchair access")
"""

invites = []
def invited_guests(invites, *guests, **special_notes):
    for guest in guests:
        invites.append(guest)
    for guest, note in special_notes.items():
        if guest in invites:
            print(f"Note for {guest}: {note}")
        else:
            invites.append(guest)
            print(f"Note for {guest}: {note}")
    return invites

invited_guests(invites, "John", "Mary", Peter="Needs wheelchair access")
print(invites) 


'''
invite_list = []
def invited_guests(invites, *guests, **special_notes):
    invite_list.extend(guests)
    invite_list.extend(special_notes)

invited_guests(invite_list, "John", "Mary", Peter="Needs wheelchair access")
print(invite_list) 

'''