from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth import authenticate

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','username', 'email', 'password', 'role']
    


# for register
class RegitserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    phone = serializers.CharField(required=True)
    address =  serializers.CharField(required=True)
    email = serializers.EmailField()
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'password2', 'role', 'phone', 'address']
        extra_kwargs = {
            "role": {"required": True},
            "password": {'required': True},
            "phone": {'required': True},
            "address": {'required': True},

        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def validate_email(self, value):
        if UserProfile.objects.filter(email=value).exists():
            raise serializers.ValidationError('This email address is already in use.')
        return value


    def create(self, validated_data):
        role = validated_data['role']
        user = UserProfile.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role = role
        )
        return user
    
    
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    data['user'] = user
                else:
                    raise serializers.ValidationError('User account is disabled')
            else:
                raise serializers.ValidationError('User account is disabled')
            
        else:
            raise serializers.ValidationError('Must include "username and password"')
        return data