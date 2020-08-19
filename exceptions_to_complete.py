finished = False
result = 0
while not finished:
    try:
        result = int(input("Please enter a integer: "))
        finished = True
    except ValueError:
        result = int(input("Please enter a valid integer: "))
print("Valid result is:", result)
