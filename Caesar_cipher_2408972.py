import os;
def welcome():
    print(""" Welcome to the Caesar Cipher
This program encrypts and decrypts text with the Caesar Cipher.
""")

def enter_message():
    while True:
        user = input("Enter 'encrypt(e)' or 'decrypt(d)': ").lower()

        if user in ['e', 'd']:
            break
        else:
            print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")

   
    secret = input("Enter the message: ").upper()

    return user, secret

def process_file(filename, mode):
    """Processes a file containing messages for encryption or decryption.

    Args:
        filename (str): The name of the file to process.
        mode (str): The mode of operation, either 'e' for encryption or 'd' for decryption.

    Yields:
        str: Processed messages one by one.
    """
    global shift
    try:
        with open(filename, 'r') as file:
            for message in file:  
                if mode == 'e':
                    yield encode_caesar_cipher(message.strip(), shift) 
                else:
                    yield decode_caesar_cipher(message.strip(), shift)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

          
def is_file(filename):
    """Checks if a file exists.

    Args:
        filename (str): The name of the file to check.

    Returns:
        bool: True if the file exists, False otherwise.
    """

    return os.path.isfile(filename)   

def write_messages(messages):
    """Writes a list of messages to a file.

    Args:
        messages (list): A list of messages to write to the file.
    """

    with open('results.txt', 'w') as file:
        for message in messages:
            file.write(message + '\n')

def message_or_file():
    """Prompts the user for input mode (message or file) and returns relevant data.

    Returns:
        tuple: A tuple containing the mode ('e' or 'd'), the message (if console input), and the filename (if file input).
    """

    while True:
        mode = input("Enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ").lower()
        if mode in ('e', 'd', 'q'):
            break
        print("Invalid mode. Please enter 'e', 'd', or 'q'.")

    if mode == 'q':
        return None, None, None

    while True:
        input_method = input("Enter 'm' to enter a message or 'f' to process a file: ").lower()
        if input_method in ('m', 'f'):
            break
        print("Invalid input method. Please enter 'm' or 'f'.")

    if input_method == 'm':
        return mode, input("Enter your message: "), False

    while True:
        filename = input("Enter the filename: ")
        if is_file(filename):  
            return mode,filename,True
        print("File not found. Please try again.")       
          
          




def encode_caesar_cipher(message, shift):
    """ takes message and shift value as a parameter then
        iterates through the each letter of the message converting then to ascii values then adding the shift values to that and using modulus 26 to ensure that our result stays imbound to 26 alphabets and finally converts the result ascii values to encoded letters of list 
         returns the encoded message using .join() """ 
    result = [chr((ord(char) - ord('A' if char.isupper() else 'a') + shift) % 26 + ord('A' if char.isupper() else 'a')) if char.isalpha() else char for char in message]
    return ''.join(result)

def decode_caesar_cipher(encoded_message, shift):
    """ takes encoded_message and shift value as parameters then returns encoded_message and (-ve shift) value back to the encode_ceaser_cipher function
     which returns the decoded message back to this function then returns that message """
    return encode_caesar_cipher(encoded_message, -shift)


def main():
    welcome()
    while True:
        mode, message_or_filename, _ = message_or_file()
        if mode is None:
            print("Thankyou for using this program, Goodbye!")
            break  



        if _ != True:  
            global shift
            shift = int(input("Enter shift: - "))
            processed_message = encode_caesar_cipher(message_or_filename, shift) if mode == 'e' else decode_caesar_cipher(message_or_filename, shift)
            print("Processed message:", processed_message)
        else:
            filename = message_or_filename
            shift = int(input("Enter shift: - "))
            processed_messages = process_file(filename, mode)
            write_messages(processed_messages)
            print("Processed messages written to results.txt")
if __name__ == '__main__': 
    main()

