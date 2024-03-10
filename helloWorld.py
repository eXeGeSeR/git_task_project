while True:
    name = input("Hello! What is your name? ")
    # The name request only alphanumeric characters 
    if name.isalpha():
        break
    # If there are no alhpanumeric characters an error will be printed
    else:
        print("Error: Please enter only alphabetical characters for your name.")

print(name)