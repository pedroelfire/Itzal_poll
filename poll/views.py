from rest_framework import generics, status
from rest_framework.response import Response
from django.core.cache import cache
from .serializers import ContactSerializer
from .models import Contact

class ContactCreateAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def create(self, request, *args, **kwargs):
        # Limitar peticiones por hora (Rate limiting)
        user_ip = request.META.get('REMOTE_ADDR')
        if cache.get(user_ip):
            return Response({"detail": "Has alcanzado el límite de peticiones. Intenta más tarde."}, status=status.HTTP_429_TOO_MANY_REQUESTS)
        
        # Establecer límite de peticiones a una por hora
        cache.set(user_ip, True, timeout=3600)  # 1 hora

        # Validar y guardar los datos
        return super().create(request, *args, **kwargs)