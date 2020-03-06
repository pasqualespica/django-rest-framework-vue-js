from rest_framework import serializers
from profiles.models import Profile, ProfileStatus


class ProfileSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = Profile
        fields = "__all__"

class ProfileAvatarSerializers(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ["avatar"]


class ProfileStatusSerializers(serializers.ModelSerializer):
    user_profile = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ProfileStatus
        fields = "__all__"
   
