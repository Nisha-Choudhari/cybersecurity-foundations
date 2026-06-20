import hashlib

def hash_password(password, algorithm="md5"):
    if algorithm == "md5":
        return hashlib.md5(password.encode()).hexdigest()
    elif algorithm == "sha256":
        return hashlib.sha256(password.encode()).hexdigest()

def crack_hash(target_hash, wordlist, algorithm="md5"):
    for word in wordlist:
        if hash_password(word, algorithm) == target_hash:
            return word
    return None

target = hash_password("123456", algorithm="sha256")
print(f"Target hash: {target}")
print("Cracking...")

with open("rockyou.txt", "r", encoding="latin-1") as f:
    wordlist = [line.strip() for line in f]

result = crack_hash(target, wordlist, algorithm="sha256")

if result:
    print(f"Password cracked: {result}")
else:
    print("Password not found in wordlist")