import random
import string
import uuid

def generate_password(length):
    """Generate a single password of the given length using a default set of characters."""
    all_chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(all_chars) for _ in range(length))

def get_mac_address():
    """Retrieve the MAC address of the machine."""
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
                    for elements in range(0,2*6,2)][::-1])
    return mac

def main():
    try:
        length = int(input("Enter the length of each password: "))
        if length <= 0:
            raise ValueError("Password length must be a positive integer")

        num_passwords = int(input("Enter the number of passwords to generate: "))
        if num_passwords <= 0:
            raise ValueError("Number of passwords must be a positive integer")

        unique_passwords = set()
        while len(unique_passwords) < num_passwords:
            password = generate_password(length)
            unique_passwords.add(password)

        mac_address = get_mac_address()
        print(f"\nMAC Address: {mac_address}")
        print("\nGenerated unique passwords:")
        for pwd in unique_passwords:
            print(pwd)
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

