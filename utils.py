import base64
from Crypto.Cipher import DES3

def lay_size(loai):
    if loai == "DES": return 8
    if loai == "3DES": return 24
    if loai == "AES": return 16
    return None

def check_khoa(k_bytes, loai):
    sz = lay_size(loai)
    if len(k_bytes) != sz:
        return None, f"Key must be exactly {sz} bytes."

    if loai == "3DES":
        try:
            k_bytes = DES3.adjust_key_parity(k_bytes)
        except ValueError as e:
            return None, f"Invalid 3DES key: {e}"

    return k_bytes, None

def nhap_key_chu(loai):
    sz = lay_size(loai)
    chuoi = input(f"Enter secret key ({sz} characters): ")
    kb = chuoi.encode("utf-8")
    return check_khoa(kb, loai)

def nhap_key_b64(loai):
    chuoi = input("Enter key (Base64): ").strip()
    try:
        kb = base64.b64decode(chuoi)
    except Exception:
        return None, "Invalid Base64 key."
    return check_khoa(kb, loai)