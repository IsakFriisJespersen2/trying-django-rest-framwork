from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views


router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename="snippet")
router.register(r'comments', views.CommentsViewSet, basename="comments")
router.register(r'users', views.UserViewSet, basename="user")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
