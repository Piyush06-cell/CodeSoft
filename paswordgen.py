import random
import string

def generate_password(length):
    # Define the character 
    characters = string.ascii_letters + string.digits + string.punctuation

    # Randomly select characters to form the password
    password = ''.join(random.choice(characters) for i in range(length))

    return password


try:
    password_length = int(input("Enter the desired password length: "))
    

    if password_length <= 0:
        print("Password length should be a positive integer.")
    else:
        password = generate_password(password_length)
        print("Generated Password:", password)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
