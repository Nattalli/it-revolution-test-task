from rest_framework import serializers

from .validators import validate_existing_link
from .models import Link, LinkClick


class CreateLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('full_link', 'title')

    full_link = serializers.CharField(validators=[validate_existing_link])


class CreateLinkClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkClick
        fields = ('link',)


class LinkStatisticsSerializer(serializers.ModelSerializer):
    click_count = serializers.IntegerField()

    class Meta:
        model = Link
        fields = ('full_link', 'short_link', 'title', 'click_count')
