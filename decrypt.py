
from cryptography.fernet import Fernet
import os

def decrypt_files():
    try:
        # Load the key
        with open('key.key', 'rb') as key_file:
            key = key_file.read()
        
        # Validate key
        if len(key) == 0:
            print("Error: key.key file is empty. Please run encrypt.py first to generate a key.")
            return
        
        fernet = Fernet(key)
        
        folder_path = input("Enter the folder path: ")
        
        if not os.path.exists(folder_path):
            print(f"Error: Folder '{folder_path}' does not exist.")
            return
        
        decrypted_count = 0
        
        for item in os.listdir(folder_path):
            full_path = os.path.join(folder_path, item)
            if os.path.isfile(full_path):
                try:
                    # Read encrypted content as bytes
                    with open(full_path, 'rb') as file:
                        encrypted_content = file.read()
                    
                    # Decrypt the content
                    decrypted_content = fernet.decrypt(encrypted_content)
                    
                    # Write decrypted content back as text
                    with open(full_path, 'w', encoding='utf-8') as file:
                        file.write(decrypted_content.decode('utf-8'))
                    
                    print(f"Successfully decrypted: {item}")
                    decrypted_count += 1
                    
                except Exception as e:
                    print(f"Error processing file {item}: {e}")
        
        print(f"\nDecryption complete. {decrypted_count} files processed.")
        
    except FileNotFoundError:
        print("Error: key.key file not found. Please run encrypt.py first to generate a key.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    decrypt_files()
