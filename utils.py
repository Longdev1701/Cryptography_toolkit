import base64
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def validate_aes_key(key: bytes):
    return len(key) in [16, 24, 32]

def validate_des_key(key: bytes):
    return len(key) == 8

def encode_base64(data: bytes):
    return base64.b64encode(data).decode()

def decode_base64(data: str):
    return base64.b64decode(data.encode())

def pad_data(data: bytes, block_size: int):
    return pad(data, block_size)

def unpad_data(data: bytes, block_size: int):
    return unpad(data, block_size)

def generate_key(length: int):
    return get_random_bytes(length)

def get_input(prompt):
    return input(prompt).strip()

def print_error(msg):
    print(f"[ERROR] {msg}")