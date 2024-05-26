from django.urls import path
from apps.base.views import index, blog_details

urlpatterns = [
    path('', index, name='index'),
    path('blog-details/<int:id>/', blog_details, name='blog_details'),
    
]
