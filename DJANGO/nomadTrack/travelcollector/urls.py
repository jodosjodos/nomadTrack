
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("travel.urls")),
    path("checklist/", include("checklist.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("account/", include("userApp.urls")),
]
