from django.db import models

class Contact(models.Model):
    correo = models.EmailField(max_length=255)
    asunto = models.CharField(max_length=255)
    mensaje = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.correo} - {self.asunto}"