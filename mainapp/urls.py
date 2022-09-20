
from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.urls import re_path as url
urlpatterns = [
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
    path('',views.home,name='home'),
    path('submit',views.message,name='submit')
]