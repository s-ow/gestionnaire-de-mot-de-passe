from cryptography.fernet import Fernet

def checkkey():
    try:
        with open('utils/settings/key.key', 'rb') as filekey:
            key = filekey.read()
    except FileNotFoundError:
        return False

    if key != "":
        return True
    else:
        return False
    
def createkey():
    newkey = Fernet.generate_key()

    with open("utils/settings/key.key", "wb") as fichier_cle:
        fichier_cle.write(newkey)

def findkey():
    with open("utils/settings/key.key", "rb") as fichier_cle:
        key = fichier_cle.read()

    fernet = Fernet(key)

    return fernet

def encode(mot):
    fernet = findkey()

    code = fernet.encrypt(mot.encode())
    
    return code

def decode(mot):
    fernet = findkey()

    decode = fernet.decrypt(mot).decode()

    return decode