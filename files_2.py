out_file = open("numbers.txt", "r")

num1 = int(out_file.readline())
num2 = int(out_file.readline())

print(num1, num2)

out_file.close()
