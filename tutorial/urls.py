from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TutorialMVS

router=DefaultRouter()
router.register("tutorials",TutorialMVS)

# urlpatterns = [
    # path(),
# ]

urlpatterns=router.urls