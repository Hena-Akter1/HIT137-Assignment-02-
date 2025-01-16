def encrypt(m,n):
    with open('raw_text.txt', 'r') as file1:
        text = file1.read()
        """Encrypt the content of a file and save it to another file."""
    encrypted_text = ''
    for char in text:
        if char.isdigit() or not char.isalnum():
            encrypted_text = encrypted_text + char
        elif (char >= 'a') and (char <= 'm'):
            shift = n * m
            new_char = chr(((ord(char) - ord('a') + shift) % 13) + ord('a'))
            encrypted_text = encrypted_text + new_char

        elif (char >= 'n') and (char <= 'z'):
            shift = (n + m)
            new_char = chr(((ord(char) - ord('n') - shift) % 13) + ord('n'))
            encrypted_text = encrypted_text + new_char
        elif (char >= 'A') and (char <= 'M'):
            shift = n #
            new_char = chr(((ord(char) - ord('A') - shift) % 13) + ord('A'))
            encrypted_text = encrypted_text + new_char
        elif (char >= 'N') and (char <= 'Z'):
            shift = m ** 2
            new_char = chr(((ord(char) - ord('N') + shift) % 13) + ord('N'))
            encrypted_text = encrypted_text + new_char
            
    with open('encrypted_text.txt', 'w') as file2:
        file2.write(encrypted_text)

        
def decrypt(m,n):
    """Decrypt the content of a encrypted file"""
    
    with open('encrypted_text.txt', 'r') as file:
        text = file.read()
        
    decrypted_text = ''
    for char in text:
        if char.isdigit() or not char.isalnum():
            decrypted_text = decrypted_text + char
        elif 'a' <= char <= 'm':
            shift = n*m
            new_char = chr(((ord(char) - ord('a') - shift) % 13) + ord('a'))
            decrypted_text = decrypted_text + new_char
        elif 'n' <= char <= 'z':
            shift = n+m
            new_char = chr(((ord(char) - ord('n') + shift) % 13) + ord('n'))
            decrypted_text = decrypted_text + new_char
        elif 'A' <= char <= 'M':
            shift = n
            new_char = chr(((ord(char) - ord('A') + shift) % 13) + ord('A'))
            decrypted_text = decrypted_text + new_char
        elif 'N' <= char <= 'Z':
            shift = m ** 2
            new_char = chr(((ord(char) - ord('N') - shift) % 13) + ord('N'))
            decrypted_text = decrypted_text + new_char

       

    return decrypted_text


def check(decrypted_text):
    """Check if the decrypted text matches the original text."""
    with open('raw_text.txt', 'r') as file1:
        original_text = file1.read()
        
    print("Original Text: ", original_text)
    print("Decrypted Text: ", decrypted_text)
    #Check correctness
    if original_text == decrypted_text:
        print('Decryption correct')
    else:
        print('Error in decryption')
        


def main():
    #User inputs for n and m 
    n = int(input("Enter the value of n "))
    m = int(input("Enter the value of m "))
    encrypt(n, m)
    decrypted_text = decrypt(n, m)
    check(decrypted_text)

main()
