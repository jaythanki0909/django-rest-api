from django.urls import path,include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('hello2',views.HelloViewSet,basename='hello-viewset')
router.register('profile',views.UserProfileViewSet)
router.register('feed',views.UserProfileFeedViewSet)
urlpatterns = [
    path('hello/',views.HelloApiView.as_view()),
    path('login/',views.UserLoginAPIView.as_view()),
    path('',include(router.urls))


]
    