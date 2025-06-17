# Ransomeware

This repository demonstrates a simple file encryption and decryption tool using Python and the `cryptography` library. **This is for educational purposes only. Do not use this code for malicious activity.**

## Features

- **File Encryption:** Encrypts all files in a specified folder using symmetric encryption (Fernet).
- **Key Generation:** Automatically generates a key and saves it to `key.key`.
- **File Decryption:** Decrypts previously encrypted files using the stored key.

## File Structure

```
.
├── encrypt.py         # Script to encrypt files in a folder
├── decrypt.py         # Script to decrypt files in a folder
├── key.key            # Encryption key (generated)
├── main.sh            # Example shell script
├── pyproject.toml     # Python project configuration
├── .replit            # Replit configuration
├── replit.nix         # Nix environment for Replit
└── enc/               # (Optional) Encrypted files directory
```

## Requirements

- Python 3.11+
- `cryptography` library

Install dependencies (if not present):

```bash
pip install cryptography
```

## Usage

### 1. Encrypt Files

Run the encryption script:

```bash
python encrypt.py
```

- You will be prompted to enter the path to the folder whose files you want to encrypt.
- The script will generate a `key.key` file (do not delete this, you need it to decrypt).

### 2. Decrypt Files

Run the decryption script:

```bash
python decrypt.py
```

- You will be prompted to enter the path to the encrypted folder.
- Make sure `key.key` is present in the same directory.

## Notes

- The `encrypt.py` and `decrypt.py` scripts process all files in the specified folder (non-recursively).
- The encryption key is critical. If lost, files cannot be decrypted.
- The tool is designed for learning purposes and is not production-ready.

## Security Warning

**Do not use this software for illegal purposes. The author is not responsible for any misuse.**
