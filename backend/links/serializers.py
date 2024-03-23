from rest_framework import serializers

from .validators import validate_existing_link
from .models import Link


class CreateLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('full_link', 'title')

    full_link = serializers.CharField(validators=[validate_existing_link])
