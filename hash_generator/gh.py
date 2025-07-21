import hashlib

string = input("Enter a string to hash: ")

menu = int(
    input(
        """### Select hashing algorithm:###
             1. MD5
             2. SHA-1
             3. SHA-256
             4. SHA-512
                Enter your choice (1-4): """
    )
)

if menu == 1:
    result = hashlib.md5(string.encode())
    print("MD5 Hash:", result.hexdigest())

elif menu == 2:
    result = hashlib.sha1(string.encode())
    print("SHA-1 Hash:", result.hexdigest())

elif menu == 3:
    result = hashlib.sha256(string.encode())
    print("SHA-256 Hash:", result.hexdigest())

elif menu == 4:
    result = hashlib.sha512(string.encode())
    print("SHA-512 Hash:", result.hexdigest())

else:
    print("Invalid choice. Please select a number between 1 and 4.")
