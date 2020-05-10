from rest_framework import serializers

from user.models import Profile

class ProfileSerializer(serializers.ProfileSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'Following', 'Followers', 'profile_photo', 'DOB']