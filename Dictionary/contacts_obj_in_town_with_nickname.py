contacts_obj = {
    "alexander": {"first_name": "Alexander",
     "last_name": "Coder",
     "phone": 5551763,
     "town": "Kingston"},
    "mike": {"first_name": "Michael",
     "cell_phone": 5559955},
    "laney": {"first_name": "Elaine",
     "last_name": "Benes"},
    "doc": {"first_name": "Tobias",
     "town": "Newport Beach"},
    "uly": {"first_name": "Ulysses",
     "species": "Cat"},
      }

nickname = input("enter the contact you would like to see: ")
if nickname in contacts_obj:
    print("contact: {0}".format(nickname))
    contact = contacts_obj[nickname]
    for key in contact:
        print("   {0}: {1}".format(key, contact[key]))
    else:
        print("sorry, I don't know {0}".format(nickname))
        