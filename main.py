import string

password = input("Enter your password: ")

if len(password) < 8:
    print("Password must be at least 8 characters long.")

has_upper = any(char in string.ascii_uppercase for char in password)
has_lower = any(char in string.ascii_lowercase for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(char in string.punctuation for char in password)

if not has_upper or not has_lower or not has_digit or not has_special:
    print("Password must contain uppercase letters, lowercase letters, digits, and special characters.")

if len(set(password)) != len(password):
    print("Password must not contain repeating characters.")
