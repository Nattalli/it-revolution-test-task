from django.urls import path
from .views import CreateShortenLinkView, CreateLinkClickView

urlpatterns = [
    path('create-shorten-link/', CreateShortenLinkView.as_view(), name='create_shorten_link'),
    path('create-link-click/', CreateLinkClickView.as_view(), name='create_link_click'),
]
