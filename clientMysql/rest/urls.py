from django.urls import include, path
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'PktRecordLog', views.PktRecordLogViewSet)
router.register(r'Pktreader', views.PktreaderViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title="VR-Admin portal API",
        default_version='v1',
        # description="VR-Admin REST API",
        # terms_of_service="https://www.google.com/policies/terms/",
        # contact=openapi.Contact(email="vradmin@neolant.com"),
        # license=openapi.License(name="EULA"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
)
urlpatterns = [
    path('', include(router.urls)),
    path('rest-api.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger'),
]
