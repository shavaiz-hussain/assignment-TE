from cryptography.fernet import Fernet

key = Fernet.generate_key()
file = open("encrypt.key", "w+")
file.write(key)
