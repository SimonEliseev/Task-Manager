from django.urls import include, path
from rest_framework import routers

from tasks.api.viewsets import TaskViewSet, CommentViewSet, StatusViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'statuses', StatusViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
