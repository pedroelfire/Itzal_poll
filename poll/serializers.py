from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    solicitud = serializers.CharField(write_only=True, required=False)  

    class Meta:
        model = Contact
        fields = ['correo', 'asunto', 'mensaje', 'solicitud']

    def validate_solicitud(self, value):
        if value:
            raise serializers.ValidationError("Campo no permitido.")
        return value