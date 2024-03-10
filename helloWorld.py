while True:
    name = input("Hello! What is your name? ")
    if name.isalpha():
        break
    else:
        print("Error: Please enter only alphabetical characters for your name.")

print(name)