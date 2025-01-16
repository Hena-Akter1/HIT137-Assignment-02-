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


def main():
    #User inputs for n and m 
    n = int(input("Enter the value of n "))
    m = int(input("Enter the value of m "))
    encrypt(n, m)
main()
