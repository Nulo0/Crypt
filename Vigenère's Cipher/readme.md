# Vigenère's Cipher
The Vigenère Cipher is a model of cryptography using a series of different letter-based Caesar Ciphers, invented by Leon Battista Alberti around 1465.

> To encrypt, a table of alphabets can be used, termed a tabula recta, Vigenère square or Vigenère table. It has the alphabet written out 26 times in different rows, each alphabet shifted cyclically to the left compared to the previous alphabet, corresponding to the 26 possible Caesar ciphers. At different points in the encryption process, the cipher uses a different alphabet from one of the rows. The alphabet used at each point depends on a repeating keyword.
[Wikipedia](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher "The free encyclopedia")

It is worth mentioning that the codes have a custom alphabet.


There are three main commands in this code:

+ Encrypt --> Encrypt the message with the specified key.

```python 
python vigenereCipher.py Encrypt "message" "key"
```
+ Decrypt --> Decrypts the message with the specified key.
```python 
python vigenereCipher.py Decrypt "message" "key"
```
+ GenerateKey --> Generate a key with the specified size.
```python 
python vigenereCipher.py GenerateKey
```
In the Encrypt command, it is mandatory that the key has the same size as the message.

**The commands must be run in the terminal.**

[Caesar's Cipher](https://www.google.com.br/ "Go to code page")