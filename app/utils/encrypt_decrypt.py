from cryptography.fernet import Fernet

class EncryptDecrypt:
    def __init__(self, key, encrypt: bool = False) -> None:
        self.cipher = Fernet(key)
        self.encrypt = encrypt
    
    def encrypt_dict(self, dictionary) -> str:
        if not self.encrypt:
            return dictionary
        serialized_dict = str(dictionary).encode()
        encrypted_dict = self.cipher.encrypt(serialized_dict)
        return encrypted_dict

    def decrypt_dict(self, encrypted_dict) -> dict:
        if not self.encrypt:
            return encrypted_dict
        decrypted_dict = self.cipher.decrypt(encrypted_dict)
        deserialized_dict = eval(decrypted_dict.decode())
        return deserialized_dict