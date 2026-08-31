import random
import string

def generate_password():

    # loop used to validate user input for length
    while True:
        length = int(input("Enter desired length of password: ").strip())

        if length < 4:
            #print("Password length must be at least greater than 4 :(")
            print("Your requested password length isn't compatible with your requirements :(")
        else:
            print("Invalid input")
            break

    # build the character pool based on user's preferences
    include_uppercase = input("Do you want to include uppercase letters? (yes/no): ").strip().lower()
    include_special = input("Do you want to include special characters? (yes/no): ").strip().lower()
    include_digits= input("Do you want to include digits? (yes/no): ").strip().lower()


    # get all available characters
    lower = string.ascii_lowercase      # ascii_lowercase gives all lowercase letter
    # print(lower)            # abcdefghijklmnopqrstuvwxyz
    uppercase = string.ascii_uppercase if include_uppercase == "yes" else ""   # if == then yay; if not turns empty string
    special = string.punctuation if include_special == "yes" else ""
    digits = string.digits if include_digits == "yes" else ""
    all_characters = lower + uppercase + special + digits   #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789


    # randomly (random.choice) select characters from the available pool for the length
    # using list cause its more flexible & faster to add items
    required_characters = []
    if include_uppercase == "yes":
        required_characters.append(random.choice(uppercase))
    if include_special == "yes":
        required_characters.append(random.choice(special))
    if include_digits == "yes":
        required_characters.append(random.choice(digits))

    remaining_length = length - len(required_characters)
    password = required_characters

    # loop through and add remaining characters
    # _ == placeholder variable
    for _ in range(remaining_length):
        character = random.choice(all_characters)
        password.append(character)

    # randomly mix up all items inside of list
    random.shuffle(password)

    str_password = "".join(password)        # .join combines all elements in list to a string
    # can do "".join    ",".join    ".".join    "|".join

    # display new password
    print(f"\n🔐:) Enjoy your new password: {str_password}")

# generate desired password
password = generate_password()
