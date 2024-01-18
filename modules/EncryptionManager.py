from cryptography.fernet import Fernet
import os
from typing import Optional

class EncryptionManager:
    def __init__(self, key_path: str = 'secret_key') -> None:
        self.key_path = key_path
        self.key = self.load_or_generate_key()
        self.cipher_suite = Fernet(self.key)
    
    def load_or_generate_key(self) -> bytes:
        if os.path.exists(self.key_path):
            with open(self.key_path, 'rb') as key_file:
                return key_file.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_path, 'wb') as key_file:
                key_file.write(key)
            return key
    
    def encrypt_password(self, password: str) -> str:
        return self.cipher_suite.encrypt(password.encode()).decode()
    
    def decrypt_password(self, encrypted_password: str) -> Optional[str]:
        try:
            return self.cipher_suite.decrypt(encrypted_password.encode()).decode()
        except Exception as e:
            print(f'Error decrypting password: {e}')
            return None

# Test
if __name__ == '__main__':
    em = EncryptionManager()
    test_password = "example_password"
    encrypted = em.encrypt_password(test_password)
    print(f'Encrypted: {encrypted}')
    decrypted = em.decrypt_password(encrypted)  # Decrypt the encrypted password
    print(f'Decrypted: {decrypted}')
