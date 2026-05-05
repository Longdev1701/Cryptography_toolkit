import hashlib

def bam_md5(chuoi_vao):
    try:
        b = chuoi_vao.encode('utf-8')
        h = hashlib.md5(b)
        return h.hexdigest()
    except Exception as e:
        return f"[!] Hashing error: {e}"

def bam_sha256(chuoi_vao):
    try:
        b = chuoi_vao.encode('utf-8')
        h = hashlib.sha256(b)
        return h.hexdigest()
    except Exception as e:
        return f"[!] Hashing error: {e}"

