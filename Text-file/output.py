output_file = open("output.txt", "w")
print("enter a few strings to write to the file, and type wuit when finished")
done=False
while not done:
    st = input("> ")
    if st == "quit":
        done = True
    else:
        output_file.write("{0}\n".format(st))
output_file.close()
print("fatto tutto!")