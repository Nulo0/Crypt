# Caesar's Cipher
The Caesar cipher was initially used by the Roman Emperor Julius Caesar as a way of protecting messages sent to his generals, and is considered one of the earliest cryptographic models in existence.

Its operation is based on the displacement of each word of the phrase, key times, this means that, if the phrase is "Test" and the key is 3 (default used by the emperor), each word must be replaced by the word 3 positions ahead in the alphabet, with "Whvw" as a result.

It is worth mentioning that the codes have a custom alphabet, however, any code that has the pattern presented above is considered Caesar Cipher.


There are three main commands in this code:

+ Encrypt --> Encrypt the message with the specified key.

```python 
python caesarCipher.py Encrypt "message" key(int)
```
+ Decrypt --> Decrypts the message with the specified key.
```python 
python caesarCipher.py Decrypt "message" key(int)
```
+ Foundkey --> Finds the key from an encrypted message.
```python 
python caesarCipher.py Foundkey "message"
```
In the Encrypt command, if the key is not specified, the value will be 0.

**The commands must be run in the terminal.**

[Vigenère's Cipher](https://www.google.com.br/ "Go to code page")