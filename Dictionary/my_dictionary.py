my_dictionary = {  'first_name': "Alessandro",  
                 'last_name': "Coder",  
                 'birth_year':"1984",  
                 'birth_month':"06",  
                 'birth_day': "17"}
print(my_dictionary)

print(my_dictionary["first_name"])

my_dictionary["birth_town"]="Cremona"
print(my_dictionary)

del(my_dictionary["birth_town"])
print(my_dictionary)

for key in my_dictionary:
    print("{0}: {1}".format(key, my_dictionary[key]))

sorted(my_dictionary)