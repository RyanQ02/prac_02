output_file = "name.txt"

out_file = open(output_file, "w")

name = input("What is your name? ")
print("Your name is {}".format(name), file=out_file)


out_file.close()
