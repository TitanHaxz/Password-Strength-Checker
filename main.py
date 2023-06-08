import string

while True:
    password = input("Enter your password: ")

    missing_requirements = []

    if len(password) < 8:
        missing_requirements.append("Password must be at least 8 characters long.")

    if not any(char in string.ascii_uppercase for char in password):
        missing_requirements.append("You must use at least one uppercase letter.")

    if not any(char in string.ascii_lowercase for char in password):
        missing_requirements.append("You must use at least one lowercase letter.")

    if not any(char.isdigit() for char in password):
        missing_requirements.append("You must use at least one digit.")

    if not any(char in string.punctuation for char in password):
        missing_requirements.append("You must use at least one special character.")

    if len(set(password)) != len(password):
        missing_requirements.append("Password must not contain repeating characters.")

    if len(missing_requirements) == 0:
        strength_score = 5
        print("Your password is strong! Strength Score: ", strength_score)
    else:
        strength_score = 5 - len(missing_requirements)
        print("Your password is weak. You must meet the following requirements:")
        for requirement in missing_requirements:
            print("- " + requirement)
        print("Strength Score: ", strength_score)
    
    continue_input = input("Do you want to enter another password? (Yes/No): ")
    if continue_input.lower() != "yes":
        break
