from rest_framework import viewsets, permissions
from .models import GalleryImage
from .serializers import GalleryImageSerializer

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow safe methods to anyone
        if request.method in permissions.SAFE_METHODS:
            return True
        # For write: only authenticated users (you can restrict to staff)
        return request.user and request.user.is_authenticated and request.user.is_staff

class GalleryImageViewSet(viewsets.ModelViewSet):
    queryset = GalleryImage.objects.order_by('-uploaded_at')
    serializer_class = GalleryImageSerializer
    permission_classes = [IsAdminOrReadOnly]