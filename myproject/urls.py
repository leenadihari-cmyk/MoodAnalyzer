from django.contrib import admin
from django.urls import path
from server.views import home, dealer_detail, post_review

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('dealer/<int:dealer_id>/', dealer_detail, name="dealer_detail"),
    path('dealer/<int:dealer_id>/review/', post_review, name="post_review"),
]