from cryptography.fernet import Fernet
class Password:

    # Encriptar la llave.
    def encryptPasword(pw):
        secretKey = Fernet.generate_key()
        crypter = Fernet(secretKey)
        spw = crypter.encrypt(pw)
        return secretKey, spw

    # Desencriptar la llave.
    def decrypt(secretKey,pw):
        crypter = Fernet(secretKey)
        dpw = crypter.decrypt(pw)
        return dpw
