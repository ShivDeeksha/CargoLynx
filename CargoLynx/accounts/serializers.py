from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=User.ROLES)
    license_image = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = ['role', 'id', 'username', 'first_name', 'last_name', 'email', 'password', 'middle_name', 'contact_info', 'address', 'city', 'pincode', 'nationality', 'dob', 'company_name', 'id_proof', 'license_image']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        license_image_data = validated_data.pop('license_image', None)
        user = User.objects.create_user(**validated_data)
        if license_image_data:
            user.license_image = license_image_data
            user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
