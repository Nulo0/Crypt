# Cifra de César
import re
import sys
import pandas as pd

ALPHABET = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ1234567890 '
CryptMode = 1
DecryptMode = CryptMode * -1

# O diciionário usado, de acordo com a GNU Public License (https://www.ime.usp.br/~ueda/br.ispell/gpl) é ofertado pelo Dicinonário br.ispell(https://www.ime.usp.br/~ueda/br.ispell/), todos os créditos, por esse trabalho incrível, a eles.

dictonary = pd.read_csv("https://www.ime.usp.br/~pf/dicios/br-utf8.txt", header=None) 
dictonary.columns = ['Palavaras']
listDictionary = dictonary['Palavaras'].tolist()

def main():
    command = sys.argv[1].lower()
    message = sys.argv[2]
    key = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    verifyComand(command, message, key)

def crypt(message, mode, key = 0):
    cryptMessage = ''
    for word in message:
        if word in ALPHABET:
            wordIndex = ALPHABET.index(word)
            cryptMessage += ALPHABET[(wordIndex + (mode * key)) % len(ALPHABET)]
        else:
            cryptMessage += word
    return cryptMessage

def encrypt(message, key):
    return crypt(message, CryptMode, key)

def decrypt(message, key):
    return crypt(message, DecryptMode, key)

def foundKey(message):
    maxSearchValue = int(input("Max key's value for search: ")) + 1
    cont = 0
    for i in range(maxSearchValue):
        newMessage = ''
        newMessage = decrypt(message, i)
        newMessage = re.sub(r'[^\w\s]','',newMessage) #regex para remover pontos
        listMessage= newMessage.split(' ')
        minimalPercent = int((len(listMessage) * 75) / 100)
        for word in listMessage:
            if word.lower() in listDictionary:
                cont += 1
        if cont > minimalPercent:
            break
    return i

def keyResult(message, key):
    decision = input("Want see a Decrypted Message? (Yes or no) ").lower()
    if decision == 'yes':
        print("Decrypted Message:  " + decrypt(message, key))
        print("\nIf the result doesn't make sense, try increasing the Max key's value for search.")
        increase = input("Want to increase?(Yes or no) ").lower()
        if increase == 'yes':
            keyIncrease = foundKey(message)
            print("Key founded " + str(keyIncrease))
            keyResult(message, keyIncrease)
        elif increase == 'no':
            exit()
        else:
            print('command not found -> ' + increase)
    elif decision == 'no':
        exit()
    else:
        print('command not found -> ' + decision)
            
def verifyComand(command, message, key):
    if command == 'encrypt':
        print("Crypt Mode ")
        print("Crypted Message:  " + encrypt(message, key))
        print("Chave não especificada.") if key == 0 else ""

    elif command == 'decrypt':
        print("Decrypt Mode ")
        print("Decrypted Message:  " + decrypt(message, key))
        print("\nIf the result doesn't make sense, try to found a correct key.")
        increase = input("Want to find?(Yes or no) ").lower()
        if increase == 'yes':
            key = foundKey(message)
            print("Key founded " + str(key))
            keyResult(message, key)
        elif increase == 'no':
            exit()
        print("Chave não especificada.") if key == 0 else ""

    elif command == "foundkey":
        key = foundKey(message)
        print("Key founded " + str(key))
        keyResult(message, key)

    else:
        print('command not found -> ' + command)

if __name__ == '__main__':
    main()