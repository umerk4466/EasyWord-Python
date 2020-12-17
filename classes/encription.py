from cryptography.fernet import Fernet


# class used for encript and decript data
class Encription:
    # constructor
    def __init__(self):
        self.__key = ""

    # method to set key
    def setKey(self, key):
        self.__key = key

    # method to generate new key
    def generateKey(self):
        self.__key =  Fernet.generate_key()
        return self.__key

    # method to encript password
    def encriptPassword(self, password):
        encoded_password = password.encode()
        f = Fernet(self.__key)
        encrypted_password = f.encrypt(encoded_password)
        return encrypted_password

    # method to decript password
    def decriptPassword(self, password_key):
        f = Fernet(self.__key)
        decrypted_password = f.decrypt(password_key)
        decrypted_password = decrypted_password.decode()
        return decrypted_password