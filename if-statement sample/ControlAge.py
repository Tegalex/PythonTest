name =  input("il tuo nome: ")
age = int(input("la tua età: "))
if name == "Alessandro":
    print("Ciao")
elif age < 18:
    print(f"{name} stai programmando presto..Nice!")
else:
    print(f"piacere di conoscerti {name}.")