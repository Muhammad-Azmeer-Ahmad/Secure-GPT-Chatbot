from django.db import models

class ChatMessage(models.Model):
    user_message = models.BinaryField()      # Encrypted user message
    bot_response = models.BinaryField()      # Encrypted bot response
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return f"Chat at {self.created_at}"
