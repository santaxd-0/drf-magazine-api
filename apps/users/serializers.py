from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    # TODO add some data about what products user bought or user will buy

    class Meta:
        model = User
        fields = ["email", "username", "first_name", "last_name", "birth_date", "bonuses"]