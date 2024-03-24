import pyshorteners
from django.db.models import Count, F
from django.db.models.functions import ExtractHour
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .models import Link, LinkClick
from .serializers import (
    CreateLinkSerializer,
    CreateLinkClickSerializer,
    LinkStatisticByDaySerializer,
    LinkStatisticByTimeOfDaySerializer,
    TopTenLinksSerializer
)


class CreateShortenLinkView(generics.CreateAPIView):
    serializer_class = CreateLinkSerializer

    def create(self, request, *args, **kwargs):
        full_link = request.data.get('full_link')
        title = request.data.get('title', None)

        shortener = pyshorteners.Shortener()
        short_link = shortener.tinyurl.short(full_link)

        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            response_data = {
                'error_message': e.detail,
                'short_link': short_link,
                'link_id': Link.objects.filter(short_link=short_link).first().id
            }
            return Response(response_data, status=400)

        link = Link.objects.create(full_link=full_link, short_link=short_link, title=title)

        response_data = serializer.data
        response_data['short_link'] = short_link
        response_data['id'] = link.id

        return Response(response_data)


class CreateLinkClickView(generics.CreateAPIView):
    serializer_class = CreateLinkClickSerializer


class LinkStatisticByDaysView(generics.RetrieveAPIView):
    serializer_class = LinkStatisticByDaySerializer

    def get_queryset(self):
        return Link.objects.all()

    def retrieve(self, request, *args, **kwargs):
        link = self.get_object()
        click_statistics = LinkClick.objects.filter(link=link).values('clicked_at__date').annotate(
            click_count=Count('id')
        )

        statistics_by_day = {}
        for entry in click_statistics:
            statistics_by_day[str(entry['clicked_at__date'])] = entry['click_count']

        return Response(statistics_by_day)


class LinkStatisticByTimeOfDayView(generics.RetrieveAPIView):
    serializer_class = LinkStatisticByTimeOfDaySerializer

    def get_queryset(self):
        return Link.objects.all()

    def retrieve(self, request, *args, **kwargs):
        link = self.get_object()

        click_statistics = LinkClick.objects.filter(link=link).annotate(
            hour_truncated=ExtractHour('clicked_at')
        ).values('hour_truncated').annotate(
            click_count=Count('id')
        )

        click_count_by_hour = {hour: 0 for hour in range(24)}

        for entry in click_statistics:
            hour_truncated = entry['hour_truncated']
            click_count = entry['click_count']
            click_count_by_hour[hour_truncated] = click_count

        return Response(click_count_by_hour)


class TopTenLinksView(generics.ListAPIView):
    serializer_class = TopTenLinksSerializer

    def get_queryset(self):
        return Link.objects.annotate(
            click_count=Count('linkclick'),
            creation_date=F('created_at')
        ).order_by('-click_count')[:10]
