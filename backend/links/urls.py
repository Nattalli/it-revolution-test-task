from django.urls import path
from .views import CreateShortenLinkView

urlpatterns = [
    path('create-shorten-link/', CreateShortenLinkView.as_view(), name='create_shorten_link'),
]
