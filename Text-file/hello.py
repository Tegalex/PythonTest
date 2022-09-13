input_file = open("hello.txt", "r")
lines = input_file.readlines()
input_file.close()
print("l'intero file hello.txt file: ")
print(lines)
print("il file hello.txt, line-by-line: ")
for x in lines:
     print(x)
print("fatto tutto!")