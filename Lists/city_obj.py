city_obj = [
  ["Toronto", "Ontario", 5113149],
  ["Montreal", "Quebec", 3635571],
  ["Vancouver", "British Columbia", 2116581],
  ["Ottawa", "Ontario", 1130761],
  ["Calgary", "Alberta", 1079310],
  ["Edmonton", "Alberta", 1034945],
  ["Quebec City", "Quebec", 715515],
  ["Winnipeg", "Manitoba", 694668],
  ["Hamilton", "Ontario", 692911],
  ["London", "Ontario", 457720]
]

 for city in city_obj:
     print("{0}, {1}, popolazione: {2}".format(city[0], city[1], city[2]))

print("Ora tocca a te, scrivi un nome di una città, ed io ti estrapolo i dati che ho a disposizione.")

# city_name = input("Dimmi un nome di una città che è in elenco: ")
# for city_name in city_obj:
#     if city[0].lower() == city_name.lower():
#         print("{0}, {1}, popolazione: {2}".format(city[0], city[1], city[2]))
#     else:
#         input("La città inserita non è in elenco. scrivi una città dell'elenco: ")
#         print("{0}, {1}, popolazione: {2}".format(city[0], city[1], city[2]))
#     break
