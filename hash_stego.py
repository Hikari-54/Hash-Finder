import hashlib
import string
import random
import shutil
import os

# This program creates and fills the files to get
# the desired last 2 digits of hashes from them
# ! finded char's will be saved in folder "matches" !

# Creating folders
if not os.path.exists("temp"):
    os.makedirs("temp")
if not os.path.exists("matches"):
    os.makedirs("matches")


def calculate_hash(data):
    data_hashObj = hashlib.sha1(data.encode())  #EDIT HASH ALGO
    data_hashStr = data_hashObj.hexdigest()
    return data_hashStr


def save_file(data, last2_hash_nums):
    # hex code -> bytes
    last2_hash_bytes = bytes.fromhex(last2_hash_nums)
    # bytes -> str by windows-1251
    hash_symb = last2_hash_bytes.decode("windows-1251")  #EDIT DECODING
    with open(f"matches/{hash_symb}.txt", "w") as file:
        file.write(data)


# ---------------------------
alphabet = string.ascii_letters + string.digits  #EDIT ALPHABET

find_symb = input("Enter the required unique characters from win-1251: ")
find_symb_hex = find_symb.encode('windows-1251').hex()
find_symb_hex_codes = []

# Splitting string into two hex nums
for i in range(0, len(find_symb_hex), 2):
    hex_code = find_symb_hex[i:i + 2]
    find_symb_hex_codes.append(hex_code)

total_symbols_to_find = len(find_symb_hex_codes)
found_symbols = {}

while True:
    number_of_found_symbols = len(found_symbols)
    if number_of_found_symbols >= total_symbols_to_find:
        break  # if all symbols were finded

    # Create files and fill them with data
    for _ in range(10):
        filename = f"temp/{_}.txt"
        with open(filename, "a+") as file:
            # Take a random character from the alphabet
            alphabet_index = random.randint(0, len(alphabet) - 1)
            file.write(alphabet[alphabet_index])

            # Calculating hashes
            file.seek(0)  # Moving the pointer to read
            data = file.readline()
            last2_hash_nums = calculate_hash(data)[-2:]
            if last2_hash_nums in find_symb_hex_codes and last2_hash_nums not in found_symbols.values():
                hash_symb = bytes.fromhex(last2_hash_nums).decode(
                    "windows-1251", errors="ignore")
                found_symbols[filename] = last2_hash_nums
                save_file(data, last2_hash_nums)

# Deleting temp folder
shutil.rmtree("temp")
print("Checkout folder matches")
