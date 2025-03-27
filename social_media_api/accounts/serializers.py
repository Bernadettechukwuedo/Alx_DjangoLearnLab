from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User = get_user_model()
class FollowSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()

    def validate_user_id(self, value):
        """Verify user exists"""
        try:
            User.objects.get(id=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found")
        return value
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField()

    class Meta:
        model = get_user_model()
        fields = ["id", "password", "email", "bio", "profile_picture"]

    def validate(self, data):
        if len(data["password"]) <= 4:
            raise serializers.ValidationError(
                "Password is too weak. It should be more than 4 characters."
            )

        return data

    def create(self, validated_data):
        password = validated_data.pop("password")
        email = validated_data.pop("email", None)
        user = get_user_model().objects.create_user(
            **validated_data, password=password, email=email
        )
        Token.objects.create(user=user)
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        if email and password:
            user = authenticate(email=email, password=password)

            if user and user.is_active:
                return user
            else:
                raise serializers.ValidationError("Invalid credentials")
        else:
            raise serializers.ValidationError("Email and password is required")


class UserProfileSerializer(serializers.ModelSerializer):
    follower_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ["id", "bio", "profile_picture", "follower_count", "following_count"]

    def get_follower_count(self, obj):
        return obj.followers.count()

    def get_following_count(self, obj):
        return obj.following.count()
