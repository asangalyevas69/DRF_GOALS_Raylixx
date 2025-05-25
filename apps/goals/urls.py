from rest_framework.routers import DefaultRouter
from .views import GoalViewSet, StepViewSet

router = DefaultRouter()
router.register(r'goals', GoalViewSet, basename='goal')
router.register(r'steps', StepViewSet, basename='step')

urlpatterns = router.urls
