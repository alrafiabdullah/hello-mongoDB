from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'username',
                  'password', 'password2', 'date_joined', 'is_staff']
        extra_kwargs = {
            'password': {'write_only': True},
            'date_joined': {'read_only': True},
            'is_staff': {'read_only': True}
        }

    def create(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Password must match!'})

        user.set_password(password)
        user.save()
