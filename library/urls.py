from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, BookViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'books', BookViewSet)


#  urls for the API
urlpatterns = [
    path('api/', include(router.urls)),
]

