from Crypto.Cipher import DES
from utils import generate_key,pad_data,unpad_data

class des:
    def encryption(data, key):
        haveKey = True
        key = key.encode()
        if(key == ""):
            key = generate_key(8)
            haveKey = False

        cipher = DES.new(key, DES.MODE_CBC)
        iv = cipher.iv

        padded_data = pad_data(data.encode(),DES.block_size)
        cipher_text = cipher.encrypt(padded_data)

        return iv + cipher_text + ((b" " + key) if haveKey is not True else b"")
    
    def decryption(data,key,iv):
        decipher = DES.new(key, DES.MODE_CBC, iv)
        original_data = unpad_data(decipher.decrypt(data),DES.block_size)

        return original_data


a = des.encryption("Longlatoi1701@","longlato")
print(a)

#cipher_text, key = a.split(b" ")
cipher_text = a[8:]
iv = a[:8]

b = des.decryption(cipher_text,"longlato".encode(), iv)
print(b)

