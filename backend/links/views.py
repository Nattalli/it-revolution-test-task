from rest_framework import generics
from rest_framework.response import Response
from .models import Link
from .serializers import CreateLinkSerializer, CreateLinkClickSerializer
import pyshorteners


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
