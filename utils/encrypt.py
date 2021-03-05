from cryptography.fernet import Fernet


def encrypt(data):
    key = get_key()
    f = Fernet(key)
    data = f.encrypt(data)
    return data


def get_key():
    try:
        file = open("encrypt.key", "rb")
        key = file.read()
        file.close()
        return key
    except FileNotFoundError:
        return b"12345"
