from django.contrib import admin
from django.conf.urls import include, url
from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

router = DefaultRouter()

schema_view = get_swagger_view(title="Peacedev Team")

PREFIX_URL = settings.PREFIX_URL
urlpatterns = [
    url(f"^{PREFIX_URL}$", schema_view),
    url(f"^{PREFIX_URL}admin/", admin.site.urls),
    url(f"^{PREFIX_URL}auth/", include("rest_auth.urls")),
    url(f"^{PREFIX_URL}api/", include(router.urls)),
    url(f"^{PREFIX_URL}api/v1/account/", include("backend.apps.account.urls")),
]
