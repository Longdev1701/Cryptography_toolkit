from Crypto.Cipher import DES, DES3, AES
from utils import generate_key,pad_data,unpad_data

class des:
    def encryption(data, key):
        key = key.encode()
        cipher = DES.new(key, DES.MODE_CBC)
        iv = cipher.iv
        padded_data = pad_data(data.encode(),DES.block_size)
        cipher_text = cipher.encrypt(padded_data)

        return iv + cipher_text
    
    def decryption(data,key,iv):
        decipher = DES.new(key, DES.MODE_CBC, iv)
        original_data = unpad_data(decipher.decrypt(data),DES.block_size)

        return original_data


# a = des.encryption("Longlatoi1701@","longlato")
# print(a)
# cipher_text = a[8:]
# iv = a[:8]
# b = des.decryption(cipher_text,"longlato".encode(), iv)
# print(b)

class triple_des:
    def encryption(data, key):
        key = key.encode()
        cipher = DES3.new(key, DES3.MODE_CBC)
        iv = cipher.iv
        padded_data = pad_data(data.encode(),DES3.block_size)
        cipher_text = cipher.encrypt(padded_data)

        return iv +  cipher_text
    def decryption(data, key, iv):
        decipher = DES3.new(key, DES3.MODE_CBC, iv)
        original_data = unpad_data(decipher.decrypt(data),DES3.block_size)

        return original_data

# a = triple_des.encryption("Longlatoi1701","longlato1701@@@@")  
# print(a[:8])
# b = triple_des.decryption(a[8:],"longlato1701@@@@".encode(),a[:8])
# print(b)

class aes:
    def encryption(data, key):
        key = key.encode()
        cipher = AES.new(key, AES.MODE_CBC)
        iv = cipher.iv
        padded_data = pad_data(data.encode(),AES.block_size)
        cipher_text = cipher.encrypt(padded_data)

        return iv + cipher_text 
    def decryption(data, key, iv):
        decipher = AES.new(key, AES.MODE_CBC, iv)
        original_data = unpad_data(decipher.decrypt(data),AES.block_size)

        return original_data
    
# a = aes.encryption("Longlatoi1701","longlato1701@@@@")  
# print(a[:16])

# b = aes.decryption(a[16:],"longlato1701@@@@".encode(),a[:16])
# print(b)