from rest_framework.routers import DefaultRouter
from .views.project_viewset import ProjectViewSet
from .views.task_viewset import TaskViewSet

router = DefaultRouter()

router.register(r"projects",ProjectViewSet,basename='projects')
router.register(r"tasks",TaskViewSet,basename="tasks")

urlpatterns = router.urls