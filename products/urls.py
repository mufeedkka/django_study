from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter




router = DefaultRouter()
router.register(r"countries", views.CountryViewSet)
urlpatterns = [
    path('test/', views.index, name="index"),
    path('signup/',views.signup, name="signup"),
    path('login/',views.loginpage, name="login"),
    path('details/<int:id>',views.details, name="details"),
    path('', include(router.urls)),
]