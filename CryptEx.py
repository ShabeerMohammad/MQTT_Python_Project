from cryptography.fernet import Fernet
key = Fernet.generate_key()
print(key)
f = Fernet(key)
print(f)
token = f.encrypt(b"Encrypting and Decrypting the data is easy")
print(token)
token1 = f.decrypt(token)
print(token1)


