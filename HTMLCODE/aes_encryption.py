from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

key = os.urandom(32) # AES-256
iv = os.urandom(16) # IV must be 16 bytes for AES

def encrypt_aes(plaintext):
 cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
 encryptor = cipher.encryptor()
 padded_plaintext = plaintext + (16 - len(plaintext) % 16) * chr(16 - len(plaintext) % 16)
 ciphertext = encryptor.update(padded_plaintext.encode()) + encryptor.finalize()
 return ciphertext

def decrypt_aes(ciphertext):
 cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
 decryptor = cipher.decryptor()
 padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
 padding_length = padded_plaintext[-1]
 return padded_plaintext[:-padding_length].decode()

if __name__ == "__main__":
    plaintext = "Hi! This is Enrico and i test this code to see if it is working properly."

    ciphertext = encrypt_aes(plaintext)
    print(f"Ciphertext: {ciphertext}")
    
    decrypted_text = decrypt_aes(ciphertext)
    print(f"Decrypted: {decrypted_text}")