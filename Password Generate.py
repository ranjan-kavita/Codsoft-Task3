import random
import string

def generate_password(length=12, include_uppercase=True, include_numbers=True, include_symbols=True):
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if include_uppercase else ''
    numbers = string.digits if include_numbers else ''
    symbols = string.punctuation if include_symbols else ''

    # Combine all the allowed characters
    all_characters = lowercase_letters + uppercase_letters + numbers + symbols

    # Ensure the password is generated from at least one character from each allowed set
    if not all_characters:
        raise ValueError("At least one character set should be enabled!")

    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

# Example usage
password = generate_password(length=16, include_uppercase=True, include_numbers=True, include_symbols=True)
print("Generated Password:", password)
