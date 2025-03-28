from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    target = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ["recipient", "actor", "verb", "target", "timestamp"]

    def get_target(self, obj):
        """Return a serialized version of the target object."""
        if obj.target:
            return str(obj.target) 
        return None
