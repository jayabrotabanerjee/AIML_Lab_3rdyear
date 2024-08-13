import random
import string

def get_user_criteria():
    length = int(input("Enter the length of the passwords: "))
    
    char_sets = []
    if input("Include lowercase letters? (y/n): ").lower() == 'y':
        char_sets.append(string.ascii_lowercase)
    if input("Include uppercase letters? (y/n): ").lower() == 'y':
        char_sets.append(string.ascii_uppercase)
    if input("Include digits? (y/n): ").lower() == 'y':
        char_sets.append(string.digits)
    if input("Include symbols? (y/n): ").lower() == 'y':
        char_sets.append(string.punctuation)
    
    if not char_sets:
        print("No character sets selected. Exiting.")
        exit()

    return length, ''.join(char_sets)

def generate_unique_passwords(length, char_set, num_passwords):
    passwords = set()

    while len(passwords) < num_passwords:
        password = ''.join(random.choice(char_set) for _ in range(length))
        passwords.add(password)

    return list(passwords)

def main():
    length, char_set = get_user_criteria()
    num_passwords = int(input("Enter the number of unique passwords to generate: "))

    if num_passwords <= 0:
        print("Number of passwords must be greater than zero. Exiting.")
        exit()

    passwords = generate_unique_passwords(length, char_set, num_passwords)

    print(f"Generated {num_passwords} unique passwords:")
    for pwd in passwords:
        print(pwd)

if __name__ == "__main__":
    main()
