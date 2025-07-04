from cryptography.fernet import Fernet
import os

key = Fernet.generate_key()
fernet = Fernet(key)
with open('key.key', 'wb') as key_file:
  key_file.write(key)
folder_path = input("Enter the folder path: ")
for item in os.listdir(folder_path):
  full_path = os.path.join(folder_path, item)
  if os.path.isfile(full_path):
      try:
          with open(full_path, 'r') as file:
              contents = file.read()
              encrypted = fernet.encrypt(contents.encode())
              with open(full_path, 'wb') as encrypted_file:
                  encrypted_file.write(encrypted)
                
      except Exception as e:
         print(f"Error processing file {item}: {e}")