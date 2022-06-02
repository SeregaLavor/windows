from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('windows/', views.all_windows, name='all_windows'),
    path('window/<int:window_id>/', views.window_detail, name='window'),
    #path('review/<int:review_id>/', views.review, name='review'),
]