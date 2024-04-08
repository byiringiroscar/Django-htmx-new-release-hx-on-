from django.urls import path


from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('content/', views.htmx_content, name='htmx-content'),
]