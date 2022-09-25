__author__ = 'Muchai Noah'
from rest_framework import serializers


class CurrentUserSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
