import uuid
import re

def get_mac_address():
    """Retrieve the MAC address of the machine."""
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
                    for elements in range(0,2*6,2)][::-1])
    return mac

def check_sentence(sentence):
    """Check if the sentence adheres to the specified rules."""
    
    # Rule 1: Check if the sentence starts with a capital letter
    if not sentence[0].isupper():
        return "The sentence must start with a capital letter."
    
    # Rule 2: Check if the sentence ends with proper punctuation
    if not sentence.endswith(('.', '?', '!')):
        return "The sentence must end with a period, question mark, or exclamation point."
    
    # Rule 3: Check for consecutive spaces
    if '  ' in sentence:
        return "The sentence should not contain consecutive spaces."
    
    # Rule 4: Check for digits
    if any(char.isdigit() for char in sentence):
        return "The sentence should not contain any digits."
    
    # Rule 5: Check that each word is separated by a single space
    if re.search(r'\s{2,}', sentence):
        return "Each word should be separated by a single space."
    
    return "The sentence is correct."

def main():
    sentence = input("Enter a sentence to check: ")
    result = check_sentence(sentence)
    mac_address = get_mac_address()
    print(f"\nMAC Address: {mac_address}")
    print(result)

if __name__ == "__main__":
    main()

