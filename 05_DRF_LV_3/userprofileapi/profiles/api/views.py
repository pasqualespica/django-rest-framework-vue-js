# from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from profiles.models import Profile
from profiles.api.serializers import ProfileSerializers

from rest_framework.viewsets import ReadOnlyModelViewSet

# class ProfileList(generics.ListAPIView):
class ProfileViewSet(ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers
    permission_classes = [IsAuthenticated]