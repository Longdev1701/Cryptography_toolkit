import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

class rsa_tool:
    @staticmethod
    def tao_key():
        k = RSA.generate(2048)
        priv = base64.b64encode(k.export_key('DER')).decode('utf-8')
        pub = base64.b64encode(k.publickey().export_key('DER')).decode('utf-8')
        return pub, priv

    @staticmethod
    def ma_hoa(txt, pub_k):
        try:
            k_goc = base64.b64decode(pub_k)
            nguoi_nhan = RSA.import_key(k_goc)
            c = PKCS1_OAEP.new(nguoi_nhan)
            
            kq = c.encrypt(txt.encode('utf-8'))
            return base64.b64encode(kq).decode('utf-8')
        except Exception as e:
            return f"[!] Encryption error: Invalid key or plaintext too long. Details: {e}"

    @staticmethod
    def giai_ma(chuoi_b64, priv_k):
        try:
            k_goc = base64.b64decode(priv_k)
            k_rieng = RSA.import_key(k_goc)
            c = PKCS1_OAEP.new(k_rieng)
            
            raw = base64.b64decode(chuoi_b64)
            txt = c.decrypt(raw).decode('utf-8')
            return txt
        except Exception as e:
            return f"[!] Decryption error: Wrong key or corrupted data. Details: {e}"