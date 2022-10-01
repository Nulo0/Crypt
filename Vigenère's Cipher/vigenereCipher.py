# Cifra de Vigenère
import string
import sys
import random as rd
from operator import add, sub

ALPHABET = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ1234567890 '
CryptMode = add
DecryptMode = sub

def main():
    command = sys.argv[1].lower()
    message = sys.argv[2] if len(sys.argv) > 3 else ""
    key = sys.argv[3] if len(sys.argv) > 3 else ""
    verifyComand(command, message, key)

def crypt(message, mode, key):
    if key == "":
        cryptMessage = message
        return cryptMessage
    count = 0
    cryptMessage = ""
    for word in message:
        soma = mode(ALPHABET.find(word), ALPHABET.find(key[count]))
        cryptMessage += str(ALPHABET[soma % len(ALPHABET)])
        count += 1
    return cryptMessage

def keyGenerator(message, chars=string.ascii_letters + string.digits, mode = 1):
    if mode == 0:
        keySize = int(input("Key's size: "))
        generateKey = ''.join(rd.choice(chars) for _ in range(keySize))
        return generateKey
    else:
        lenKey = len(message)
        generateKey = ''.join(rd.choice(chars) for _ in range(lenKey))
        return generateKey

def decisionKey(message):
    decision = input("Want to generate a key?(Yes or no) ").lower()
    if decision == 'yes':
        generateKey = keyGenerator(message)
        print("The generated key: " + generateKey)
        use = input("Want to use this key?(Yes or no) ").lower()
        if use == 'yes':
            print("Crypt Mode: ")
            print("Crypted Message:  " + encrypt(message, generateKey))
        elif use == 'no':
            decisionKey(message)
        else:
            print('command not found -> ' + use)
    elif decision == 'no':
        print("Mandatory key.")
        exit()
    else:
        print('command not found -> ' + decision)

def encrypt(message, key):
    return crypt(message, CryptMode, key)

def decrypt(message, key):
    return crypt(message, DecryptMode, key)

def verifyComand(command, message, key):
    if command == 'encrypt':
        if(len(key) != len(message)):
            print("Key's size must be the same of message.")
            decisionKey(message)
        else:
            print("Crypt Mode: ")
            print("Crypted Message:  " + encrypt(message, key))
            print("Key not specified.") if key == "" else ""
    elif command == 'decrypt':
        print("Decrypt Mode: ")
        print("Decrypted Message:  " + decrypt(message, key))
        print("Key not specified.") if key == "" else ""
    elif command == 'generatekey':
        print("Generated Key: " + keyGenerator(message, mode=0))
    else:
        print('command not found -> ' + command)
    

if __name__ == '__main__':
    main()