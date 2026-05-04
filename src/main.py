from hashing import bam_md5, bam_sha256

def main():
    # Chuỗi dữ liệu mẫu để test
    test_string = "Chào mừng bạn đến với Lab 5"
    
    print(f"--- Kiểm tra hàm băm cho chuỗi: '{test_string}' ---")
    
    # Chạy thử MD5
    result_md5 = bam_md5(test_string)
    print(f"[MD5]:    {result_md5}")
    
    # Chạy thử SHA-256
    result_sha256 = bam_sha256(test_string)
    print(f"[SHA256]: {result_sha256}")

if __name__ == "__main__":
    main()