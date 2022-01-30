from rest_framework import routers

from climbdit.views import StateViewSet, LocationViewSet, ClimberViewSet, ClimbViewSet


router = routers.DefaultRouter()
router.register('state', StateViewSet)
router.register('location', LocationViewSet)
router.register('climber', ClimberViewSet)
router.register('climb', ClimbViewSet)

urlpatterns = router.urls