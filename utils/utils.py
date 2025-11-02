from cryptography.fernet import Fernet
from django.conf import settings

# Initialize Fernet with project ENCRYPTION_KEY
fernet = Fernet(settings.ENCRYPTION_KEY.encode())

def encrypt_message(message: str) -> bytes:
    """
    Encrypt a string message into bytes.
    """
    return fernet.encrypt(message.encode())

def decrypt_message(token: bytes) -> str:
    """
    Decrypt encrypted bytes back into string.
    """
    return fernet.decrypt(token).decode()
