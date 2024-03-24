from rest_framework import serializers
from .models import Link


def validate_existing_link(value):
    if Link.objects.filter(full_link=value).exists():
        raise serializers.ValidationError(
            f"This link is already exists in our database:",
        )
