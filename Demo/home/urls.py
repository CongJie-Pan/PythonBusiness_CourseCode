from django.contrib import admin
from django.urls import path, include  # Remove the dot before include
from . import views

urlpatterns = [
    # Don't use below, otherwise you will get a recursion error
    # Reason:
    # Warning: Including empty path patterns can trigger infinite recursion in URL routing
    # Best practice: Use specific path patterns or direct view assignments to prevent recursion errors
    # ---
    # path('admin/', admin.site.urls),
    #path('', include('home.urls')),
    #---
    path('',views.simple_crawl),
    path('welcome/',views.hello),
]