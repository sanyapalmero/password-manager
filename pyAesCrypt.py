import os
from pyAesCrypt import encryptFile, decryptFile

BUFFER_SIZE = 64 * 1024

def clear():
    os.system('cls' if os.name=='nt' else 'clear')


def open_file():
    is_opened = False
    while not is_opened:
        path = input("path to your file: ")
        try:
            file = open(path)
            return path
        except FileNotFoundError as e:
            print(e)


def encrypt_file():
    path = open_file()
    password = input("password: ")
    encryptFile(path, path + ".encrypted", password, BUFFER_SIZE)
    print("file has been encrypted")


def decrypt_file():
    path = open_file()
    password = input("password: ")
    try:
        decryptFile(path, "res.txt", password, BUFFER_SIZE)
        print("file has been decrypted")
    except ValueError:
        print("wrong password or file is corrupted")


def main():
    menu = True
    while menu:
        print("1 - encrypt file")
        print("2 - decrypt file")
        print("3 - exit")

        resp = input("select action: ")
        if resp == "1":
            encrypt_file()
        elif resp == "2":
            decrypt_file()
        elif resp == "3":
            menu = False
            print("program has been completed")
        else:
            clear()
            print("unknown action")


if __name__ == '__main__':
    main()
