from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'cars'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('cars/api/', include('cars.apiurls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
