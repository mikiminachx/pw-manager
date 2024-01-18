from ..Modules.EncryptionManager import EncryptionManager
from ..Modules.DatabaseManager import DatabaseManager

class PasswordManager:
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.encryption_manager = EncryptionManager()
    
    def add_password(self, service, password):
        encrypted_password = self.encryption_manager.encrypt_password(password)
        self.db_manager.insert_password(service, encrypted_password)
    
    def get_password(self, service):
        encrypted_password = self.encryption_manager.retrieve_password(service)
        if encrypted_password:
            return self.encryption_manager.decrypt_password(encrypted_password)
        return None

# Test
pm = PasswordManager()
pm.add_password("example_service", "my_secured_password")
print(pm.add_password("example_service"))