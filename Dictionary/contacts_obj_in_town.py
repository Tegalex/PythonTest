contacts_obj = [
  {"first_name": "Alexander",
   "last_name": "Coder",
   "phone": 5551763,
   "town": "Kingston"},
  {"first_name": "Michael",
   "last_name": "Jordan",
   "phone": 5558722,
    "town": "Chicago"},
  {"first_name": "Elaine",
   "last_name": "Benes",
   "phone": 5551915,
   "town": "New York"},
  {"first_name": "Tobias",
   "last_name": "Fünke",
   "phone": 5556742,
   "town": "Newport Beach"},
]

user_input = input("enter a last name: ")
for contact in contacts_obj:
    if contact["last_name"].lower() == user_input.lower():
        print("{0} {1} ({2}): {3}".format(contact["first_name"], contact["last_name"], contact["town"], contact["phone"]))
        
        

valid_keys = []
for key in contacts_obj[0].keys():
    valid_keys.append(key)
key_choice = ""
while key_choice != "quit":
    print("Available searches: {0}".format(valid_keys))
    key_choice = input("Enter the type of search you would like to perform, or type quit: ")
    if key_choice in valid_keys:
        value_choice = input("Enter the value you would like to search for: ")
        for contact in contacts_obj:
            if str(contact[key_choice]).lower() == value_choice.lower():
                print("{0} {1} ({2}): {3}".format(
                contact["first_name"], contact["last_name"],
                contact["town"], contact["phone"]))