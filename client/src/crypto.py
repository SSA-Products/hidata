from imports import *

class Crypto:

    def hash_hex(string):
        return hashlib.sha256(string).hexdigest()

    def hash(string):
        return hashlib.sha256(string).digest()

    def pad(string):
        while len(string) % 16 != 0:
            string = string + b" "
        return string

    def encrypt(data, key):
        mode = AES.MODE_CBC
        IV = b'\xda\xd9\x90\xb6S\x0e\xca\xa1\x1e\xae\x94?\xd9\x90\xddu'  # The IV
        cipher = AES.new(key, mode, IV)
        padded = Crypto.pad(data)
        encrypted = cipher.encrypt(padded)
        return encrypted

    def decrypt(data, key):
        mode = AES.MODE_CBC
        IV = b'\xda\xd9\x90\xb6S\x0e\xca\xa1\x1e\xae\x94?\xd9\x90\xddu'  # The IV
        cipher = AES.new(key, mode, IV)
        decrypted = cipher.decrypt(data)
        return decrypted

    def encrypt_rsa(data, publickey):
        result = []
        for n in range(0, len(data), 245):
            chunk = data[n:n+245]
            result.append(rsa.encrypt(chunk, publickey))
        return b''.join(result)

    def decrypt_rsa(data, privatekey):
        result = []
        for n in range(0, len(data), 256):
            chunk = data[n:n+256]
            result.append(rsa.decrypt(chunk, privatekey))
        return b''.join(result)

    def load_rsa_public(pem_key):
        return rsa.PublicKey.load_pkcs1(pem_key)

    def load_rsa_private(pem_key):
        return rsa.PrivateKey.load_pkcs1(pem_key)

    def save_rsa(key):
        return key.save_pkcs1("PEM")