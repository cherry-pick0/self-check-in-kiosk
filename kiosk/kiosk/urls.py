"""kiosk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from api.token_auth import CustomAuthToken
from api.v1.guest_registrations import GuestRegistrationsViewSet
from api.v1.kiosk_managers import KioskManagersViewSet
from api.v1.kiosk_users import KioskUsersViewSet
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash="")
router.register(
    r"v1/guest-registrations", GuestRegistrationsViewSet, basename="guest-registrations"
)
router.register(r"v1/kiosk-managers", KioskManagersViewSet, basename="kiosk-managers")
router.register(r"v1/kiosk-users", KioskUsersViewSet, basename="kiosk-users")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token-auth", CustomAuthToken.as_view()),
    path("api/", include(router.urls)),
]
