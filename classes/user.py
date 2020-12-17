# import other classes
from classes.encription import Encription


# class for user data
class User:
    # constructor
    def __init__(self):
        self.__name = ""
        self.__emailAddress = ""
        self.__username = ""
        self.__password = ""

    # method to set name
    def setName(self, name):
        self.__name = name
    
    # method to get name
    def getName(self):
        return self.__name

    # method to set emailAddress
    def setEmailAddress(self, emailAddress):
        if emailAddress == "":
            raise Exception("Error, email cannot be empty") 
        else:
            self.__emailAddress = emailAddress

    # method to get emailAddress
    def getEmailAddress(self):
        return self.__emailAddress

    # method to set username
    def setUsername(self, username):
        if username == "":
            raise Exception("Error, Username cannot be empty") 
        else:
            self.__username = username
    
    # method to get username
    def getUsername(self):
        return self.__username
    
    # method to set password
    def setPassword(self, password):
        if password == "":
            raise Exception("Error, Password cannot be empty") 
        else:
            self.__password = password

    # method to get password
    def getPassword(self):
        return self.__password

    # method to validate user if exists
    def validate(self):
        try:
            # get registered username
            user_data_file = open("user_data/user_data.txt", "r")
            username = user_data_file.readline().replace("\n", "")
            user_data_file.close()
            # get registered user credentials
            user_credentials_file = open("user_data/user_credentials.key", "rb")
            main_key = user_credentials_file.readline().replace(b"\n", b"")
            password_key = user_credentials_file.readline()
            user_credentials_file.close()
            # decrept password
            encription = Encription()
            encription.setKey(main_key)
            decrepted_password = encription.decriptPassword(password_key)
            # validate usere data
            if username == self.__username and decrepted_password == self.__password :
                return True       
            else:
                return False
        except:
            return False

    # method to register user
    def signup(self):
        try:
            # create user data file
            user_data_file = open("user_data/user_data.txt", "w")
            user_data_file.write(self.__username+"\n")
            user_data_file.write(self.__emailAddress+"\n")
            user_data_file.close()
            # create user encripted password file
            encription = Encription()
            user_credentials_file = open("user_data/user_credentials.key", "wb")
            user_credentials_file.write(encription.generateKey()+b'\n')
            user_credentials_file.write(encription.encriptPassword(self.__password))
            user_credentials_file.close()
            return True
        except:
            return False