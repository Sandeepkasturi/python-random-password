import random
import string

def generate_password(length):
    """Generate a random password of specified length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Example usage: generate a random password of length 10
password = generate_password(10)
print(password)
