country_names = ["Italy", "Austria", "Spain"]
print("ci sono {0} paesi nella lista".format(len(country_names)))

counter = 0
while counter < len(country_names):
    print("il paese con l'indice {0} è {1}".format(counter,country_names[counter]))
    counter = counter + 1