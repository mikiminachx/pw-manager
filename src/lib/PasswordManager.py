from ..EncryptionManager import EncryptionManager
from ..DatabaseManager import DatabaseManager

class PasswordManager:
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.encryption_manager = EncryptionManager()

    def add_password(self, service, loginid, password):
        encrypted_password = self.encryption_manager.encrypt_password(password)
        self.db_manager.insert_password(service, loginid, encrypted_password)

    def get_loginid(self, service):
        return self.db_manager.retrieve_loginid(service)

    def get_password(self, service):
        encrypted_password = self.db_manager.retrieve_password(service)
        if encrypted_password:
            return self.encryption_manager.decrypt_password(encrypted_password)
        return None
    
    def get_all_details(self):
        all_details = self.db_manager.retrieve_all_details()
        if all_details:
            decrypted_details = [(service, loginid, self.encryption_manager.decrypt_password(encrypted_password))
                                 for service, loginid, encrypted_password in all_details]
            return decrypted_details
        else:
            return []

    def delete_password(self, service):
        self.db_manager.delete_service(service)
        print(f"Password for {service} is deleted.")

if __name__ == "__main__":
    pm = PasswordManager()

    # Test: Add Password
    pm.add_password("example_service", "example_loginid", "my_secured_password")
    print("Password added for example_service.")

    # Test: Get Password for a Specific Service
    retrieved_password = pm.get_password("example_service")
    print(f"Retrieved Password for example_service: {retrieved_password}")

    # Test: Get LoginID for a Specific Service
    retrieved_loginid = pm.get_loginid("example_service")
    print(f"Retrieved LoginID for example_service: {retrieved_loginid}")

    # Test: Get All Details
    all_details = pm.get_all_details("example_service")
    print("All details:", all_details)

    # Test: Delete passwords
    delete_password = pm.delete_password("example_service")
    print(f"Password for the selected password is deleted.")

    # Display passwords for all services (Optional)
    for service, loginid, decrypted_password in all_details:
        print(f"Service: {service}, Login ID: {loginid}, Password: {decrypted_password}")
