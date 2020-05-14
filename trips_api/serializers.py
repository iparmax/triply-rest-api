from rest_framework import serializers

from . import models


class TripsSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta:
        model = models.Trip
        fields = ("user_id", "email", "origin","destination","dep_time")

    def create(self, validated_data):
        """Create and return a new user."""

        user = models.Trip(
            email=validated_data["email"],
            user_id=validated_data["user_id"],
            origin=validated_data["origin"],
            destination=validated_data["destination"],
            dep_time=validated_data["dep_time"]
        )

        user.save()

        return user