country_list = []
done =False
while done ==False:
    country = input("inserisci un nome di paese: ")
    if len(country)==0:
        done=True
    else:
        country_list.append(country)
        
for country in country_list:
    print("Country: {0}".format(country))
    
print("Tutto fatto!")