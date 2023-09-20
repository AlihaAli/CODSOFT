import random

# Function to generate a random password of the specified length
def generate_password(length):
  valid_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:,.<>?"
  valid_char_count = len(valid_char)

  password = ""
  random.seed(None)

  for i in range(length):
    random_index = random.randint(0, valid_char_count - 1)
    password += valid_char[random_index]

  return password

# Main function
def main():
  password_length = int(input("Enter the length of the password you desire: "))

  if password_length <= 0:
    raise ValueError("Invalid length. Please enter a positive integer.")

  password = generate_password(password_length)

  print("Generated Password:", password)

if __name__ == "__main__":
  main()
