password = "spam"
done = False
while done == False:
    user_password = input("Inserisci la password: ")
    if password == user_password:
        done = True
    else:
        print("Non è la password. Non puoi accedere")
print("SECRET ACCESS GRANTED")