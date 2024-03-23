from django.urls import path
from .views import (
    CreateShortenLinkView,
    CreateLinkClickView,
    LinkStatisticByDaysView,
    LinkStatisticByTimeOfDayView,
    TopTenLinksView,
)

urlpatterns = [
    path('create-shorten-link/', CreateShortenLinkView.as_view(), name='create_shorten_link'),
    path('create-link-click/', CreateLinkClickView.as_view(), name='create_link_click'),
    path('link-statistics-by-days/<int:pk>/', LinkStatisticByDaysView.as_view(), name='link_statistics_by_days'),
    path(
        'link-statistics-by-time-of-the-day/<int:pk>/',
        LinkStatisticByTimeOfDayView.as_view(),
        name='link_statistics_by_time_of_the_day'
    ),
    path('top-ten-links/', TopTenLinksView.as_view(), name='top_ten_links'),
]
