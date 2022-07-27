from django.urls import path
from polls import views
from django.urls import URLPattern

app_name = 'youtube'

urlpatterns = [
    # path('list/', views.Youtube_information.as_view(), name = 'Youtube_info'),
    # path('', views.Youtube_information.as_view(), name = 'Youtube_info')
    path('list/', views.Youtube_information.as_view(), name = 'youtube_info'),
]
