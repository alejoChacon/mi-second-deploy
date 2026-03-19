from rest_framework import serializers
from apps.users.models import User
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True,required=True,validators=[validate_password])

    class Meta:
        model = User
        fields = ['avatar','first_name','last_name','role','username','email','password','password2']

    def validate(self, attrs):
        password = attrs['password']
        password2 = attrs['password2']
        if password != password2:
            raise serializers.ValidationError('Las contraseñas no coinciden')
        return attrs

    def create(self, validated_data):
        password2 = validated_data.pop('password2',"")
        user = User(**validated_data)
        user.set_password(password2)
        user.save()
        return user

    def update(self, instance, validated_data):
        password2 = validated_data.pop('password2',"")
        profile_phote = validated_data.get('avatar')
        if profile_phote:
            instance.avatar.delete()
        return super().update(instance, validated_data)
    
    def to_representation(self, instance):
        return {
            'Id':instance.id,
            'Nombre Completo': instance.get_full_name(),
            "Rol": instance.role,
            "Avatar_url": instance.avatar.url,
            "Username": instance.username,
            "Email": instance.email
        }
    
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class TokenSerializado(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        data['user'] = self.user.get_full_name() or self.user.username
        data['State'] = self.user.role
        return data