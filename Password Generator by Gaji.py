


import random
import string

def password_generator(length):
    if length < 4:
        print("Password length should be at least 4.")
        return None
    
    # Character sets to use in the password
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
    # Ensuring the password has at least one of each type of character
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(special),
        random.choice(digits)
    ]
    
    # Fill the rest of the password length with random characters
    all_characters = lower + upper + digits + special
    password += random.choices(all_characters, k=length - 4)
    
    # Shuffle the password to avoid predictable patterns
    random.shuffle(password)
    
    # Combine the list into a single string
    return ''.join(password)

# Prompt the user for the length of the password
def passcode():
    print("Welcome to Gaji password generator :) ")
    print(f"\n")
    try:
        length = int(input("Enter the desired password length: "))
        password = password_generator(length)
        if password:
            print(f"Your generated password is: {password}")
    except ValueError:
        print("Please enter a valid number for the password length.")
        passcode()  # Re-run if there's an error

passcode()
