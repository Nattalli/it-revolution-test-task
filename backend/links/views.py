from rest_framework import generics
from rest_framework.response import Response
from .models import Link, LinkClick
from .serializers import CreateLinkSerializer, CreateLinkClickSerializer, LinkStatisticsSerializer
import pyshorteners
from django.db.models import Count


class CreateShortenLinkView(generics.CreateAPIView):
    serializer_class = CreateLinkSerializer

    def create(self, request, *args, **kwargs):
        full_link = request.data.get('full_link')
        title = request.data.get('title', None)

        shortener = pyshorteners.Shortener()
        short_link = shortener.tinyurl.short(full_link)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        Link.objects.create(full_link=full_link, short_link=short_link, title=title)
        return Response(serializer.data)


class CreateLinkClickView(generics.CreateAPIView):
    serializer_class = CreateLinkClickSerializer


class LinkStatisticsView(generics.RetrieveAPIView):
    serializer_class = LinkStatisticsSerializer

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
